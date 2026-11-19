"""
readiness.py - Pure Scoring, Tier Evaluation, and Personalized Recommendation Engine.
Evaluates Goethe-Zertifikat A1 & ÖSD Zertifikat A1 exam readiness.

Benchmarks:
- Real Goethe/ÖSD passing benchmark is 60%.
- Safety buffer tiers:
  * Ready to Book (Green): Overall >= 80% AND every category >= 60%.
  * Almost Ready (Amber): Overall 65% - 79% OR overall >= 80% with one skill < 60%.
  * Not Ready Yet (Red): Overall < 65%.
"""

from typing import List, Dict, Any, Optional
import sys
import os

# Ensure questions can be imported regardless of execution context
try:
    from data.questions import QUESTIONS, CATEGORIES
except ImportError:
    try:
        from questions import QUESTIONS, CATEGORIES
    except ImportError:
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data")))
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "phase_2_question_bank")))
        from questions import QUESTIONS, CATEGORIES

# Knowledge Base of Actionable Recommendations Mapped to Missed Subtopics
SUBTOPIC_RECOMMENDATIONS = {
    "Articles (der/die/das)": {
        "title": "Mastering Definite Articles & Akkusativ Case",
        "action": (
            "Learn every new German noun together with its color-coded article (der = blue, die = red, das = green). "
            "Drill the Akkusativ case with transitive verbs like 'kaufen', 'haben', and 'brauchen' that force masculine 'der' into 'den'."
        ),
        "tip": "Tip: Group nouns by reliable gender endings (e.g. -ung, -heit, -keit are 100% feminine/die; -chen, -lein are das).",
    },
    "Present Tense Verb Conjugation": {
        "title": "Irregular & Stem-Changing Verb Conjugations",
        "action": (
            "Review present tense verb paradigms, especially 2nd and 3rd person singular stem vowels "
            "(e -> i/ie, a -> ä) such as 'sprechen -> du sprichst' and 'fahren -> er fährt'."
        ),
        "tip": "Tip: Write out 5 daily sentences with common irregular verbs (sehen, lesen, treffen, nehmen).",
    },
    "Prepositions (im, am, um, nach)": {
        "title": "Temporal Prepositions Formula: am / um / im",
        "action": (
            "Anchor the temporal rule: use 'am' for days and parts of the day (am Montag, am Morgen), "
            "'um' for exact clock times (um 14:00 Uhr), and 'im' for months and seasons (im August, im Sommer)."
        ),
        "tip": "Tip: Draft your daily routine using only 'am' and 'um' to build reflex memory.",
    },
    "Negation (nicht/kein)": {
        "title": "Distinguishing 'nicht' vs. 'kein/keine/keinen'",
        "action": (
            "Use 'kein-' exclusively to negate nouns with an indefinite article ('ein/eine') or no article. "
            "Use 'nicht' for verbs, adjectives, adverbs, proper names, and nouns with definite articles ('der/die/das')."
        ),
        "tip": "Tip: Remember case endings: masculine accusative is 'keinen' (keinen Kaffee), feminine is 'keine' (keine Zeit).",
    },
    "Food & Everyday Shopping": {
        "title": "Everyday Food & Packaging Quantity Vocabulary",
        "action": (
            "Drill shopping measurement nouns: 'ein Laib Brot', 'eine Flasche Wasser', 'ein Becher Joghurt', "
            "and 'ein Glas Marmelade'. Practice realistic market and supermarket dialogues."
        ),
        "tip": "Tip: Review the Goethe A1 Wortliste section 'Essen und Trinken' (high-yield 50 words).",
    },
    "City & Directions": {
        "title": "Navigating City Directions & Spatial Adverbs",
        "action": (
            "Master essential direction phrases: 'nach links', 'nach rechts', 'geradeaus', 'an der Kreuzung', "
            "and 'gegenüber von'. Note that 'dort' takes 'dorthin' for movement."
        ),
        "tip": "Tip: Describe your route from home to work out loud in German using directional words.",
    },
    "Time & Schedule Expressions": {
        "title": "Colloquial vs. Official Clock Expressions",
        "action": (
            "Master informal German clock expressions: 'Viertel vor' (quarter to), 'Viertel nach' (quarter past), "
            "and 'halb' (half past). Note: 'halb drei' is 14:30 (half-way to 3), never 15:30!"
        ),
        "tip": "Tip: Switch your phone or clock to German and read the time aloud throughout the day.",
    },
    "Professions & Personal Details": {
        "title": "Career Prepositions: 'arbeiten als' vs. 'bei'",
        "action": (
            "Use 'arbeiten als + Beruf' for your profession (e.g. 'Ich arbeite als Ingenieur') "
            "and 'arbeiten bei + Firma' for your employer (e.g. 'Ich arbeite bei Siemens')."
        ),
        "tip": "Tip: Perfect your 60-second self-introduction for Part 1 of the Goethe/ÖSD Sprechen module.",
    },
    "Reading Personal Messages": {
        "title": "Scanning Informal Emails & Personal Invitations",
        "action": (
            "Scan informal emails for key logistical data: date, starting time, venue ('ab 19 Uhr im Garten'), "
            "RSVP requests ('bis Donnerstag Bescheid sagen'), and items to bring ('Salat / Nachtisch')."
        ),
        "tip": "Tip: Highlight WH-questions (Wer? Wann? Wo? Was?) on your first read of any text.",
    },
    "Reading Notices & Opening Hours": {
        "title": "Interpreting Public Signs & Schedule Exceptions",
        "action": (
            "Pay close attention to restriction markers on public notices: 'geschlossen' (closed), "
            "'kein Zutritt' (no entry), and exception clauses such as 'außer an Feiertagen'."
        ),
        "tip": "Tip: Learn common clinic and public office words: Sprechzeiten, Notdienst, Öffnungszeiten.",
    },
    "Reading Timetables & Notices": {
        "title": "Reading Transit Displays & DB Timetables",
        "action": (
            "Train your eye to quickly extract transit data: 'Gleis' (platform), 'Abfahrt' (departure), "
            "'Ankunft' (arrival), and delay annotations ('+5 Min.', 'Fällt heute aus')."
        ),
        "tip": "Tip: Practice reading live departure tables on the Deutsche Bahn website in German.",
    },
    "Reading Short Advertisements": {
        "title": "Analyzing Rental & Classified Advertisements",
        "action": (
            "Carefully distinguish 'Kaltmiete' (base rent) from 'Warmmiete' (total rent including Nebenkosten). "
            "Verify move-in availability dates ('ab 1. August') and restrictions ('keine Haustiere')."
        ),
        "tip": "Tip: Check practice classifieds on real estate or marketplace listings in German.",
    },
}

# Exam-Day Success Tips for 100% Score
PERFECT_SCORE_TIPS = [
    {
        "title": "Exam-Day Pacing: Lesen & Schreiben (65 Minutes Total)",
        "action": (
            "In the Goethe/ÖSD A1 written exam, you have 65 minutes for Reading (Teil 1, 2, 3) and Writing (Teil 1, 2). "
            "Allocate 25 minutes for reading, 25 minutes for writing, and reserve a 15-minute buffer to review."
        ),
        "tip": "Tip: Transfer answers directly onto the official Antwortbogen — no additional transfer time is given!",
    },
    {
        "title": "Maximize Sprechen (Speaking) & Hören (Listening) Performance",
        "action": (
            "Since your reading, grammar, and vocabulary are exceptional, focus your remaining prep on Hören "
            "(audio plays twice in Teil 1 and 3) and practice making polite requests with prompt cards (Wortkarten) for Sprechen."
        ),
        "tip": "Tip: Practice asking spontaneous requests starting with 'Könnten Sie bitte...' and 'Darf ich...'.",
    },
]


def calculate_readiness(
    user_answers: Dict[int, int],
    questions: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """
    Pure calculation of overall score, category breakdown, readiness tier,
    and personalized practice recommendations.

    Args:
        user_answers: Mapping of question ID (1-12) to chosen option index (0-3).
                      Also supports 0-indexed question indices {0: opt, 1: opt, ...}.
        questions: Optional list of question dictionaries (defaults to QUESTIONS).

    Returns:
        Structured dictionary with scores, percentages, tier classification,
        verdict text, and actionable recommendations.
    """
    if questions is None:
        questions = QUESTIONS

    total_questions = len(questions)
    if total_questions == 0:
        raise ValueError("Questions list cannot be empty.")

    # Robust normalization: detect 0-indexed vs 1-indexed
    # If 0 is in user_answers and max(user_answers.keys()) < total_questions:
    is_zero_indexed = (
        len(user_answers) > 0 and
        0 in user_answers and
        max(user_answers.keys()) < total_questions
    )

    normalized_answers: Dict[int, int] = {}
    if is_zero_indexed:
        for idx, q in enumerate(questions):
            if idx in user_answers:
                normalized_answers[q["id"]] = user_answers[idx]
    else:
        for q in questions:
            qid = q["id"]
            if qid in user_answers:
                normalized_answers[qid] = user_answers[qid]

    # 1. Calculate overall and category scores
    total_correct = 0
    missed_questions = []

    category_stats: Dict[str, Dict[str, Any]] = {
        cat: {"score": 0, "total": 0, "percentage": 0.0, "status": "Needs Work", "status_color": "#EF4444"}
        for cat in CATEGORIES
    }

    for q in questions:
        qid = q["id"]
        cat = q["category"]
        category_stats[cat]["total"] += 1

        selected_opt = normalized_answers.get(qid)
        is_correct = (selected_opt is not None) and (selected_opt == q["correct_answer_index"])

        if is_correct:
            total_correct += 1
            category_stats[cat]["score"] += 1
        else:
            missed_questions.append({
                "question": q,
                "user_answer": selected_opt,
                "correct_answer": q["correct_answer_index"],
                "is_correct": False
            })

    # Overall percentage
    overall_percentage = round((total_correct / total_questions) * 100, 1)

    # Calculate per-category percentages & status labels
    for cat, stats in category_stats.items():
        if stats["total"] > 0:
            pct = round((stats["score"] / stats["total"]) * 100, 1)
            stats["percentage"] = pct
            if pct >= 80.0:
                stats["status"] = "Strong"
                stats["status_color"] = "#10B981"
            elif pct >= 60.0:
                stats["status"] = "Passing"
                stats["status_color"] = "#F59E0B"
            else:
                stats["status"] = "Needs Work"
                stats["status_color"] = "#EF4444"

    # Identify lowest-scoring skill (tie-breaker: Grammar > Vocabulary > Reading)
    sorted_skills = sorted(
        category_stats.items(),
        key=lambda item: (item[1]["percentage"], item[1]["score"])
    )
    lowest_scoring_skill = sorted_skills[0][0]
    min_skill_percentage = sorted_skills[0][1]["percentage"]

    # 2. Determine Readiness Tier
    # Ready to Book (Green): Overall >= 80% AND every category >= 60%
    if overall_percentage >= 80.0 and min_skill_percentage >= 60.0:
        tier = "ready"
        tier_label = "Ready to Book"
        tier_badge = "Exam-Ready"
        tier_color = "#10B981"
        badge_bg = "#ECFDF5"
        verdict = (
            "High confidence! You comfortably clear the 60% Goethe/ÖSD passing benchmark with an optimal safety buffer. "
            "You are ready to book your exam date."
        )

    # Almost Ready (Amber): Overall 65% - 79% OR overall >= 80% with one skill < 60%
    elif (65.0 <= overall_percentage < 80.0) or (overall_percentage >= 80.0 and min_skill_percentage < 60.0):
        tier = "almost"
        tier_label = "Almost Ready"
        tier_badge = "Needs Fine-Tuning"
        tier_color = "#F59E0B"
        badge_bg = "#FFFBEB"
        if overall_percentage >= 80.0 and min_skill_percentage < 60.0:
            verdict = (
                f"Strong overall score ({overall_percentage}%), but your {lowest_scoring_skill} score "
                f"({min_skill_percentage}%) is below the safety threshold. Spend 1–2 weeks drilling this area before booking."
            )
        else:
            verdict = (
                "Close to passing! You are near the benchmark, but exam fees are an investment (€100–€180). "
                "Dedicate 1–2 weeks to your focus areas below before booking."
            )

    # Not Ready Yet (Red): Overall < 65%
    else:
        tier = "not_ready"
        tier_label = "Not Ready Yet"
        tier_badge = "High Risk of Retake"
        tier_color = "#EF4444"
        badge_bg = "#FEF2F2"
        verdict = (
            "Not yet exam-ready. With an overall score below 65%, booking now carries a high risk of losing your registration fee. "
            "Build your core fundamentals with the priority focus areas below."
        )

    # 3. Generate Personalized Recommendations
    recommendations = generate_recommendations(missed_questions, lowest_scoring_skill)

    return {
        "overall_score": total_correct,
        "total_questions": total_questions,
        "overall_percentage": overall_percentage,
        "tier": tier,
        "tier_label": tier_label,
        "tier_badge": tier_badge,
        "tier_color": tier_color,
        "badge_bg": badge_bg,
        "verdict": verdict,
        "skill_breakdown": category_stats,
        "lowest_scoring_skill": lowest_scoring_skill,
        "min_skill_percentage": min_skill_percentage,
        "missed_questions": missed_questions,
        "recommendations": recommendations,
    }


def generate_recommendations(
    missed_questions: List[Dict[str, Any]],
    lowest_scoring_skill: str
) -> List[Dict[str, Any]]:
    """
    Produce 2-3 prioritized actionable recommendation cards.
    If 100% score (missed_questions empty), returns 2 exam-day tips.
    Otherwise, prioritizes subtopics from the lowest-scoring skill.
    """
    if len(missed_questions) == 0:
        # User scored 100%
        return [
            {
                "priority": idx + 1,
                "priority_label": f"Exam-Day Tip {idx + 1}",
                "subtopic": tip["title"],
                "category": "Exam Strategy",
                "action": tip["action"],
                "tip": tip["tip"],
            }
            for idx, tip in enumerate(PERFECT_SCORE_TIPS)
        ]

    # Prioritize missed questions: those belonging to lowest_scoring_skill come first
    def priority_sort_key(item: Dict[str, Any]) -> int:
        cat = item["question"]["category"]
        return 0 if cat == lowest_scoring_skill else 1

    sorted_missed = sorted(missed_questions, key=priority_sort_key)

    seen_subtopics = set()
    recommendations: List[Dict[str, Any]] = []

    for item in sorted_missed:
        q = item["question"]
        subtopic = q["subtopic"]
        category = q["category"]

        if subtopic not in seen_subtopics:
            seen_subtopics.add(subtopic)
            rec_content = SUBTOPIC_RECOMMENDATIONS.get(
                subtopic,
                {
                    "title": f"Review {subtopic}",
                    "action": f"Focus revision on {subtopic} within the {category} module.",
                    "tip": "Tip: Review the official Goethe A1 vocabulary list and grammar exercises.",
                }
            )

            priority_num = len(recommendations) + 1
            recommendations.append({
                "priority": priority_num,
                "priority_label": f"Priority {priority_num} Focus",
                "subtopic": subtopic,
                "category": category,
                "action": rec_content["action"],
                "tip": rec_content["tip"],
            })

            # Stop once we have 3 recommendations
            if len(recommendations) == 3:
                break

    # If user missed only 1 question, provide at least 2 recommendations by adding a general exam tip
    if len(recommendations) == 1:
        recommendations.append({
            "priority": 2,
            "priority_label": "Exam Strategy Tip",
            "subtopic": PERFECT_SCORE_TIPS[0]["title"],
            "category": "General Strategy",
            "action": PERFECT_SCORE_TIPS[0]["action"],
            "tip": PERFECT_SCORE_TIPS[0]["tip"],
        })

    return recommendations
