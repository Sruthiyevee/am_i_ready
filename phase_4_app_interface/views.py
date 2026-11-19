"""
views.py - UI Renderers for "Am I Exam-Ready?"
Provides modular views:
- render_header(): German ribbon, authority badge, and title
- render_landing_screen(): Hero, exam fee value prop, 3-skill preview, CTA
- render_quiz_screen(): 1-question view, progress bar, category/subtopic badges, reading snippets, navigation
- render_results_dashboard(): Verdict hero card, category skill meters, focus areas, collapsible review, retake CTA
"""

import streamlit as st
from typing import Dict, Any, List


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


def render_header():
    """Renders the top branding, German flag accent bar, and authority pill."""
    st.markdown("""
    <div class="de-accent-bar">
        <div class="bar-black"></div>
        <div class="bar-red"></div>
        <div class="bar-gold"></div>
    </div>
    <div class="authority-pill">
        <span>🇩🇪</span> Goethe-Zertifikat A1 (Start Deutsch 1) & ÖSD Zertifikat A1 Diagnostic
    </div>
    """, unsafe_allow_html=True)


def render_landing_screen():
    """Renders the Landing Screen with clear value prop and single primary CTA."""
    render_header()

    st.markdown("""
    <h1 style="font-size: 2.25rem; font-weight: 800; color: #0F172A; line-height: 1.2; margin-bottom: 0.75rem;">
        Am I ready for my A1 German exam?
    </h1>
    <p style="font-size: 1.1rem; color: #475569; line-height: 1.6; margin-bottom: 1.75rem;">
        Exam registration fees range between <strong>€100 and €180</strong>. 
        Take this official-format 12-question diagnostic across Vocabulary, Grammar, and Reading 
        (~3 minutes) to objectively check if you are ready to book and pass on your first attempt.
    </p>
    """, unsafe_allow_html=True)

    # 3-Skill Preview Cards
    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
        <div class="ed-card" style="margin-bottom:0; padding:1.25rem;">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;">
                <span class="badge-pill badge-vocabulary">📚 4 Questions</span>
            </div>
            <h4 style="margin:0 0 0.35rem 0; font-size:1.05rem; font-weight:700; color:#0F172A;">Vocabulary</h4>
            <p style="margin:0; font-size:0.85rem; color:#64748B; line-height:1.45;">
                Everyday shopping, directions in town, clock times, family & professions.
            </p>
        </div>
        <div class="ed-card" style="margin-bottom:0; padding:1.25rem;">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;">
                <span class="badge-pill badge-grammar">🧩 4 Questions</span>
            </div>
            <h4 style="margin:0 0 0.35rem 0; font-size:1.05rem; font-weight:700; color:#0F172A;">Grammar</h4>
            <p style="margin:0; font-size:0.85rem; color:#64748B; line-height:1.45;">
                Articles (der/die/das), accusative case, verb endings, prepositions & negation.
            </p>
        </div>
        <div class="ed-card" style="margin-bottom:0; padding:1.25rem;">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;">
                <span class="badge-pill badge-reading">📖 4 Questions</span>
            </div>
            <h4 style="margin:0 0 0.35rem 0; font-size:1.05rem; font-weight:700; color:#0F172A;">Reading</h4>
            <p style="margin:0; font-size:0.85rem; color:#64748B; line-height:1.45;">
                Informal emails, doctor clinic notices, Deutsche Bahn train timetables & ads.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Trust Features
    st.markdown("""
    <div style="display:flex; flex-wrap:wrap; gap:1.25rem; font-size:0.88rem; color:#475569; margin-bottom:1.75rem;">
        <span>✓ <strong>100% Free</strong> & Client-Side</span>
        <span>✓ <strong>Goethe/ÖSD 60% Benchmark</strong> + Safety Buffer</span>
        <span>✓ <strong>Instant</strong> Personalized Study Plan</span>
    </div>
    """, unsafe_allow_html=True)

    # Primary CTA
    if st.button("🚀 Start Readiness Check (3 mins)", use_container_width=True, type="primary"):
        set_state("page", "quiz")
        set_state("current_question_idx", 0)
        set_state("user_answers", {})
        set_state("validation_error", None)
        st.rerun()


def render_quiz_screen(questions: List[Dict[str, Any]]):
    """Renders 1 question at a time with progress bar and navigation controls."""
    current_idx = get_state("current_question_idx", 0)
    total_q = len(questions)
    q = questions[current_idx]
    qid = q["id"]

    render_header()

    # Progress bar and Counter
    progress_val = (current_idx + 1) / total_q
    st.progress(progress_val)

    st.markdown(f"""
    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.5rem; margin-bottom:1.25rem;">
        <span style="font-size:0.88rem; font-weight:700; color:#475569; text-transform:uppercase; letter-spacing:0.05em;">
            Question {current_idx + 1} of {total_q}
        </span>
        <div style="display:flex; gap:0.5rem; align-items:center;">
            <span class="badge-pill badge-{q['category'].lower()}">{q['category']}</span>
            <span class="badge-subtopic">{q['subtopic']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Question Card Container
    st.markdown('<div class="ed-card" style="padding:1.5rem 1.75rem;">', unsafe_allow_html=True)

    # If Reading question, display authentic German context box
    if q.get("context_snippet"):
        st.markdown(f"""
        <div class="reading-passage-box">
            <div class="reading-passage-header">📄 A1 Leseverstehen Kontext ({q['subtopic']})</div>
            <div class="reading-passage-content">{q['context_snippet']}</div>
        </div>
        """, unsafe_allow_html=True)

    # Question Prompt
    st.markdown(f"""
    <div style="font-size: 1.15rem; font-weight: 700; color: #0F172A; line-height: 1.5; margin-bottom: 1.25rem;">
        {q['prompt']}
    </div>
    """, unsafe_allow_html=True)

    # Radio selection
    user_answers = get_state("user_answers", {})
    current_selection = user_answers.get(qid)
    
    # Render custom radio options
    selected_option = st.radio(
        label="Wählen Sie die richtige Antwort:",
        options=list(range(len(q["options"]))),
        format_func=lambda i: f"{chr(65 + i)})  {q['options'][i]}",
        index=current_selection if current_selection is not None else None,
        key=f"radio_q_{qid}",
        label_visibility="collapsed"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # Validation message if user attempted to proceed without selecting
    val_err = get_state("validation_error")
    if val_err:
        st.warning(val_err)

    # Navigation Buttons (Previous / Next)
    col_prev, col_next = st.columns([1, 1.5])

    with col_prev:
        if current_idx > 0:
            if st.button("← Previous", use_container_width=True):
                # Save selection if made
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


def render_results_dashboard(result: Dict[str, Any], questions: List[Dict[str, Any]]):
    """Renders the comprehensive diagnostic results dashboard."""
    render_header()

    tier = result["tier"]
    tier_label = result["tier_label"]
    overall_pct = result["overall_percentage"]
    overall_score = result["overall_score"]
    total_q = result["total_questions"]
    verdict = result["verdict"]

    # 1. Top Hero Verdict Banner
    banner_class = f"verdict-{tier.replace('_', '-')}"
    tier_icon = "🎉" if tier == "ready" else ("⚠️" if tier == "almost" else "🛑")

    st.markdown(f"""
    <div class="{banner_class}">
        <div style="font-size: 2.25rem; margin-bottom: 0.25rem;">{tier_icon}</div>
        <div style="font-size: 0.85rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.85; margin-bottom: 0.4rem;">
            Exam Readiness Verdict
        </div>
        <h2 style="margin: 0 0 0.5rem 0; font-size: 2rem; font-weight: 800;">
            {tier_label}
        </h2>
        <div style="font-size: 2.75rem; font-weight: 800; line-height: 1; margin: 0.75rem 0;">
            {overall_pct}%
            <span style="font-size: 1.15rem; font-weight: 600; opacity: 0.85;">({overall_score}/{total_q} Correct)</span>
        </div>
        <p style="margin: 0 auto; max-width: 620px; font-size: 1.05rem; line-height: 1.55; font-weight: 500;">
            {verdict}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 2. Skill Breakdown Section
    st.markdown("""
    <h3 style="font-size: 1.25rem; font-weight: 800; color: #0F172A; margin: 1.75rem 0 1rem 0;">
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
                    <span style="font-size:0.9rem; font-weight:700; color:#1E293B;">{cat}</span>
                    <span style="font-size:0.75rem; font-weight:700; padding:0.15rem 0.5rem; border-radius:9999px; {badge_style}">
                        {status}
                    </span>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:baseline;">
                    <span style="font-size:1.5rem; font-weight:800; color:#0F172A;">{pct}%</span>
                    <span style="font-size:0.85rem; color:#64748B; font-weight:600;">{score} / {total}</span>
                </div>
                <div class="metric-bar-bg">
                    <div class="{fill_class}" style="width: {pct}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # 3. Personalized Practice Recommendations
    st.markdown("""
    <h3 style="font-size: 1.25rem; font-weight: 800; color: #0F172A; margin: 2rem 0 1rem 0;">
        🎯 Your Top Focus Areas & Next Steps
    </h3>
    """, unsafe_allow_html=True)

    for rec in result["recommendations"]:
        st.markdown(f"""
        <div class="recommendation-card">
            <span class="priority-tag">{rec['priority_label']} • {rec['category']}</span>
            <h4 style="margin: 0.25rem 0 0.5rem 0; font-size: 1.05rem; font-weight: 700; color: #0F172A;">
                {rec['subtopic']}
            </h4>
            <p style="margin: 0 0 0.65rem 0; font-size: 0.95rem; color: #334155; line-height: 1.55;">
                {rec['action']}
            </p>
            <div style="font-size: 0.85rem; font-weight: 600; color: #4F46E5; background: #F8FAFC; padding: 0.45rem 0.75rem; border-radius: 6px; border-left: 3px solid #4F46E5;">
                💡 {rec['tip']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 4. Collapsible Question-by-Question Review
    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
    with st.expander("🔍 Review All 12 Questions, Answers & Explanations", expanded=False):
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
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
                    <span style="font-size:0.85rem; font-weight:700; color:#475569;">
                        Question {qid} • {q['category']} ({q['subtopic']})
                    </span>
                    <span style="font-size:0.85rem; font-weight:800; color:{status_color};">
                        {status_symbol}
                    </span>
                </div>
                <div style="font-size:1rem; font-weight:600; color:#0F172A; margin-bottom:0.6rem;">
                    {q['prompt']}
                </div>
            """, unsafe_allow_html=True)

            user_choice_text = q['options'][user_opt_idx] if user_opt_idx is not None else "No answer selected"
            correct_choice_text = q['options'][correct_opt_idx]

            if is_correct:
                st.markdown(f"""
                <div style="font-size:0.9rem; color:#047857; margin-bottom:0.5rem;">
                    <strong>Your Answer:</strong> {user_choice_text}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="font-size:0.9rem; color:#B91C1C; margin-bottom:0.25rem;">
                    <strong>Your Answer:</strong> {user_choice_text}
                </div>
                <div style="font-size:0.9rem; color:#047857; margin-bottom:0.5rem;">
                    <strong>Correct Answer:</strong> {correct_choice_text}
                </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
                <div style="font-size:0.88rem; color:#334155; background:rgba(255,255,255,0.7); padding:0.65rem 0.85rem; border-radius:6px; border:1px solid rgba(0,0,0,0.06); line-height:1.45;">
                    📖 <strong>Explanation:</strong> {q['explanation']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # 5. Bottom Action Button (Retake Check)
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    if st.button("🔄 Retake Readiness Check", use_container_width=True):
        set_state("page", "landing")
        set_state("current_question_idx", 0)
        set_state("user_answers", {})
        set_state("validation_error", None)
        st.rerun()
