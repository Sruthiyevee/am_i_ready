"""
test_phase3.py - Comprehensive Unit Tests for Phase 3 Readiness & Recommendation Engine
Tests all tier thresholds, safety buffer logic, edge cases, and personalized recommendations.
"""

import sys
import pytest
from pathlib import Path

# Add project root and phase directories to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "phase_2_question_bank"))
sys.path.insert(0, str(BASE_DIR / "phase_3_readiness_engine"))

from questions import QUESTIONS, get_all_questions
from readiness import (
    calculate_readiness,
    generate_recommendations,
    SUBTOPIC_RECOMMENDATIONS,
    PERFECT_SCORE_TIPS
)


class TestReadinessTierLogic:
    """Validate the 3 readiness tiers and the Goethe/ÖSD 60% + safety buffer."""

    def test_perfect_score_ready_tier(self):
        """12/12 (100%) must result in 'Ready to Book' (Green) and 2 exam-day tips."""
        answers = {q["id"]: q["correct_answer_index"] for q in QUESTIONS}
        result = calculate_readiness(answers)

        assert result["overall_score"] == 12
        assert result["overall_percentage"] == 100.0
        assert result["tier"] == "ready"
        assert result["tier_label"] == "Ready to Book"
        assert result["tier_color"] == "#10B981"
        assert "High confidence" in result["verdict"]

        # All skills 100% and Strong
        for cat, stats in result["skill_breakdown"].items():
            assert stats["score"] == 4
            assert stats["percentage"] == 100.0
            assert stats["status"] == "Strong"

        # 2 Exam-Day tips provided
        recs = result["recommendations"]
        assert len(recs) == 2
        assert "Exam Strategy" in recs[0]["category"]
        assert "Exam-Day Tip 1" in recs[0]["priority_label"]

    def test_safety_rule_high_overall_low_single_skill_triggers_amber(self):
        """
        Safety Buffer Rule:
        Overall score 10/12 (83.3% >= 80%), but Grammar is 2/4 (50% < 60%).
        Must NOT be 'ready'; must be downgraded to 'Almost Ready' (Amber)!
        """
        answers = {}
        for q in QUESTIONS:
            if q["category"] == "Grammar":
                # Only answer 2 correctly, 2 incorrectly
                if q["id"] in [5, 6]:
                    answers[q["id"]] = q["correct_answer_index"]
                else:
                    answers[q["id"]] = (q["correct_answer_index"] + 1) % 4
            else:
                # Answer all Vocabulary and Reading correctly
                answers[q["id"]] = q["correct_answer_index"]

        result = calculate_readiness(answers)

        assert result["overall_score"] == 10
        assert result["overall_percentage"] == 83.3
        assert result["skill_breakdown"]["Grammar"]["percentage"] == 50.0
        assert result["skill_breakdown"]["Vocabulary"]["percentage"] == 100.0
        assert result["skill_breakdown"]["Reading"]["percentage"] == 100.0

        # Safety rule triggers Amber tier
        assert result["tier"] == "almost"
        assert result["tier_label"] == "Almost Ready"
        assert result["tier_color"] == "#F59E0B"
        assert "Grammar" in result["verdict"]

        # Recommendations must prioritize Grammar
        recs = result["recommendations"]
        assert len(recs) >= 2
        assert recs[0]["category"] == "Grammar"

    def test_solid_amber_tier(self):
        """9/12 (75%) with 3/4 (75%) across each skill must be 'Almost Ready' (Amber)."""
        answers = {}
        for q in QUESTIONS:
            # Miss 1 in each category: Q4 (Vocab), Q8 (Grammar), Q12 (Reading)
            if q["id"] in [4, 8, 12]:
                answers[q["id"]] = (q["correct_answer_index"] + 1) % 4
            else:
                answers[q["id"]] = q["correct_answer_index"]

        result = calculate_readiness(answers)

        assert result["overall_score"] == 9
        assert result["overall_percentage"] == 75.0
        assert result["tier"] == "almost"
        assert result["tier_label"] == "Almost Ready"
        assert result["tier_color"] == "#F59E0B"

        for cat, stats in result["skill_breakdown"].items():
            assert stats["score"] == 3
            assert stats["percentage"] == 75.0
            assert stats["status"] == "Passing"

        # Exactly 3 recommendations for the 3 missed subtopics
        recs = result["recommendations"]
        assert len(recs) == 3

    def test_not_ready_red_tier(self):
        """7/12 (58.3% < 65%) must be 'Not Ready Yet' (Red)."""
        answers = {}
        # Miss 5 questions: 2 Vocab, 2 Grammar, 1 Reading
        missed_ids = [1, 2, 5, 6, 9]
        for q in QUESTIONS:
            if q["id"] in missed_ids:
                answers[q["id"]] = (q["correct_answer_index"] + 1) % 4
            else:
                answers[q["id"]] = q["correct_answer_index"]

        result = calculate_readiness(answers)

        assert result["overall_score"] == 7
        assert result["overall_percentage"] == 58.3
        assert result["tier"] == "not_ready"
        assert result["tier_label"] == "Not Ready Yet"
        assert result["tier_color"] == "#EF4444"
        assert "Not yet exam-ready" in result["verdict"]

    def test_zero_score_edge_case(self):
        """0/12 (0%) score must handle cleanly without ZeroDivisionError."""
        answers = {q["id"]: (q["correct_answer_index"] + 1) % 4 for q in QUESTIONS}
        result = calculate_readiness(answers)

        assert result["overall_score"] == 0
        assert result["overall_percentage"] == 0.0
        assert result["tier"] == "not_ready"
        assert len(result["recommendations"]) == 3


class TestRecommendationEngine:
    """Validate generation of targeted subtopic practice guidance."""

    def test_miss_single_question_gives_at_least_two_recommendations(self):
        """Missing only 1 question must return the specific focus + an exam strategy tip."""
        # Only miss Q5: Articles (der/die/das)
        answers = {q["id"]: q["correct_answer_index"] for q in QUESTIONS}
        answers[5] = (answers[5] + 1) % 4

        result = calculate_readiness(answers)
        recs = result["recommendations"]

        assert len(recs) == 2
        assert recs[0]["subtopic"] == "Articles (der/die/das)"
        assert recs[0]["category"] == "Grammar"
        assert "Akkusativ" in recs[0]["action"]
        assert recs[1]["category"] == "General Strategy"

    def test_subtopic_knowledge_base_covers_all_questions(self):
        """Every question in the question bank must have a mapped subtopic recommendation."""
        for q in QUESTIONS:
            subtopic = q["subtopic"]
            assert subtopic in SUBTOPIC_RECOMMENDATIONS, (
                f"Missing recommendation mapping for subtopic: '{subtopic}' in Q{q['id']}"
            )
            rec = SUBTOPIC_RECOMMENDATIONS[subtopic]
            assert "title" in rec and len(rec["title"]) > 5
            assert "action" in rec and len(rec["action"]) > 20
            assert "tip" in rec and len(rec["tip"]) > 10


class TestInputFormatsAndRobustness:
    """Validate flexibility with 0-indexed vs 1-indexed answer dicts."""

    def test_zero_indexed_answers_support(self):
        """Passing {0: opt, 1: opt, ...} should produce identical results to {1: opt, 2: opt, ...}."""
        answers_1_based = {q["id"]: q["correct_answer_index"] for q in QUESTIONS}
        answers_0_based = {i: q["correct_answer_index"] for i, q in enumerate(QUESTIONS)}

        res_1 = calculate_readiness(answers_1_based)
        res_0 = calculate_readiness(answers_0_based)

        assert res_1["overall_score"] == res_0["overall_score"] == 12
        assert res_1["overall_percentage"] == res_0["overall_percentage"] == 100.0
        assert res_1["tier"] == res_0["tier"] == "ready"
