"""
history.py - Mock Test History for "Am I Exam-Ready?"
Provides realistic mock diagnostic test attempts showing a learner's progression
over time, with detailed question-level answers for review.
"""

from typing import List, Dict, Any, Optional

MOCK_TEST_HISTORY: List[Dict[str, Any]] = [
    {
        "id": "attempt-3",
        "title": "Attempt 3: Post-Vocabulary & Reading Sprint",
        "date": "18 Nov 2026, 16:45",
        "time_spent": "3m 12s",
        "answers": {
            1: 0,   # Q1 Vocab: Laib (Correct)
            2: 1,   # Q2 Vocab: rechts (Correct)
            3: 1,   # Q3 Vocab: Viertel vor drei (Correct)
            4: 2,   # Q4 Vocab: als (Correct)
            5: 1,   # Q5 Grammar: den (Correct)
            6: 1,   # Q6 Grammar: Besuchst (Correct)
            7: 1,   # Q7 Grammar: im / um (Incorrect -> correct is am / um)
            8: 0,   # Q8 Grammar: nicht (Incorrect -> correct is keine)
            9: 1,   # Q9 Reading: Salat / Dessert (Correct)
            10: 2,  # Q10 Reading: Freitag geschlossen (Correct)
            11: 2,  # Q11 Reading: Gleis 7 (Correct)
            12: 2,  # Q12 Reading: 1. August (Correct)
        },
        "notes": (
            "Major improvement in vocabulary and reading comprehension (both 100%). "
            "However, temporal prepositions (am vs. im) and noun negation (nicht vs. keine) still caused errors in Grammar."
        ),
    },
    {
        "id": "attempt-2",
        "title": "Attempt 2: Mid-Preparation Check",
        "date": "11 Nov 2026, 11:20",
        "time_spent": "3m 48s",
        "answers": {
            1: 0,   # Q1 Vocab: Laib (Correct)
            2: 0,   # Q2 Vocab: oben (Incorrect -> correct is rechts)
            3: 0,   # Q3 Vocab: Viertel nach zwei (Incorrect -> correct is Viertel vor drei)
            4: 2,   # Q4 Vocab: als (Correct)
            5: 1,   # Q5 Grammar: den (Correct)
            6: 1,   # Q6 Grammar: Besuchst (Correct)
            7: 0,   # Q7 Grammar: am / um (Correct)
            8: 2,   # Q8 Grammar: keine (Correct)
            9: 1,   # Q9 Reading: Salat / Dessert (Correct)
            10: 0,  # Q10 Reading: 14:00 - 17:30 (Incorrect -> Friday afternoon closed)
            11: 2,  # Q11 Reading: Gleis 7 (Correct)
            12: 0,  # Q12 Reading: drei Zimmer (Incorrect -> correct is 1. August)
        },
        "notes": (
            "Grammar score jumped to 100%! However, directional words in city navigation "
            "and careful scanning of store opening hours still led to errors."
        ),
    },
    {
        "id": "attempt-1",
        "title": "Attempt 1: Baseline Diagnostic",
        "date": "28 Oct 2026, 09:15",
        "time_spent": "4m 20s",
        "answers": {
            1: 1,   # Q1 Vocab: Flasche (Incorrect)
            2: 0,   # Q2 Vocab: oben (Incorrect)
            3: 1,   # Q3 Vocab: Viertel vor drei (Correct)
            4: 0,   # Q4 Vocab: wie (Incorrect)
            5: 0,   # Q5 Grammar: der (Incorrect)
            6: 1,   # Q6 Grammar: Besuchst (Correct)
            7: 1,   # Q7 Grammar: im / um (Incorrect)
            8: 0,   # Q8 Grammar: nicht (Incorrect)
            9: 1,   # Q9 Reading: Salat / Dessert (Correct)
            10: 0,  # Q10 Reading: 14:00 - 17:30 (Incorrect)
            11: 2,  # Q11 Reading: Gleis 7 (Correct)
            12: 2,  # Q12 Reading: 1. August (Correct)
        },
        "notes": (
            "Initial diagnostic before formal A1 study began. "
            "Severe confusion with masculine accusative articles and job prepositions."
        ),
    },
]


def get_mock_history() -> List[Dict[str, Any]]:
    """Return all mock test attempts."""
    return MOCK_TEST_HISTORY


def get_history_attempt_by_id(attempt_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a specific past attempt by its unique ID."""
    for attempt in MOCK_TEST_HISTORY:
        if attempt.get("id") == attempt_id:
            return attempt
    return None
