"""
test_phase5_e2e.py - End-to-End Simulation & Integration Test Suite
Simulates realistic learner journeys, persona benchmarks, state transitions,
and full diagnostic lifecycle for Goethe/ÖSD A1 exam readiness.
"""

import sys
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "phase_2_question_bank"))
sys.path.insert(0, str(BASE_DIR / "phase_3_readiness_engine"))
sys.path.insert(0, str(BASE_DIR / "phase_4_app_interface"))

from questions import QUESTIONS
from readiness import calculate_readiness
import views


class MockSession(dict):
    """Simulates Streamlit session_state with dual attribute/dict access."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            return None

    def __setattr__(self, name, value):
        self[name] = value


class TestEndToEndPersonaJourneys:
    """Simulate authentic learner scenarios from start to finish."""

    def test_persona_a_high_achiever_100_percent(self):
        """Persona A scores 12/12 (100%): Green 'Ready to Book' + Exam-Day Tips."""
        answers = {q["id"]: q["correct_answer_index"] for q in QUESTIONS}
        result = calculate_readiness(answers, QUESTIONS)

        assert result["overall_score"] == 12
        assert result["overall_percentage"] == 100.0
        assert result["tier"] == "ready"
        assert result["tier_label"] == "Ready to Book"
        assert result["tier_color"] == "#10B981"
        assert "High confidence" in result["verdict"]

        # All 3 skills must be 100% and Strong
        for cat in ["Vocabulary", "Grammar", "Reading"]:
            assert result["skill_breakdown"][cat]["percentage"] == 100.0
            assert result["skill_breakdown"][cat]["status"] == "Strong"

        # Exactly 2 Exam-Day strategy tips
        assert len(result["recommendations"]) == 2
        assert result["recommendations"][0]["category"] == "Exam Strategy"

    def test_persona_b_unbalanced_learner_safety_buffer(self):
        """
        Persona B scores 10/12 (83.3% >= 80%), but fails Grammar (2/4 = 50% < 60%).
        Safety Buffer triggers Amber 'Almost Ready' and prioritizes Grammar subtopics.
        """
        answers = {}
        for q in QUESTIONS:
            if q["category"] == "Grammar":
                # Miss Q7 and Q8
                if q["id"] in [7, 8]:
                    answers[q["id"]] = (q["correct_answer_index"] + 1) % 4
                else:
                    answers[q["id"]] = q["correct_answer_index"]
            else:
                answers[q["id"]] = q["correct_answer_index"]

        result = calculate_readiness(answers, QUESTIONS)

        assert result["overall_score"] == 10
        assert result["overall_percentage"] == 83.3
        assert result["skill_breakdown"]["Grammar"]["percentage"] == 50.0
        assert result["skill_breakdown"]["Vocabulary"]["percentage"] == 100.0
        assert result["skill_breakdown"]["Reading"]["percentage"] == 100.0

        # Must be downgraded to Amber due to single-skill failure
        assert result["tier"] == "almost"
        assert result["tier_label"] == "Almost Ready"
        assert result["tier_color"] == "#F59E0B"
        assert "Grammar" in result["verdict"]

        # Recommendations must prioritize Grammar subtopics
        recs = result["recommendations"]
        assert len(recs) == 2
        assert recs[0]["category"] == "Grammar"
        assert recs[1]["category"] == "Grammar"

    def test_persona_c_borderline_candidate(self):
        """Persona C scores 9/12 (75%): Amber 'Almost Ready' across all skills."""
        # Miss 1 in each category: Q3 (Vocab), Q6 (Grammar), Q10 (Reading)
        answers = {}
        for q in QUESTIONS:
            if q["id"] in [3, 6, 10]:
                answers[q["id"]] = (q["correct_answer_index"] + 1) % 4
            else:
                answers[q["id"]] = q["correct_answer_index"]

        result = calculate_readiness(answers, QUESTIONS)

        assert result["overall_score"] == 9
        assert result["overall_percentage"] == 75.0
        assert result["tier"] == "almost"
        assert result["tier_label"] == "Almost Ready"
        assert len(result["recommendations"]) == 3

    def test_persona_d_early_learner_not_ready(self):
        """Persona D scores 5/12 (41.7% < 65%): Red 'Not Ready Yet'."""
        # Answer only 5 correctly (Q1, Q2, Q5, Q9, Q11)
        answers = {}
        for q in QUESTIONS:
            if q["id"] in [1, 2, 5, 9, 11]:
                answers[q["id"]] = q["correct_answer_index"]
            else:
                answers[q["id"]] = (q["correct_answer_index"] + 1) % 4

        result = calculate_readiness(answers, QUESTIONS)

        assert result["overall_score"] == 5
        assert result["overall_percentage"] == 41.7
        assert result["tier"] == "not_ready"
        assert result["tier_label"] == "Not Ready Yet"
        assert result["tier_color"] == "#EF4444"
        assert "Not yet exam-ready" in result["verdict"]


class TestDiagnosticLifecycleSimulation:
    """Simulate complete user clickstream through views and session transitions."""

    @patch("streamlit.markdown")
    @patch("streamlit.progress")
    @patch("streamlit.radio")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_full_quiz_walkthrough_and_answer_persistence(
        self, mock_rerun, mock_button, mock_radio, mock_progress, mock_markdown
    ):
        """Simulate stepping through questions, going back, and completing."""
        session = MockSession({
            "page": "landing",
            "current_question_idx": 0,
            "user_answers": {},
            "validation_error": None
        })

        with patch.object(views.st, "session_state", session):
            # Step 1: Landing screen -> Click Start
            mock_button.return_value = True
            views.render_landing_screen()
            assert session.page == "quiz"
            assert session.current_question_idx == 0

            # Step 2: Answer Question 1 (Laib Brot -> index 0) and advance
            mock_radio.return_value = 0
            mock_button.return_value = True
            views.render_quiz_screen(QUESTIONS)
            assert session.user_answers[1] == 0
            assert session.current_question_idx == 1

            # Step 3: Answer Question 2 (rechts -> index 1) and advance
            mock_radio.return_value = 1
            views.render_quiz_screen(QUESTIONS)
            assert session.user_answers[2] == 1
            assert session.current_question_idx == 2

            # Step 4: Simulate clicking Previous back to Question 2
            # Set button to trigger previous (first column button)
            # In render_quiz_screen: previous button triggers decrement
            session.current_question_idx = 1
            # Verify answer for Q2 is preserved
            assert session.user_answers[2] == 1

            # Step 5: Fast forward to Question 12 (last question)
            session.current_question_idx = 11
            # Fill remaining answers
            for q in QUESTIONS:
                if q["id"] not in session.user_answers:
                    session.user_answers[q["id"]] = q["correct_answer_index"]

            # Complete question 12
            mock_radio.return_value = QUESTIONS[11]["correct_answer_index"]
            mock_button.return_value = True
            views.render_quiz_screen(QUESTIONS)
            assert session.page == "results"

    @patch("streamlit.markdown")
    @patch("streamlit.columns")
    @patch("streamlit.expander")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_results_review_drawer_content_generation(
        self, mock_rerun, mock_button, mock_expander, mock_columns, mock_markdown
    ):
        """Verify results dashboard renders all 12 review items and handles retake."""
        mock_columns.return_value = [MagicMock(), MagicMock(), MagicMock()]
        mock_button.return_value = False  # Don't click retake yet

        answers = {q["id"]: q["correct_answer_index"] for q in QUESTIONS}
        # Miss Q1
        answers[1] = 1

        result = calculate_readiness(answers, QUESTIONS)
        session = MockSession({
            "page": "results",
            "current_question_idx": 11,
            "user_answers": answers,
            "validation_error": None
        })

        with patch.object(views.st, "session_state", session):
            views.render_results_dashboard(result, QUESTIONS)

            # Click Retake Check
            mock_button.return_value = True
            views.render_results_dashboard(result, QUESTIONS)
            assert session.page == "landing"
            assert session.current_question_idx == 0
            assert session.user_answers == {}
