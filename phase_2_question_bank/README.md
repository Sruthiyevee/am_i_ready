# Phase 2: Authentic A1 Question Bank

## Summary of Diagnostic Question Set
The question bank in `questions.py` provides **12 authentic German multiple-choice questions** mirroring the official **Goethe-Zertifikat A1 (Start Deutsch 1)** and **ÖSD Zertifikat A1** test specifications.

---

### Category & Subtopic Breakdown

| # | Category | Specific Subtopic | Core Concept Tested |
| :---: | :--- | :--- | :--- |
| **Q1** | **Vocabulary** | Food & Everyday Shopping | Packaging / counting nouns (*ein Laib Brot*) |
| **Q2** | **Vocabulary** | City & Directions | Directional adverbs (*nach rechts / links*) |
| **Q3** | **Vocabulary** | Time & Schedule Expressions | 12h/24h colloquial clock time (*Viertel vor drei* = 14:45) |
| **Q4** | **Vocabulary** | Professions & Personal Details | Career preposition construction (*arbeiten als + Beruf*) |
| **Q5** | **Grammar** | Articles (der/die/das) | Masculine accusative definite article (*kaufen -> den Schreibtisch*) |
| **Q6** | **Grammar** | Present Tense Verb Conjugation | 2nd person singular verb ending (*du besuchst*) |
| **Q7** | **Grammar** | Prepositions (im, am, um, nach) | Time prepositions for weekdays and clock times (*am Montag, um 09:00 Uhr*) |
| **Q8** | **Grammar** | Negation (nicht/kein) | Feminine noun negation in the accusative (*keine Zeit*) |
| **Q9** | **Reading** | Reading Personal Messages | Informal party invitation email & requested items (*Salat / Nachtisch*) |
| **Q10** | **Reading** | Reading Notices & Opening Hours | Doctor's office notice with Friday afternoon closure (*Freitagnachmittag geschlossen*) |
| **Q11** | **Reading** | Reading Timetables & Notices | Deutsche Bahn station departures table & track identification (*Gleis 7*) |
| **Q12** | **Reading** | Reading Short Advertisements | Rental apartment classified ad & availability date (*Frei ab 1. August*) |

---

### Unit Test Verification
- Ran `pytest phase_2_question_bank/test_phase2.py -v`.
- **20 / 20 tests passed**: Schema, option count, uniqueness, correct answer ranges, Reading context snippets, and category retrieval helpers verified.
