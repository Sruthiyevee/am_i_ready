"""
groq_service.py - Groq LLM Integration for "Am I Exam-Ready?"
Provides high-speed, personalized German A1 exam coaching, automated
study roadmap generation, question deep-dive analysis, and interactive tutoring.
"""

import os
from typing import Dict, Any, List, Optional
import streamlit as st

# Attempt dotenv loading safely
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Attempt Groq client import
try:
    from groq import Groq
except ImportError:
    Groq = None

# Default Recommended Groq Models
DEFAULT_MODEL = "llama-3.3-70b-versatile"
FAST_MODEL = "llama-3.1-8b-instant"
AVAILABLE_MODELS = [
    ("llama-3.3-70b-versatile", "Llama 3.3 70B (High Precision & Reasoning)"),
    ("llama-3.1-8b-instant", "Llama 3.1 8B (Ultra Fast, Low Latency)"),
]


def get_groq_api_key() -> Optional[str]:
    """
    Retrieves the Groq API Key checking in order:
    1. Streamlit session state ('groq_api_key') entered by user in UI
    2. Environment variable ('GROQ_API_KEY') from .env or system environment
    3. Streamlit secrets ('st.secrets["GROQ_API_KEY"]')
    """
    # 1. User UI session input
    if hasattr(st, "session_state"):
        ui_key = st.session_state.get("groq_api_key")
        if ui_key and str(ui_key).strip():
            return str(ui_key).strip()

    # 2. Environment variable (.env or OS)
    env_key = os.getenv("GROQ_API_KEY")
    if env_key and str(env_key).strip():
        return str(env_key).strip()

    # 3. Streamlit secrets (for cloud deployments)
    try:
        if hasattr(st, "secrets") and "GROQ_API_KEY" in st.secrets:
            sec_key = st.secrets["GROQ_API_KEY"]
            if sec_key and str(sec_key).strip():
                return str(sec_key).strip()
    except Exception:
        pass

    return None


def is_groq_available() -> bool:
    """Returns True if the Groq SDK is installed and an API key is configured."""
    if Groq is None:
        return False
    key = get_groq_api_key()
    return bool(key and len(key) > 5)


def get_groq_client(api_key: Optional[str] = None):
    """Initializes and returns an authenticated Groq client."""
    if Groq is None:
        raise ImportError(
            "The 'groq' package is not installed. Please run: pip install groq"
        )
    key = api_key or get_groq_api_key()
    if not key:
        raise ValueError(
            "Groq API Key is not configured. Please add GROQ_API_KEY to your .env file, "
            "set it in Streamlit secrets, or enter it in the app sidebar."
        )
    return Groq(api_key=key)


def generate_study_plan(
    result: Dict[str, Any],
    questions: List[Dict[str, Any]],
    user_answers: Dict[int, int],
    model: str = DEFAULT_MODEL,
    api_key: Optional[str] = None,
) -> str:
    """
    Generates a personalized 7-day study plan & exam strategy based on
    the student's diagnostic results, tier, and specific missed questions.
    """
    client = get_groq_client(api_key=api_key)

    tier_label = result.get("tier_label", "Unknown")
    overall_pct = result.get("overall_percentage", 0)
    overall_score = result.get("overall_score", 0)
    total_q = result.get("total_questions", 12)
    breakdown = result.get("skill_breakdown", {})

    vocab_pct = breakdown.get("Vocabulary", {}).get("percentage", 0)
    grammar_pct = breakdown.get("Grammar", {}).get("percentage", 0)
    reading_pct = breakdown.get("Reading", {}).get("percentage", 0)

    # Compile missed topics and questions
    missed_items = []
    for q in questions:
        qid = q["id"]
        user_choice = user_answers.get(qid)
        correct_choice = q["correct_answer_index"]
        if user_choice is None or user_choice != correct_choice:
            user_text = q["options"][user_choice] if user_choice is not None else "None selected"
            correct_text = q["options"][correct_choice]
            missed_items.append(
                f"- Category: {q['category']} | Subtopic: {q['subtopic']}\n"
                f"  Prompt: {q['prompt']}\n"
                f"  Learner answered: '{user_text}' (Correct was: '{correct_text}')"
            )

    missed_summary = "\n".join(missed_items) if missed_items else "None! Student scored 100% on all diagnostic questions."

    system_prompt = (
        "You are an encouraging, world-class German language teacher and official Goethe-Institut / ÖSD "
        "A1 certified examiner. Your role is to provide actionable, uplifting, and pedagogical advice to learners "
        "preparing for the Goethe-Zertifikat A1 (Start Deutsch 1) or ÖSD Zertifikat A1 exams.\n\n"
        "Guidelines:\n"
        "1. Be concise, highly structured, motivating, and realistic.\n"
        "2. Address their specific performance tier directly.\n"
        "3. Provide a day-by-day 7-day high-yield study blueprint targeting their weakest areas.\n"
        "4. Include 2-3 memorable mnemonic tricks ('Eselsbrücken') for their specific missed grammar/vocab concepts.\n"
        "5. Include 1 official Goethe/ÖSD exam day strategy tip.\n"
        "6. Format with clean GitHub Markdown, bullet points, and emoji headings."
    )

    user_prompt = f"""Learner Diagnostic Profile:
- Readiness Verdict: {tier_label}
- Overall Score: {overall_pct}% ({overall_score}/{total_q} questions correct)
- Pillar Breakdown:
  * 📚 Vocabulary: {vocab_pct}%
  * 🧩 Grammar: {grammar_pct}%
  * 📖 Reading: {reading_pct}%

Specific Missed Questions / Needs Work:
{missed_summary}

Please generate an inspiring, highly customized 7-Day Study Action Plan and Exam Day Strategy tailored specifically to their diagnostic results."""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.6,
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Unable to generate AI study plan via Groq: {str(e)}"


def explain_question_deep_dive(
    question: Dict[str, Any],
    user_selected_idx: Optional[int],
    language: str = "English",
    model: str = DEFAULT_MODEL,
    api_key: Optional[str] = None,
) -> str:
    """
    Generates a deep-dive, pedagogical explanation for a specific question,
    explaining grammatical rules, why options are right/wrong, and offering practice examples.
    """
    client = get_groq_client(api_key=api_key)

    qid = question["id"]
    prompt = question["prompt"]
    options = question["options"]
    correct_idx = question["correct_answer_index"]
    correct_text = options[correct_idx]
    user_text = options[user_selected_idx] if user_selected_idx is not None else "No answer"
    category = question.get("category", "")
    subtopic = question.get("subtopic", "")
    context_snippet = question.get("context_snippet", "")

    lang_instr = (
        "Respond entirely in English, but keep German examples and terms clearly formatted in bold/backticks."
        if "English" in language
        else "Antworte auf Deutsch mit einfacher, klarer Sprache für Deutschlernende auf A1/A2 Niveau."
    )

    system_prompt = (
        f"You are a friendly German A1 tutor assisting a student who just took an A1 diagnostic test question. "
        f"{lang_instr}\n\n"
        f"Structure your response clearly:\n"
        f"1. **Core Rule / Concept**: Explain the underlying grammatical rule or vocabulary principle in 2-3 sentences.\n"
        f"2. **Why the Answer is Correct**: Clarify why '{correct_text}' is the right solution.\n"
        f"3. **Common Trap / Pitfall**: Explain why other options (like '{user_text}') might deceive learners.\n"
        f"4. **Practice Examples**: 2 natural German example sentences showing how native speakers use this.\n"
        f"5. **Exam Tip**: 1 short, memorable rule-of-thumb for the Goethe/ÖSD A1 test."
    )

    user_content = f"""Question {qid}:
Category: {category} ({subtopic})
Context / Passage: {context_snippet or 'None'}
Question Prompt: {prompt}
Options:
- A) {options[0]}
- B) {options[1]}
- C) {options[2]}
{f'- D) {options[3]}' if len(options) > 3 else ''}

Student Selected: {user_text}
Correct Answer: {correct_text}
"""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            temperature=0.5,
            max_tokens=800,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Unable to fetch Groq AI explanation: {str(e)}"


def ask_groq_tutor(
    user_query: str,
    context: Optional[str] = None,
    language: str = "English",
    model: str = DEFAULT_MODEL,
    api_key: Optional[str] = None,
) -> str:
    """
    Answers general German A1 learning questions, grammar dilemmas, or vocabulary queries.
    """
    client = get_groq_client(api_key=api_key)

    lang_instr = (
        "Respond in English with German terms and examples."
        if "English" in language
        else "Antworte auf Deutsch in verständlicher Sprache für A1/A2 Lernende."
    )

    system_prompt = (
        f"You are Groq German Coach, an expert AI tutor for A1 German learners taking Goethe or ÖSD exams. "
        f"{lang_instr}\n"
        f"Keep explanations warm, practical, concise, and focused on CEFR A1 scope. "
        f"Always provide 1-2 practical German example sentences with translations."
    )

    messages = [{"role": "system", "content": system_prompt}]
    if context:
        messages.append({"role": "system", "content": f"Context regarding learner's recent test: {context}"})
    messages.append({"role": "user", "content": user_query})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.6,
            max_tokens=600,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Groq Tutor Error: {str(e)}"
