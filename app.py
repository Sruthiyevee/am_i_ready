"""
app.py - Main Entrypoint for "Am I Exam-Ready?"
A1 German Readiness Check for Goethe-Zertifikat A1 & ÖSD Zertifikat A1.
Client-side Streamlit web application.
"""

import streamlit as st
import sys
import os

# Add root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from data.questions import QUESTIONS
from data.history import get_mock_history
from utils.readiness import calculate_readiness
from src.styles import CUSTOM_CSS
from phase_4_app_interface.views import (
    render_landing_screen,
    render_quiz_screen,
    render_results_dashboard,
    render_history_screen,
    render_groq_sidebar,
    render_groq_ai_study_plan,
)

# 1. Page Configuration
st.set_page_config(
    page_title="Am I Exam-Ready? (A1 German Readiness Check)",
    page_icon="🇩🇪",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Inject Modern Ed-Tech CSS Design System
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# 3. Session State Initialization
if "page" not in st.session_state:
    st.session_state.page = "landing"

if "current_question_idx" not in st.session_state:
    st.session_state.current_question_idx = 0

if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

if "validation_error" not in st.session_state:
    st.session_state.validation_error = None

if "history" not in st.session_state:
    st.session_state.history = list(get_mock_history())


# 4. View Router
def main():
    render_groq_sidebar()

    if st.session_state.page == "landing":
        render_landing_screen()

    elif st.session_state.page == "quiz":
        render_quiz_screen(QUESTIONS)

    elif st.session_state.page == "results":
        if (
            not st.session_state.get("current_attempt_recorded", False)
            and len(st.session_state.user_answers) == len(QUESTIONS)
        ):
            from datetime import datetime
            attempt_num = len(st.session_state.history) + 1
            new_attempt = {
                "id": f"attempt-{attempt_num}",
                "title": f"Attempt {attempt_num}: Live Test Check",
                "date": datetime.now().strftime("%d %b %Y, %H:%M"),
                "time_spent": "Live Session",
                "answers": dict(st.session_state.user_answers),
                "notes": "Completed during your current live diagnostic session.",
            }
            st.session_state.history.insert(0, new_attempt)
            st.session_state.current_attempt_recorded = True

        readiness_result = calculate_readiness(st.session_state.user_answers, QUESTIONS)
        render_results_dashboard(readiness_result, QUESTIONS)
        render_groq_ai_study_plan(readiness_result, QUESTIONS)

    elif st.session_state.page == "history":
        render_history_screen(st.session_state.history, QUESTIONS)

    else:
        st.session_state.page = "landing"
        st.rerun()


if __name__ == "__main__":
    main()
