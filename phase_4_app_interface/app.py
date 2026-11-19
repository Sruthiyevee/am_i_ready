"""
app.py - Standalone Runner for Phase 4 App Interface
"""

import streamlit as st
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "phase_1_setup"))
sys.path.insert(0, os.path.join(BASE_DIR, "phase_2_question_bank"))
sys.path.insert(0, os.path.join(BASE_DIR, "phase_3_readiness_engine"))
sys.path.insert(0, os.path.dirname(__file__))

from questions import QUESTIONS
from readiness import calculate_readiness
from styles import CUSTOM_CSS
from views import (
    render_landing_screen,
    render_quiz_screen,
    render_results_dashboard,
)

st.set_page_config(
    page_title="Am I Exam-Ready? (A1 German Readiness Check)",
    page_icon="🇩🇪",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "landing"

if "current_question_idx" not in st.session_state:
    st.session_state.current_question_idx = 0

if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

if "validation_error" not in st.session_state:
    st.session_state.validation_error = None


def main():
    if st.session_state.page == "landing":
        render_landing_screen()

    elif st.session_state.page == "quiz":
        render_quiz_screen(QUESTIONS)

    elif st.session_state.page == "results":
        readiness_result = calculate_readiness(st.session_state.user_answers, QUESTIONS)
        render_results_dashboard(readiness_result, QUESTIONS)

    else:
        st.session_state.page = "landing"
        st.rerun()


if __name__ == "__main__":
    main()
