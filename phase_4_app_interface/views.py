"""
views.py - UI Renderers for "Am I Exam-Ready?"
Modern pastel neo-minimalist mobile-app aesthetic aligned with the design language:
warm cream/ivory background, soft pastel cards (sage green, coral pink, warm butter),
obsidian black pill CTAs (#18181B), and high-trust ed-tech typography.
"""

import streamlit as st
from typing import Dict, Any, List, Optional
import os
import sys

try:
    from utils.readiness import calculate_readiness
except ImportError:
    from readiness import calculate_readiness

try:
    from utils.groq_service import (
        DEFAULT_MODEL,
        AVAILABLE_MODELS,
        get_groq_api_key,
        is_groq_available,
        generate_study_plan,
        explain_question_deep_dive,
        ask_groq_tutor,
    )
except ImportError:
    try:
        from groq_service import (
            DEFAULT_MODEL,
            AVAILABLE_MODELS,
            get_groq_api_key,
            is_groq_available,
            generate_study_plan,
            explain_question_deep_dive,
            ask_groq_tutor,
        )
    except ImportError:
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils")))
        from groq_service import (
            DEFAULT_MODEL,
            AVAILABLE_MODELS,
            get_groq_api_key,
            is_groq_available,
            generate_study_plan,
            explain_question_deep_dive,
            ask_groq_tutor,
        )


def get_state(key: str, default: Any = None) -> Any:
    """Helper to safely retrieve a session state variable via attribute or item."""
    if hasattr(st.session_state, key):
        return getattr(st.session_state, key)
    elif isinstance(st.session_state, dict) and key in st.session_state:
        return st.session_state[key]
    return default


def set_state(key: str, value: Any):
    """Helper to safely set a session state variable via attribute or item."""
    if hasattr(st.session_state, "__setitem__"):
        st.session_state[key] = value
    try:
        setattr(st.session_state, key, value)
    except AttributeError:
        pass


def render_header(show_history_link: bool = True):
    """Renders the mobile phone status bar, app navigation header, and authority badge."""
    st.markdown("""<div class="mobile-status-bar">
<span>9:30</span>
<div style="display:flex; align-items:center; gap:0.45rem;">
<span>📶</span>
<span>🔋 100%</span>
</div>
</div>
<div class="mobile-app-header">
<div class="mobile-menu-btn" title="Navigation Menu">
<span>≡</span>
</div>
<div style="display:flex; flex-direction:column; align-items:center;">
<div class="de-accent-bar">
<div class="bar-black"></div>
<div class="bar-red"></div>
<div class="bar-gold"></div>
</div>
<div class="authority-pill">
<span>🇩🇪</span> Goethe & ÖSD A1 Diagnostic
</div>
</div>
<div class="mobile-avatar" title="Learner Profile">
<span>🧑‍🎓</span>
</div>
</div>""", unsafe_allow_html=True)


def render_landing_screen():
    """Renders the Landing Screen modeled after Screen 1 (Hero Rainbow Arches & Welcome Sheet)."""
    render_header()

    # 1. Hero Illustration Box (Screen 1 Rainbow Arches & Character)
    st.markdown("""<div class="hero-illustration-box">
<div class="hero-arcs">
<div class="hero-avatar-circle">
<span>👩‍🎓</span>
</div>
</div>
</div>""", unsafe_allow_html=True)

    # 2. Rounded Welcome Floating Sheet
    st.markdown("""<div class="ed-card" style="margin-top:-0.5rem; border-radius:32px; padding:2rem 1.75rem 1.75rem 1.75rem;">
<h1 style="font-size: 2.15rem; font-weight: 800; color: #18181B; line-height: 1.2; margin: 0 0 0.65rem 0; letter-spacing: -0.02em;">
Thrilled to Join Your German Learning Journey!
</h1>
<p style="font-size: 1.05rem; color: #52525B; line-height: 1.55; margin-bottom: 1.25rem;">
Excited to join your journey, making learning easy and fun as we reach goals together.
</p>
<div style="background:#FAF8F5; border:1px solid #E4E4E7; border-radius:16px; padding:0.9rem 1.1rem; margin-bottom:1.5rem; font-size:0.92rem; color:#3F3F46; line-height:1.5;">
💡 Exam registration fees range between <strong>€100 and €180</strong>. 
Take this official-format 12-question diagnostic across Vocabulary, Grammar, and Reading 
(~3 minutes) to objectively check if you are ready to book and pass on your first attempt.
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0.85rem; margin-bottom: 1.5rem;">
<div style="background:#FEF9EE; border:1px solid #FDE68A; border-radius:20px; padding:1.15rem;">
<span class="badge-pill badge-vocabulary" style="margin-bottom:0.4rem;">📚 4 Questions</span>
<h4 style="margin:0 0 0.25rem 0; font-size:1.02rem; font-weight:800; color:#18181B;">Vocabulary</h4>
<p style="margin:0; font-size:0.82rem; color:#71717A; line-height:1.45;">
Shopping, directions in town, clock times, family & jobs.
</p>
</div>
<div style="background:#FAF5FF; border:1px solid #E9D5FF; border-radius:20px; padding:1.15rem;">
<span class="badge-pill badge-grammar" style="margin-bottom:0.4rem;">🧩 4 Questions</span>
<h4 style="margin:0 0 0.25rem 0; font-size:1.02rem; font-weight:800; color:#18181B;">Grammar</h4>
<p style="margin:0; font-size:0.82rem; color:#71717A; line-height:1.45;">
Articles (der/die/das), accusative, verb endings, prepositions.
</p>
</div>
<div style="background:#F0FDF4; border:1px solid #A7F3D0; border-radius:20px; padding:1.15rem;">
<span class="badge-pill badge-reading" style="margin-bottom:0.4rem;">📖 4 Questions</span>
<h4 style="margin:0 0 0.25rem 0; font-size:1.02rem; font-weight:800; color:#18181B;">Reading</h4>
<p style="margin:0; font-size:0.82rem; color:#71717A; line-height:1.45;">
Informal emails, clinic notices, train timetables & ads.
</p>
</div>
</div>
<div style="display:flex; flex-wrap:wrap; gap:1rem; font-size:0.84rem; color:#71717A; margin-bottom:1.5rem; justify-content:center;">
<span>✓ <strong>100% Free</strong> & Client-Side</span>
<span>✓ <strong>Goethe/ÖSD 60% Benchmark</strong></span>
<span>✓ <strong>Instant Action Plan</strong></span>
</div>
</div>""", unsafe_allow_html=True)

    # 3. Slider-Style Pill Action Buttons
    if st.button("🚀 Start Readiness Check (3 mins)", use_container_width=True, type="primary"):
        set_state("page", "quiz")
        set_state("current_question_idx", 0)
        set_state("user_answers", {})
        set_state("validation_error", None)
        set_state("current_attempt_recorded", False)
        st.rerun()

    # Review Previous Tests CTA (Secondary Button)
    st.markdown("<div style='margin-top: 0.65rem;'></div>", unsafe_allow_html=True)
    if st.button("📜 Review Previous Tests (3 Mock Attempts)", key="btn_review_history_landing", use_container_width=True, type="secondary"):
        set_state("page", "history")
        st.rerun()


def render_quiz_screen(questions: List[Dict[str, Any]]):
    """Renders 1 question at a time styled after Screen 2 ('Today Class' diagnostic active card)."""
    current_idx = get_state("current_question_idx", 0)
    total_q = len(questions)
    q = questions[current_idx]
    qid = q["id"]

    render_header()

    # Screen 2 "Today Class" Style Header Card
    step_str = f"Step {current_idx + 1:02d}/{total_q:02d}"
    st.markdown(f"""
    <div class="active-class-hero">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
            <span class="active-class-tag">● Live Diagnostic Diagnostic Check</span>
            <span style="font-size:0.85rem; font-weight:800; color:#1B4332;">{step_str}</span>
        </div>
        <h2 style="margin:0 0 0.25rem 0; font-size:1.45rem; font-weight:800; color:#18181B;">
            A1 German Exam Readiness
        </h2>
        <div style="font-size:0.88rem; color:#2D6A4F; font-weight:600; margin-bottom:0.85rem;">
            Category: {q['category']} • Topic: {q['subtopic']}
        </div>
        <div style="display:flex; gap:0.5rem; align-items:center;">
            <span class="badge-pill badge-{q['category'].lower()}">{q['category']}</span>
            <span class="badge-subtopic">{q['subtopic']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Sleek Dark Progress Bar
    progress_val = (current_idx + 1) / total_q
    st.progress(progress_val)

    # Question Card Container
    st.markdown('<div class="ed-card" style="padding:1.65rem 1.75rem; margin-top:1rem;">', unsafe_allow_html=True)

    # Reading passage context snippet (if Q9-Q12)
    if q.get("context_snippet"):
        st.markdown(f"""
        <div class="reading-passage-box">
            <div class="reading-passage-header">📄 A1 Leseverstehen Kontext ({q['subtopic']})</div>
            <div class="reading-passage-content">{q['context_snippet']}</div>
        </div>
        """, unsafe_allow_html=True)

    # Question Prompt
    st.markdown(f"""
    <div style="font-size: 1.18rem; font-weight: 800; color: #18181B; line-height: 1.5; margin-bottom: 1.25rem;">
        {q['prompt']}
    </div>
    """, unsafe_allow_html=True)

    # Radio selection
    user_answers = get_state("user_answers", {})
    current_selection = user_answers.get(qid)

    selected_option = st.radio(
        label="Wählen Sie die richtige Antwort:",
        options=list(range(len(q["options"]))),
        format_func=lambda i: f"{chr(65 + i)})  {q['options'][i]}",
        index=current_selection if current_selection is not None else None,
        key=f"radio_q_{qid}",
        label_visibility="collapsed"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # Validation message if attempted to proceed without selecting
    val_err = get_state("validation_error")
    if val_err:
        st.warning(val_err)

    # Navigation Buttons (Previous / Next)
    col_prev, col_next = st.columns([1, 1.5])

    with col_prev:
        if current_idx > 0:
            if st.button("← Previous", use_container_width=True, type="secondary"):
                if selected_option is not None:
                    user_answers[qid] = selected_option
                    set_state("user_answers", user_answers)
                set_state("validation_error", None)
                set_state("current_question_idx", current_idx - 1)
                st.rerun()

    with col_next:
        is_last_question = (current_idx == total_q - 1)
        next_label = "Complete & View Results ✓" if is_last_question else "Next Question →"

        if st.button(next_label, use_container_width=True, type="primary"):
            if selected_option is None:
                set_state("validation_error", "⚠️ Bitte wählen Sie eine Antwort aus, um fortzufahren. (Please select an option to continue.)")
                st.rerun()
            else:
                user_answers[qid] = selected_option
                set_state("user_answers", user_answers)
                set_state("validation_error", None)

                if is_last_question:
                    set_state("page", "results")
                else:
                    set_state("current_question_idx", current_idx + 1)
                st.rerun()


def render_results_dashboard(result: Dict[str, Any], questions: List[Dict[str, Any]], is_historical: bool = False):
    """Renders the comprehensive diagnostic results dashboard styled like Screen 2 & Screen 3."""
    render_header()

    tier = result["tier"]
    tier_label = result["tier_label"]
    overall_pct = result["overall_percentage"]
    overall_score = result["overall_score"]
    total_q = result["total_questions"]
    verdict = result["verdict"]

    # 1. Top Hero Verdict Banner (Modeled after Screen 2 & 3 Hero Cards)
    banner_class = f"verdict-{tier.replace('_', '-')}"
    tier_icon = "🎉" if tier == "ready" else ("⚠️" if tier == "almost" else "🛑")

    st.markdown(f"""
    <div class="{banner_class}">
        <div style="display:inline-block; font-size: 0.76rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; background:rgba(255,255,255,0.7); backdrop-filter:blur(4px); padding:0.3rem 0.9rem; border-radius:9999px; margin-bottom: 0.75rem;">
            {tier_icon} Exam Readiness Verdict
        </div>
        <h2 style="margin: 0 0 0.5rem 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.02em;">
            {tier_label}
        </h2>
        <div style="font-size: 3rem; font-weight: 800; line-height: 1.1; margin: 0.5rem 0 0.75rem 0;">
            {overall_pct}%
            <span style="font-size: 1.15rem; font-weight: 600; opacity: 0.85;">({overall_score}/{total_q} Correct)</span>
        </div>
        <p style="margin: 0 auto; max-width: 580px; font-size: 1.05rem; line-height: 1.55; font-weight: 500;">
            {verdict}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 2. Skill Breakdown Section (3 Modern Pastel Pillar Cards)
    st.markdown("""
    <h3 style="font-size: 1.25rem; font-weight: 800; color: #18181B; margin: 1.5rem 0 0.85rem 0;">
        📊 Skill Breakdown by Diagnostic Pillar
    </h3>
    """, unsafe_allow_html=True)

    breakdown = result["skill_breakdown"]
    cols = st.columns(3)

    category_keys = ["Vocabulary", "Grammar", "Reading"]
    for i, cat in enumerate(category_keys):
        stats = breakdown[cat]
        pct = stats["percentage"]
        score = stats["score"]
        total = stats["total"]
        status = stats["status"]

        if pct >= 80:
            fill_class = "metric-bar-fill-emerald"
            badge_style = "background:#ECFDF5; color:#065F46; border:1px solid #A7F3D0;"
        elif pct >= 60:
            fill_class = "metric-bar-fill-amber"
            badge_style = "background:#FFFBEB; color:#92400E; border:1px solid #FCD34D;"
        else:
            fill_class = "metric-bar-fill-rose"
            badge_style = "background:#FEF2F2; color:#991B1B; border:1px solid #FCA5A5;"

        with cols[i]:
            st.markdown(f"""
            <div class="metric-container">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
                    <span style="font-size:0.92rem; font-weight:700; color:#18181B;">{cat}</span>
                    <span style="font-size:0.72rem; font-weight:700; padding:0.18rem 0.5rem; border-radius:9999px; {badge_style}">
                        {status}
                    </span>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:baseline;">
                    <span style="font-size:1.6rem; font-weight:800; color:#18181B;">{pct}%</span>
                    <span style="font-size:0.85rem; color:#71717A; font-weight:600;">{score} / {total}</span>
                </div>
                <div class="metric-bar-bg">
                    <div class="{fill_class}" style="width: {pct}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # 3. Personalized Practice Recommendations (Timeline Chips from Screen 2)
    st.markdown("""
    <h3 style="font-size: 1.25rem; font-weight: 800; color: #18181B; margin: 1.85rem 0 0.85rem 0;">
        🎯 Your Top Focus Areas & Next Steps
    </h3>
    """, unsafe_allow_html=True)

    for rec in result["recommendations"]:
        st.markdown(f"""
        <div class="recommendation-card">
            <span class="priority-tag">{rec['priority_label']} • {rec['category']}</span>
            <h4 style="margin: 0.25rem 0 0.35rem 0; font-size: 1.05rem; font-weight: 800; color: #18181B;">
                {rec['subtopic']}
            </h4>
            <p style="margin: 0 0 0.65rem 0; font-size: 0.95rem; color: #3F3F46; line-height: 1.55;">
                {rec['action']}
            </p>
            <div style="font-size: 0.85rem; font-weight: 600; color: #18181B; background: #FAF8F5; padding: 0.45rem 0.75rem; border-radius: 10px; border-left: 3px solid #18181B;">
                💡 {rec['tip']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 4. Review Section Header & Language Switcher
    st.markdown("<div style='margin-top: 1.85rem;'></div>", unsafe_allow_html=True)

    rev_col1, rev_col2 = st.columns([1.5, 1.5])
    with rev_col1:
        st.markdown("""
        <h3 style="font-size: 1.25rem; font-weight: 800; color: #18181B; margin: 0 0 0.25rem 0;">
            🔍 Question-by-Question Review
        </h3>
        <p style="font-size: 0.85rem; color: #71717A; margin: 0 0 0.75rem 0;">
            Review your answers, see correct solutions, and study grammatical rules.
        </p>
        """, unsafe_allow_html=True)

    with rev_col2:
        st.markdown("""
        <div style="font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #71717A; margin-bottom: 0.25rem;">
            🌐 Explanation Language:
        </div>
        """, unsafe_allow_html=True)
        explanation_lang = st.radio(
            "Explanation Language / Erklärungssprache",
            options=["🇬🇧 English", "🇩🇪 Deutsch"],
            index=0,
            horizontal=True,
            key="explanation_lang_choice",
            label_visibility="collapsed"
        )

    use_english = "English" in explanation_lang

    with st.expander("📝 Click to View / Collapse All 12 Questions", expanded=True):
        user_answers = get_state("user_answers", {})
        for q in questions:
            qid = q["id"]
            user_opt_idx = user_answers.get(qid)
            correct_opt_idx = q["correct_answer_index"]
            is_correct = (user_opt_idx == correct_opt_idx)

            card_class = "review-card-correct" if is_correct else "review-card-incorrect"
            status_symbol = "✓ Correct" if is_correct else "✗ Incorrect"
            status_color = "#059669" if is_correct else "#DC2626"

            st.markdown(f"""
            <div class="{card_class}">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.45rem;">
                    <span style="font-size:0.84rem; font-weight:700; color:#71717A;">
                        Question {qid} • {q['category']} ({q['subtopic']})
                    </span>
                    <span style="font-size:0.84rem; font-weight:800; color:{status_color};">
                        {status_symbol}
                    </span>
                </div>
                <div style="font-size:1.05rem; font-weight:800; color:#18181B; margin-bottom:0.35rem;">
                    {q['prompt']}
                </div>
            """, unsafe_allow_html=True)

            if use_english and q.get("prompt_en"):
                st.markdown(f"""
                <div style="font-size:0.88rem; font-style:italic; color:#71717A; margin-bottom:0.55rem;">
                    🇬🇧 <em>"{q['prompt_en']}"</em>
                </div>
                """, unsafe_allow_html=True)

            user_choice_text = q['options'][user_opt_idx] if user_opt_idx is not None else "No answer selected"
            correct_choice_text = q['options'][correct_opt_idx]

            if is_correct:
                st.markdown(f"""
                <div style="font-size:0.92rem; color:#065F46; margin-bottom:0.6rem;">
                    <strong>Your Answer:</strong> {user_choice_text}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="font-size:0.92rem; color:#991B1B; margin-bottom:0.25rem;">
                    <strong>Your Answer:</strong> {user_choice_text}
                </div>
                <div style="font-size:0.92rem; color:#065F46; margin-bottom:0.6rem;">
                    <strong>Correct Answer:</strong> {correct_choice_text}
                </div>
                """, unsafe_allow_html=True)

            if use_english:
                explanation_text = q.get("explanation_en", q.get("explanation"))
                lang_tag = "🇬🇧 Explanation (English)"
            else:
                explanation_text = q.get("explanation_de", q.get("explanation"))
                lang_tag = "🇩🇪 Erklärung (Deutsch)"

            st.markdown(f"""<div style="font-size:0.9rem; color:#18181B; background:rgba(255,255,255,0.9); padding:0.85rem 1rem; border-radius:14px; border:1px solid rgba(0,0,0,0.06); line-height:1.55;">
<div style="font-size:0.72rem; font-weight:800; text-transform:uppercase; letter-spacing:0.06em; color:#18181B; margin-bottom:0.3rem;">
{lang_tag}
</div>
{explanation_text}
</div>
</div>""", unsafe_allow_html=True)

            # Groq AI Deep Dive Explanation (Available when Groq API Key is configured)
            if is_groq_available():
                deep_dive_cache_key = f"groq_deep_dive_{qid}_{'en' if use_english else 'de'}"
                cached_deep_dive = get_state(deep_dive_cache_key)

                with st.expander(f"🤖 Groq AI Tutor: Deep Dive on Question {qid}", expanded=bool(cached_deep_dive)):
                    if not cached_deep_dive:
                        current_model = get_state("groq_selected_model", DEFAULT_MODEL)
                        if st.button(f"Generate Groq AI Explanation for Q{qid}", key=f"btn_groq_q_{qid}"):
                            with st.spinner(f"Groq AI Tutor is analyzing Question {qid}..."):
                                dd_text = explain_question_deep_dive(
                                    q, user_opt_idx, language="English" if use_english else "Deutsch", model=current_model
                                )
                                set_state(deep_dive_cache_key, dd_text)
                                st.rerun()
                    else:
                        st.markdown(f"""
                        <div class="ai-response-box">
                            {cached_deep_dive}
                        </div>
                        """, unsafe_allow_html=True)

    # 5. Bottom Action Controls
    if not is_historical:
        st.markdown("<div style='margin-top: 1.85rem;'></div>", unsafe_allow_html=True)
        col_retake, col_hist = st.columns([1, 1])

        with col_retake:
            if st.button("🔄 Retake Readiness Check", key="btn_retake_quiz", use_container_width=True, type="primary"):
                set_state("page", "landing")
                set_state("current_question_idx", 0)
                set_state("user_answers", {})
                set_state("validation_error", None)
                set_state("current_attempt_recorded", False)
                st.rerun()

        with col_hist:
            if st.button("📜 Review Past Tests", key="btn_view_history", use_container_width=True, type="secondary"):
                set_state("page", "history")
                st.rerun()


def render_history_screen(history_list: List[Dict[str, Any]], questions: List[Dict[str, Any]]):
    """Renders the Past Diagnostic Tests review screen styled like Screen 3 ('Last Lessons' list)."""
    render_header()

    st.markdown("""
    <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:0.5rem;">
        <h1 style="font-size: 2.1rem; font-weight: 800; color: #18181B; margin: 0; letter-spacing: -0.02em;">
            📜 Previous Tests & Review
        </h1>
    </div>
    <p style="font-size: 1.05rem; color: #52525B; margin-bottom: 1.5rem; line-height: 1.55;">
        Track your learning progression across previous diagnostic checks. 
        Select any past attempt below to inspect full score metrics, focus recommendations, and question-by-question mistakes.
    </p>
    """, unsafe_allow_html=True)

    if not history_list:
        st.info("No test history recorded yet. Complete a diagnostic check to see your progress here!")
        if st.button("🚀 Start Your First Check", type="primary"):
            set_state("page", "landing")
            st.rerun()
        return

    # 1. Historical Progress Summary Stats (Screen 3 Top Banner Style)
    first_attempt_res = calculate_readiness(history_list[-1]["answers"], questions)
    latest_attempt_res = calculate_readiness(history_list[0]["answers"], questions)
    growth = round(latest_attempt_res["overall_percentage"] - first_attempt_res["overall_percentage"], 1)
    growth_str = f"+{growth}%" if growth >= 0 else f"{growth}%"

    st.markdown(f"""
    <div class="history-hero">
        <div style="display:inline-block; font-size:0.75rem; font-weight:800; text-transform:uppercase; letter-spacing:0.08em; color:#9F1239; background:rgba(255,255,255,0.7); padding:0.25rem 0.75rem; border-radius:9999px; margin-bottom:0.75rem;">
            📈 Learning Progression Summary
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:0.85rem;">
            <div>
                <div style="font-size:0.78rem; color:#71717A; font-weight:600;">Saved Tests</div>
                <div style="font-size:1.65rem; font-weight:800; color:#18181B;">{len(history_list)}</div>
            </div>
            <div>
                <div style="font-size:0.78rem; color:#71717A; font-weight:600;">Baseline</div>
                <div style="font-size:1.65rem; font-weight:800; color:#71717A;">{first_attempt_res['overall_percentage']}%</div>
            </div>
            <div>
                <div style="font-size:0.78rem; color:#71717A; font-weight:600;">Latest Score</div>
                <div style="font-size:1.65rem; font-weight:800; color:#18181B;">{latest_attempt_res['overall_percentage']}%</div>
            </div>
            <div>
                <div style="font-size:0.78rem; color:#71717A; font-weight:600;">Growth</div>
                <div style="font-size:1.65rem; font-weight:800; color:#059669;">{growth_str}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 2. "Last Lessons" Stack Representation (Screen 3 List View)
    st.markdown("""
    <h3 style="font-size: 1.25rem; font-weight: 800; color: #18181B; margin: 1.5rem 0 0.75rem 0;">
        Last Lessons & Diagnostic Attempts:
    </h3>
    """, unsafe_allow_html=True)

    attempt_icons = ["🏆", "🧭", "⏱️"]
    for idx, att in enumerate(history_list):
        res = calculate_readiness(att["answers"], questions)
        icon = attempt_icons[idx % len(attempt_icons)]
        tier_badge_style = "background:#ECFDF5; color:#065F46;" if res["tier"] == "ready" else ("background:#FFFBEB; color:#92400E;" if res["tier"] == "almost" else "background:#FEF2F2; color:#991B1B;")

        st.markdown(f"""
        <div class="history-item-card">
            <div style="display:flex; align-items:center;">
                <div class="history-icon-badge">{icon}</div>
                <div>
                    <strong style="color:#18181B; font-size:0.98rem; display:block;">{att['title']}</strong>
                    <span style="font-size:0.8rem; color:#71717A;">📅 {att['date']} • ⏱️ {att.get('time_spent', '3m')}</span>
                </div>
            </div>
            <div style="text-align:right;">
                <span style="font-size:0.82rem; font-weight:800; padding:0.25rem 0.65rem; border-radius:9999px; {tier_badge_style}">
                    {res['overall_percentage']}% • {res['tier_label']}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 3. Attempt Selector Dropdown
    st.markdown("""
    <h3 style="font-size: 1.15rem; font-weight: 800; color: #18181B; margin: 1.35rem 0 0.5rem 0;">
        Select an Attempt to Review in Full Detail:
    </h3>
    """, unsafe_allow_html=True)

    attempt_options = {}
    for att in history_list:
        res = calculate_readiness(att["answers"], questions)
        tier_tag = "Ready (Green)" if res["tier"] == "ready" else ("Almost (Amber)" if res["tier"] == "almost" else "Not Ready (Red)")
        label = f"{att['title']} — {att['date']} [{res['overall_percentage']}% • {tier_tag}]"
        attempt_options[label] = att

    selected_label = st.selectbox(
        "Choose test attempt:",
        options=list(attempt_options.keys()),
        index=0,
        label_visibility="collapsed"
    )

    selected_attempt = attempt_options[selected_label]
    selected_result = calculate_readiness(selected_attempt["answers"], questions)

    # Display Attempt Note / Context Card
    st.markdown(f"""
    <div style="background:#FFFFFF; border:1px solid #E4E4E7; border-left:4px solid #18181B; border-radius:18px; padding:1.15rem 1.35rem; margin:1rem 0 1.5rem 0;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
            <strong style="color:#18181B; font-size:1rem;">{selected_attempt['title']}</strong>
            <span style="font-size:0.82rem; color:#71717A;">⏱️ Duration: {selected_attempt.get('time_spent', '3m')}</span>
        </div>
        <p style="margin:0; font-size:0.9rem; color:#52525B; line-height:1.5;">
            📝 <em>"{selected_attempt['notes']}"</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Temporarily set session user_answers to the selected attempt's answers for the review accordion
    old_answers = get_state("user_answers", {})
    set_state("user_answers", selected_attempt["answers"])

    # Render complete results dashboard for this selected attempt
    render_results_dashboard(selected_result, questions, is_historical=True)

    # Restore active answers
    set_state("user_answers", old_answers)

    # Return button
    st.markdown("<div style='margin-top:1.5rem;'></div>", unsafe_allow_html=True)
    if st.button("← Back to Active Diagnostic / Home", key="btn_back_home", use_container_width=True, type="secondary"):
        set_state("page", "landing")
        st.rerun()


# ==============================================================================
# Groq LLM View Components
# ==============================================================================

def render_groq_sidebar():
    """Renders the Groq AI Tutor settings and live Q&A assistant in the sidebar."""
    with st.sidebar:
        st.markdown("""
        <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.35rem;">
            <span style="font-size:1.4rem;">🤖</span>
            <h2 style="margin:0; font-size:1.25rem; font-weight:800; color:#18181B;">Groq AI Tutor</h2>
        </div>
        <p style="font-size:0.84rem; color:#71717A; margin-bottom:0.85rem; line-height:1.45;">
            High-speed AI coaching powered by Groq Llama 3 models.
        </p>
        """, unsafe_allow_html=True)

        is_active = is_groq_available()
        if is_active:
            st.success("🟢 Groq AI Connected", icon="✅")
        else:
            st.info("⚪ Groq AI Offline. Add an API key to enable AI coaching & study plans.", icon="🔑")

        # Model Selector
        model_options = [m[0] for m in AVAILABLE_MODELS]
        model_labels = {m[0]: m[1] for m in AVAILABLE_MODELS}
        selected_model = st.selectbox(
            "AI Model / Modell:",
            options=model_options,
            format_func=lambda x: model_labels.get(x, x),
            index=0,
            key="groq_selected_model"
        )

        # API Key input expander
        with st.expander("🔑 API Key Settings", expanded=not is_active):
            current_key = get_groq_api_key() or ""
            key_input = st.text_input(
                "Groq API Key:",
                value=current_key,
                type="password",
                help="Stored only in your current session. Get a free key at console.groq.com/keys",
                placeholder="gsk_..."
            )
            if key_input != current_key:
                set_state("groq_api_key", key_input)
                st.rerun()

            st.markdown("""
            <div style="font-size:0.78rem; color:#71717A; margin-top:0.4rem;">
                💡 <em>Never committed to git. Add to <code>.env</code>: <code>GROQ_API_KEY=gsk_...</code></em>
            </div>
            """, unsafe_allow_html=True)

        # Interactive Mini-Chat: Ask Groq German Coach
        st.markdown("<hr style='margin:1rem 0; border:none; border-top:1px solid #E4E4E7;' />", unsafe_allow_html=True)
        st.markdown("""
        <h4 style="margin:0 0 0.35rem 0; font-size:0.95rem; font-weight:800; color:#18181B;">
            💬 Ask Groq German Coach
        </h4>
        <div style="font-size:0.8rem; color:#71717A; margin-bottom:0.65rem;">
            Ask any grammar rule, word difference, or exam question.
        </div>
        """, unsafe_allow_html=True)

        chip_col1, chip_col2 = st.columns(2)
        quick_prompt = None
        with chip_col1:
            if st.button("der/die/das", key="chip_gender", use_container_width=True):
                quick_prompt = "What are the most reliable rules for der, die, and das in German A1?"
        with chip_col2:
            if st.button("am/um/im", key="chip_prep", use_container_width=True):
                quick_prompt = "Explain when to use am, um, and im in German with simple A1 examples."

        user_chat_input = st.text_input(
            "Your German Question:",
            value=quick_prompt if quick_prompt else "",
            placeholder="e.g. When do I use 'kein' vs 'nicht'?",
            key="groq_sidebar_question"
        )

        if st.button("Ask Groq 🚀", key="btn_ask_groq_sidebar", use_container_width=True, type="secondary"):
            if not is_groq_available():
                st.warning("⚠️ Please provide a Groq API Key above to chat with the AI coach.")
            elif not user_chat_input.strip():
                st.warning("Please type a question or click a topic chip.")
            else:
                with st.spinner("Groq AI is thinking..."):
                    answer = ask_groq_tutor(user_chat_input, model=selected_model)
                    set_state("groq_sidebar_last_answer", answer)

        last_ans = get_state("groq_sidebar_last_answer")
        if last_ans:
            st.markdown(f"""
            <div class="ai-response-box">
                {last_ans}
            </div>
            """, unsafe_allow_html=True)


def render_groq_ai_study_plan(result: Dict[str, Any], questions: List[Dict[str, Any]]):
    """Renders the Groq AI Study Coach & Personalized 7-Day Exam Strategy Card."""
    st.markdown("""
    <div class="ai-coach-card">
        <div class="ai-badge">✨ Groq AI Study Coach & Exam Strategy</div>
        <h3 style="margin: 0 0 0.45rem 0; font-size: 1.25rem; font-weight: 800; color: #18181B;">
            Personalized 7-Day Exam Blueprint
        </h3>
        <p style="margin: 0 0 1rem 0; font-size: 0.92rem; color: #52525B; line-height: 1.5;">
            Let Groq's high-speed AI diagnose your exact weaknesses, synthesize a tailored 7-day study routine,
            and provide memorable German grammar mnemonics for Goethe/ÖSD A1.
        </p>
    """, unsafe_allow_html=True)

    if not is_groq_available():
        st.markdown("""
        <div class="ai-key-box">
            🔑 <strong>Groq LLM is not connected yet:</strong><br/>
            Enter your free Groq API key in the sidebar or configure <code>GROQ_API_KEY</code> in your <code>.env</code> file to generate your custom AI study plan.
            <div style="margin-top:0.35rem;">
                👉 <a href="https://console.groq.com/keys" target="_blank" style="color:#B45309; font-weight:700;">Get a free API key at console.groq.com</a>
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)
        return

    study_plan_key = f"groq_study_plan_{result['overall_score']}_{result['tier']}"
    plan_content = get_state(study_plan_key)

    current_model = get_state("groq_selected_model", DEFAULT_MODEL)
    model_name_short = "Llama 3.3 70B" if "70b" in current_model else "Llama 3.1 8B"

    btn_label = "🔄 Regenerate AI Study Plan" if plan_content else f"🚀 Generate AI Study Plan ({model_name_short})"
    if st.button(btn_label, key="btn_gen_study_plan", type="primary", use_container_width=True):
        with st.spinner("🤖 Groq AI Coach is compiling your personalized 7-day study plan..."):
            user_answers = get_state("user_answers", {})
            plan_content = generate_study_plan(result, questions, user_answers, model=current_model)
            set_state(study_plan_key, plan_content)
            st.rerun()

    if plan_content:
        st.markdown(f"""
        <div class="ai-response-box">
            {plan_content}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

