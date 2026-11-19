"""
test_phase2.py - Comprehensive Unit Tests for Phase 2 Question Bank
Verifies schema, authenticity, answer options, distribution, and lookup helpers.
"""

import os
import sys
import pytest
from pathlib import Path

# Add project root and phase_2_question_bank to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "phase_2_question_bank"))

from questions import (
    QUESTIONS,
    CATEGORIES,
    CATEGORY_CONFIG,
    get_all_questions,
    get_questions_by_category,
    get_question_by_id
)


class TestQuestionBankIntegrity:
    """Validate structure, counts, and category distribution."""

    def test_total_question_count(self):
        """Must contain exactly 12 questions."""
        assert len(QUESTIONS) == 12, f"Expected 12 questions, found {len(QUESTIONS)}"

    def test_category_distribution(self):
        """Must contain exactly 4 Vocabulary, 4 Grammar, and 4 Reading questions."""
        vocab_qs = [q for q in QUESTIONS if q["category"] == "Vocabulary"]
        grammar_qs = [q for q in QUESTIONS if q["category"] == "Grammar"]
        reading_qs = [q for q in QUESTIONS if q["category"] == "Reading"]

        assert len(vocab_qs) == 4, f"Expected 4 Vocabulary questions, got {len(vocab_qs)}"
        assert len(grammar_qs) == 4, f"Expected 4 Grammar questions, got {len(grammar_qs)}"
        assert len(reading_qs) == 4, f"Expected 4 Reading questions, got {len(reading_qs)}"

    def test_unique_sequential_ids(self):
        """Question IDs must be unique and sequential from 1 to 12."""
        ids = [q["id"] for q in QUESTIONS]
        assert ids == list(range(1, 13)), f"IDs are not 1-12 in sequence: {ids}"
        assert len(set(ids)) == 12, "Duplicate question IDs detected"

    def test_categories_constant(self):
        """CATEGORIES constant must contain Vocabulary, Grammar, and Reading."""
        assert set(CATEGORIES) == {"Vocabulary", "Grammar", "Reading"}
        for cat in CATEGORIES:
            assert cat in CATEGORY_CONFIG
            assert "color" in CATEGORY_CONFIG[cat]
            assert "icon" in CATEGORY_CONFIG[cat]


class TestQuestionSchema:
    """Validate schema, options, and explanation fields for every question."""

    @pytest.mark.parametrize("q", QUESTIONS, ids=[f"Q{q['id']}-{q['category']}" for q in QUESTIONS])
    def test_question_fields(self, q):
        """Every question must conform strictly to the required schema."""
        # 1. Category
        assert q["category"] in CATEGORIES, f"Q{q['id']} invalid category: {q['category']}"

        # 2. Subtopic
        assert isinstance(q["subtopic"], str) and len(q["subtopic"].strip()) > 3, (
            f"Q{q['id']} missing valid subtopic"
        )

        # 3. Prompt
        assert isinstance(q["prompt"], str) and len(q["prompt"].strip()) > 5, (
            f"Q{q['id']} prompt too short or invalid"
        )

        # 4. Options
        assert isinstance(q["options"], list), f"Q{q['id']} options must be a list"
        assert len(q["options"]) == 4, f"Q{q['id']} must have exactly 4 options, got {len(q['options'])}"
        for opt in q["options"]:
            assert isinstance(opt, str) and len(opt.strip()) > 0, f"Q{q['id']} empty option found"
        # Ensure all 4 options are distinct (no duplicate choices)
        assert len(set(q["options"])) == 4, f"Q{q['id']} has duplicate options: {q['options']}"

        # 5. Correct answer index
        assert isinstance(q["correct_answer_index"], int)
        assert q["correct_answer_index"] in [0, 1, 2, 3], (
            f"Q{q['id']} invalid correct_answer_index: {q['correct_answer_index']}"
        )

        # 6. Explanation
        assert isinstance(q["explanation"], str) and len(q["explanation"].strip()) > 25, (
            f"Q{q['id']} explanation must be informative (>25 chars)"
        )

    def test_reading_questions_have_context_snippets(self):
        """All 4 reading questions must have authentic German context snippets."""
        reading_qs = [q for q in QUESTIONS if q["category"] == "Reading"]
        for q in reading_qs:
            assert q.get("context_snippet") is not None, f"Reading Q{q['id']} missing context_snippet"
            assert len(q["context_snippet"].strip()) > 20, f"Reading Q{q['id']} context_snippet too brief"


class TestLookupHelpers:
    """Verify helper retrieval functions."""

    def test_get_all_questions(self):
        all_qs = get_all_questions()
        assert len(all_qs) == 12

    def test_get_questions_by_category(self):
        vocab = get_questions_by_category("Vocabulary")
        grammar = get_questions_by_category("Grammar")
        reading = get_questions_by_category("Reading")
        invalid = get_questions_by_category("NonExistent")

        assert len(vocab) == 4
        assert len(grammar) == 4
        assert len(reading) == 4
        assert len(invalid) == 0

    def test_get_question_by_id(self):
        q1 = get_question_by_id(1)
        assert q1 is not None
        assert q1["id"] == 1
        assert q1["category"] == "Vocabulary"

        q12 = get_question_by_id(12)
        assert q12 is not None
        assert q12["id"] == 12
        assert q12["category"] == "Reading"

        q_none = get_question_by_id(999)
        assert q_none is None
