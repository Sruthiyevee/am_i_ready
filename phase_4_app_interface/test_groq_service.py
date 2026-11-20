"""
test_groq_service.py - Unit test suite for Groq LLM Integration
Tests API key loading order, Groq client creation, prompt construction,
study plan generation, question deep dive, tutor Q&A, and UI view components.
"""

import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "utils"))
sys.path.insert(0, str(BASE_DIR / "phase_4_app_interface"))

from utils.groq_service import (
    DEFAULT_MODEL,
    FAST_MODEL,
    AVAILABLE_MODELS,
    get_groq_api_key,
    is_groq_available,
    get_groq_client,
    generate_study_plan,
    explain_question_deep_dive,
    ask_groq_tutor,
)
from data.questions import QUESTIONS
from utils.readiness import calculate_readiness
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


class TestGroqKeyRetrieval:
    """Test priority and fallbacks for Groq API key retrieval."""

    def test_key_from_session_state(self):
        fake_state = MockSessionState({"groq_api_key": "gsk_session_12345"})
        with patch.object(views.st, "session_state", fake_state):
            key = get_groq_api_key()
            assert key == "gsk_session_12345"

    def test_key_from_environment(self):
        fake_state = MockSessionState({})
        with patch.object(views.st, "session_state", fake_state):
            with patch.dict(os.environ, {"GROQ_API_KEY": "gsk_env_67890"}):
                key = get_groq_api_key()
                assert key == "gsk_env_67890"

    def test_key_from_streamlit_secrets(self):
        fake_state = MockSessionState({})
        with patch.object(views.st, "session_state", fake_state):
            with patch.dict(os.environ, {}, clear=True):
                with patch.object(views.st, "secrets", {"GROQ_API_KEY": "gsk_secret_abcde"}):
                    key = get_groq_api_key()
                    assert key == "gsk_secret_abcde"

    def test_key_missing_returns_none(self):
        fake_state = MockSessionState({})
        with patch.object(views.st, "session_state", fake_state):
            with patch.dict(os.environ, {}, clear=True):
                with patch.object(views.st, "secrets", {}):
                    key = get_groq_api_key()
                    assert key is None
                    assert is_groq_available() is False


class TestGroqClientAndCompletions:
    """Test client initialization and LLM completions with mocked Groq SDK."""

    def test_client_raises_value_error_if_no_key(self):
        with patch("utils.groq_service.get_groq_api_key", return_value=None):
            with pytest.raises(ValueError, match="Groq API Key is not configured"):
                get_groq_client()

    @patch("utils.groq_service.Groq")
    def test_generate_study_plan_success(self, mock_groq_class):
        mock_client = MagicMock()
        mock_groq_class.return_value = mock_client
        mock_completion = MagicMock()
        mock_completion.choices = [
            MagicMock(message=MagicMock(content="### 7-Day Personalized German Study Plan\nDay 1: Review Akkusativ."))
        ]
        mock_client.chat.completions.create.return_value = mock_completion

        answers = {1: 0, 2: 1}  # Simulated answers
        res = calculate_readiness(answers, QUESTIONS)

        output = generate_study_plan(res, QUESTIONS, answers, api_key="gsk_test_key")

        assert "7-Day Personalized German Study Plan" in output
        assert mock_client.chat.completions.create.called
        call_kwargs = mock_client.chat.completions.create.call_args.kwargs
        assert call_kwargs["model"] == DEFAULT_MODEL
        # Ensure diagnostic profile was passed
        user_msg = call_kwargs["messages"][1]["content"]
        assert str(res["overall_percentage"]) in user_msg

    @patch("utils.groq_service.Groq")
    def test_explain_question_deep_dive_english(self, mock_groq_class):
        mock_client = MagicMock()
        mock_groq_class.return_value = mock_client
        mock_completion = MagicMock()
        mock_completion.choices = [
            MagicMock(message=MagicMock(content="**Core Concept**: In German, masculine accusative takes 'den'."))
        ]
        mock_client.chat.completions.create.return_value = mock_completion

        q = QUESTIONS[0]
        output = explain_question_deep_dive(q, user_selected_idx=1, language="English", api_key="gsk_test_key")

        assert "Core Concept" in output
        assert mock_client.chat.completions.create.called
        call_kwargs = mock_client.chat.completions.create.call_args.kwargs
        system_msg = call_kwargs["messages"][0]["content"]
        assert "Respond entirely in English" in system_msg

    @patch("utils.groq_service.Groq")
    def test_explain_question_deep_dive_german(self, mock_groq_class):
        mock_client = MagicMock()
        mock_groq_class.return_value = mock_client
        mock_completion = MagicMock()
        mock_completion.choices = [
            MagicMock(message=MagicMock(content="**Erklärung**: Das Noun benötigt den Akkusativ."))
        ]
        mock_client.chat.completions.create.return_value = mock_completion

        q = QUESTIONS[0]
        output = explain_question_deep_dive(q, user_selected_idx=1, language="Deutsch", api_key="gsk_test_key")

        assert "Erklärung" in output
        call_kwargs = mock_client.chat.completions.create.call_args.kwargs
        system_msg = call_kwargs["messages"][0]["content"]
        assert "Antworte auf Deutsch" in system_msg

    @patch("utils.groq_service.Groq")
    def test_ask_groq_tutor_answers_query(self, mock_groq_class):
        mock_client = MagicMock()
        mock_groq_class.return_value = mock_client
        mock_completion = MagicMock()
        mock_completion.choices = [
            MagicMock(message=MagicMock(content="Use 'am' with days: am Montag."))
        ]
        mock_client.chat.completions.create.return_value = mock_completion

        reply = ask_groq_tutor("When do I use am?", api_key="gsk_test_key")
        assert "am Montag" in reply


class TestGroqUIComponents:
    """Test Groq UI renderers in views.py."""

    @patch("streamlit.sidebar")
    @patch("streamlit.markdown")
    @patch("streamlit.selectbox")
    @patch("streamlit.expander")
    @patch("streamlit.text_input")
    @patch("streamlit.button")
    def test_render_groq_sidebar_offline(
        self, mock_btn, mock_input, mock_exp, mock_select, mock_md, mock_sidebar
    ):
        fake_state = MockSessionState({})
        with patch.object(views.st, "session_state", fake_state):
            with patch("utils.groq_service.get_groq_api_key", return_value=None):
                views.render_groq_sidebar()
                # Verify offline notice or API key expander rendered
                assert mock_exp.called
