"""
test_phase4.py - Unit test suite for Phase 4 UI Views and State Transitions
Tests syntax, component renderers, state machine logic, and review drawer.
"""

import sys
import ast
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "phase_2_question_bank"))
sys.path.insert(0, str(BASE_DIR / "phase_3_readiness_engine"))
sys.path.insert(0, str(BASE_DIR / "phase_4_app_interface"))

from questions import QUESTIONS
from readiness import calculate_readiness
import views


class MockSessionState(dict):
    """Simulates Streamlit's st.session_state supporting both attribute and dict access."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            return None

    def __setattr__(self, name, value):
        self[name] = value


class TestPhase4SyntaxAndStructure:
    """Validate AST syntax and function exports in views.py and app.py."""

    def test_views_syntax(self):
        views_file = BASE_DIR / "phase_4_app_interface" / "views.py"
        source = views_file.read_text(encoding="utf-8")
        parsed = ast.parse(source)
        assert isinstance(parsed, ast.Module)

    def test_app_syntax(self):
        app_file = BASE_DIR / "app.py"
        source = app_file.read_text(encoding="utf-8")
        parsed = ast.parse(source)
        assert isinstance(parsed, ast.Module)

    def test_exported_view_functions(self):
        assert hasattr(views, "render_header")
        assert hasattr(views, "render_landing_screen")
        assert hasattr(views, "render_quiz_screen")
        assert hasattr(views, "render_results_dashboard")


class TestLandingScreenLogic:
    """Test landing screen actions and state setup."""

    @patch("streamlit.markdown")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_landing_screen_renders_and_cta_starts_quiz(self, mock_rerun, mock_button, mock_markdown):
        mock_button.return_value = True  # User clicks "Start Readiness Check"

        fake_session = MockSessionState({"page": "landing"})
        with patch.object(views.st, "session_state", fake_session):
            views.render_landing_screen()

            # Button was evaluated and clicked
            assert mock_button.called
            assert fake_session.page == "quiz"
            assert fake_session.current_question_idx == 0
            assert fake_session.user_answers == {}
            assert mock_rerun.called


class TestQuizScreenNavigationAndValidation:
    """Test 1-question display, previous/next buttons, and validation blocking."""

    @patch("streamlit.markdown")
    @patch("streamlit.progress")
    @patch("streamlit.radio")
    @patch("streamlit.button")
    @patch("streamlit.warning")
    @patch("streamlit.rerun")
    def test_prevents_advancing_without_option_selected(
        self, mock_rerun, mock_warning, mock_button, mock_radio, mock_progress, mock_markdown
    ):
        """User clicks Next without picking any radio option: must trigger validation warning."""
        mock_radio.return_value = None  # No option selected
        mock_button.return_value = True  # User clicks Next

        fake_session = MockSessionState({
            "current_question_idx": 0,
            "user_answers": {},
            "validation_error": None
        })

        with patch.object(views.st, "session_state", fake_session):
            views.render_quiz_screen(QUESTIONS)

            # Did not advance question index
            assert fake_session.current_question_idx == 0
            # Validation error was set
            assert fake_session.validation_error is not None
            assert "Bitte wählen Sie eine Antwort aus" in fake_session.validation_error
            assert mock_rerun.called

    @patch("streamlit.markdown")
    @patch("streamlit.progress")
    @patch("streamlit.radio")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_advances_when_option_selected(
        self, mock_rerun, mock_button, mock_radio, mock_progress, mock_markdown
    ):
        """User selects an option and clicks Next: saves answer and increments question index."""
        mock_radio.return_value = 1  # User selected option B (index 1)
        mock_button.return_value = True

        fake_session = MockSessionState({
            "current_question_idx": 3,
            "user_answers": {},
            "validation_error": "Old error"
        })

        with patch.object(views.st, "session_state", fake_session):
            views.render_quiz_screen(QUESTIONS)

            q4_id = QUESTIONS[3]["id"]
            assert fake_session.user_answers[q4_id] == 1
            assert fake_session.current_question_idx == 4
            assert fake_session.validation_error is None
            assert mock_rerun.called

    @patch("streamlit.markdown")
    @patch("streamlit.progress")
    @patch("streamlit.radio")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_completing_last_question_transitions_to_results(
        self, mock_rerun, mock_button, mock_radio, mock_progress, mock_markdown
    ):
        """On question 12 (idx 11), clicking Complete transitions page to 'results'."""
        mock_radio.return_value = 2  # Option C
        mock_button.return_value = True

        fake_session = MockSessionState({
            "page": "quiz",
            "current_question_idx": 11,
            "user_answers": {},
            "validation_error": None
        })

        with patch.object(views.st, "session_state", fake_session):
            views.render_quiz_screen(QUESTIONS)

            q12_id = QUESTIONS[11]["id"]
            assert fake_session.user_answers[q12_id] == 2
            assert fake_session.page == "results"
            assert mock_rerun.called


class TestResultsDashboardView:
    """Test rendering of verdict, metric bars, recommendations, and retake action."""

    @patch("streamlit.markdown")
    @patch("streamlit.columns")
    @patch("streamlit.expander")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_results_dashboard_renders_and_retake_resets_state(
        self, mock_rerun, mock_button, mock_expander, mock_columns, mock_markdown
    ):
        mock_cols = [MagicMock(), MagicMock(), MagicMock()]
        mock_columns.return_value = mock_cols

        mock_button.return_value = True  # User clicks "Retake Readiness Check"

        answers = {q["id"]: q["correct_answer_index"] for q in QUESTIONS}
        readiness_result = calculate_readiness(answers, QUESTIONS)

        fake_session = MockSessionState({
            "page": "results",
            "current_question_idx": 11,
            "user_answers": answers,
            "validation_error": None
        })

        with patch.object(views.st, "session_state", fake_session):
            views.render_results_dashboard(readiness_result, QUESTIONS)

            # Check that reset occurred
            assert fake_session.page == "landing"
            assert fake_session.current_question_idx == 0
            assert fake_session.user_answers == {}
            assert mock_rerun.called
