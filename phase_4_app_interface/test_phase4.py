"""
test_phase4.py - Unit test suite for Phase 4 UI Views and State Transitions
Tests syntax, component renderers, state machine logic, English/German explanation toggling,
review drawer, and past test history review.
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
from history import get_mock_history
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


def mock_columns_factory(spec):
    count = len(spec) if isinstance(spec, list) else spec
    return [MagicMock() for _ in range(count)]


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
        assert hasattr(views, "render_history_screen")


class TestLandingScreenLogic:
    """Test landing screen actions and state setup."""

    @patch("streamlit.markdown")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_landing_screen_renders_and_cta_starts_quiz(self, mock_rerun, mock_button, mock_markdown):
        mock_button.side_effect = [True, False]  # Click "Start Readiness Check"

        fake_session = MockSessionState({"page": "landing"})
        with patch.object(views.st, "session_state", fake_session):
            views.render_landing_screen()

            assert fake_session.page == "quiz"
            assert fake_session.current_question_idx == 0
            assert fake_session.user_answers == {}
            assert mock_rerun.called

    @patch("streamlit.markdown")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_landing_screen_can_navigate_to_history(self, mock_rerun, mock_button, mock_markdown):
        mock_button.side_effect = [False, True]  # Click "Review Previous Tests"

        fake_session = MockSessionState({"page": "landing"})
        with patch.object(views.st, "session_state", fake_session):
            views.render_landing_screen()

            assert fake_session.page == "history"
            assert mock_rerun.called
            # Verify the review button was explicitly configured with type="secondary"
            review_btn_call = mock_button.call_args_list[1]
            assert review_btn_call.kwargs.get("type") == "secondary"


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
        mock_radio.return_value = None
        mock_button.return_value = True

        fake_session = MockSessionState({
            "current_question_idx": 0,
            "user_answers": {},
            "validation_error": None
        })

        with patch.object(views.st, "session_state", fake_session):
            views.render_quiz_screen(QUESTIONS)

            assert fake_session.current_question_idx == 0
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
        mock_radio.return_value = 1
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
        mock_radio.return_value = 2
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
    """Test rendering of verdict, metric bars, recommendations, language toggle, and retake action."""

    @patch("streamlit.markdown")
    @patch("streamlit.columns")
    @patch("streamlit.expander")
    @patch("streamlit.radio")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_results_dashboard_renders_and_retake_resets_state(
        self, mock_rerun, mock_button, mock_radio, mock_expander, mock_columns, mock_markdown
    ):
        mock_columns.side_effect = mock_columns_factory
        mock_radio.return_value = "🇬🇧 English"
        mock_button.side_effect = [True, False]  # Click Retake Check

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

            assert fake_session.page == "landing"
            assert fake_session.current_question_idx == 0
            assert fake_session.user_answers == {}
            assert mock_rerun.called

    @patch("streamlit.markdown")
    @patch("streamlit.columns")
    @patch("streamlit.expander")
    @patch("streamlit.radio")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_results_dashboard_supports_english_and_german_explanations(
        self, mock_rerun, mock_button, mock_radio, mock_expander, mock_columns, mock_markdown
    ):
        mock_columns.side_effect = mock_columns_factory
        mock_button.return_value = False

        answers = {q["id"]: q["correct_answer_index"] for q in QUESTIONS}
        readiness_result = calculate_readiness(answers, QUESTIONS)

        fake_session = MockSessionState({
            "page": "results",
            "current_question_idx": 11,
            "user_answers": answers,
            "validation_error": None
        })

        # Test English toggle
        mock_radio.return_value = "🇬🇧 English"
        with patch.object(views.st, "session_state", fake_session):
            views.render_results_dashboard(readiness_result, QUESTIONS)
            markdown_calls = [call[0][0] for call in mock_markdown.call_args_list if len(call[0]) > 0]
            assert any("Explanation (English)" in str(m) for m in markdown_calls)

        mock_markdown.reset_mock()

        # Test German toggle
        mock_radio.return_value = "🇩🇪 Deutsch"
        with patch.object(views.st, "session_state", fake_session):
            views.render_results_dashboard(readiness_result, QUESTIONS)
            markdown_calls = [call[0][0] for call in mock_markdown.call_args_list if len(call[0]) > 0]
            assert any("Erklärung (Deutsch)" in str(m) for m in markdown_calls)

    @patch("streamlit.markdown")
    @patch("streamlit.columns")
    @patch("streamlit.expander")
    @patch("streamlit.radio")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_results_dashboard_review_button_is_secondary(
        self, mock_rerun, mock_button, mock_radio, mock_expander, mock_columns, mock_markdown
    ):
        """Verify the Review Past Tests button on the results screen is styled as a secondary button."""
        mock_columns.side_effect = mock_columns_factory
        mock_button.return_value = False
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
            review_calls = [c for c in mock_button.call_args_list if "Review" in str(c)]
            assert len(review_calls) > 0
            assert review_calls[0].kwargs.get("type") == "secondary"


class TestHistoryScreenView:
    """Test rendering of previous tests review screen and mock data inspection."""

    @patch("streamlit.markdown")
    @patch("streamlit.columns")
    @patch("streamlit.expander")
    @patch("streamlit.radio")
    @patch("streamlit.selectbox")
    @patch("streamlit.button")
    @patch("streamlit.rerun")
    def test_history_screen_renders_progression_and_selected_attempt(
        self, mock_rerun, mock_button, mock_selectbox, mock_radio, mock_expander, mock_columns, mock_markdown
    ):
        mock_columns.side_effect = mock_columns_factory
        history = get_mock_history()
        assert len(history) == 3

        # Default selectbox returns first option (Attempt 3)
        mock_selectbox.return_value = f"{history[0]['title']} — {history[0]['date']} [83.3% • Almost (Amber)]"
        mock_radio.return_value = "🇬🇧 English"
        mock_button.return_value = False

        fake_session = MockSessionState({
            "page": "history",
            "user_answers": {},
        })

        with patch.object(views.st, "session_state", fake_session):
            views.render_history_screen(history, QUESTIONS)

            markdown_calls = [str(call[0][0]) for call in mock_markdown.call_args_list if len(call[0]) > 0]
            assert any("Previous Tests & Review" in m for m in markdown_calls)
            assert any("Learning Progression Summary" in m for m in markdown_calls)
            assert any("Attempt 3: Post-Vocabulary & Reading Sprint" in m for m in markdown_calls)
