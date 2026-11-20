"""
src/groq_service.py - Re-export of utils.groq_service for project consistency.
"""
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

__all__ = [
    "DEFAULT_MODEL",
    "FAST_MODEL",
    "AVAILABLE_MODELS",
    "get_groq_api_key",
    "is_groq_available",
    "get_groq_client",
    "generate_study_plan",
    "explain_question_deep_dive",
    "ask_groq_tutor",
]
