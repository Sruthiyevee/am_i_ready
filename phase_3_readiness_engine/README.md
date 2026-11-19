# Phase 3: Readiness Scoring & Dynamic Recommendation Engine

## Overview
Phase 3 implements pure Python mathematical scoring, category aggregation, readiness tier classifications based on official Goethe/ÖSD benchmarks, and dynamic recommendations based on missed subtopics.

---

## 1. Readiness Tier Classification Formula

| Tier | Status | Criteria | Verdict & Guidance |
| :---: | :---: | :--- | :--- |
| **Ready to Book** | **Green** (`#10B981`) | Overall $\ge 80\%$ **AND** every individual skill $\ge 60\%$ | High confidence! Comfortably clears the 60% Goethe/ÖSD benchmark with safety margin. Ready to book exam. |
| **Almost Ready** | **Amber** (`#F59E0B`) | Overall $65\% - 79\%$, **OR** overall $\ge 80\%$ with one skill $< 60\%$ | Close to passing, but protect exam fee (€100–€180). Dedicate 1–2 weeks to weak areas before booking. |
| **Not Ready Yet** | **Red** (`#EF4444`) | Overall $< 65\%$ | High risk of failing. Reinforce core grammar & vocabulary fundamentals before paying fee. |

---

## 2. Dynamic Recommendation Engine
- **Prioritization Rule**: Questions from the **lowest-scoring skill** are prioritized first.
- Generates **2–3 specific, actionable practice recommendations** mapped to the exact subtopics missed.
- **100% Score Edge Case**: If the user scores 100% (0 missed questions), returns **2 Exam-Day Strategy Tips**:
  1. *Exam-Day Pacing*: Allocating the 65-minute Lesen & Schreiben time and Antwortbogen transfer rules.
  2. *Speaking & Listening Focus*: Wortkarten preparation for Sprechen Teil 2 & 3 and Hören repetition rules.

---

## 3. Unit Test Verification
- File: `phase_3_readiness_engine/test_phase3.py`
- **8 / 8 tests passed**:
  - `test_perfect_score_ready_tier`: 100% score logic & exam-day tips.
  - `test_safety_rule_high_overall_low_single_skill_triggers_amber`: 83.3% overall with 50% grammar correctly triggers Amber tier.
  - `test_solid_amber_tier`: 75% score across all categories.
  - `test_not_ready_red_tier`: <65% score.
  - `test_zero_score_edge_case`: 0% score handled without ZeroDivisionError.
  - `test_miss_single_question_gives_at_least_two_recommendations`: Minimum 2 tips when missing 1 question.
  - `test_subtopic_knowledge_base_covers_all_questions`: 100% subtopic coverage.
  - `test_zero_indexed_answers_support`: Robust dictionary key normalization.
