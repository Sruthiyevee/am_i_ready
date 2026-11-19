"""
questions.py - Authentic A1 German Question Bank
Aligned with Goethe-Zertifikat A1 (Start Deutsch 1) & ÖSD Zertifikat A1 standards.

Contains 12 questions:
- 4 Vocabulary questions
- 4 Grammar questions
- 4 Reading comprehension questions (with authentic German context snippets)
"""

from typing import List, Dict, Any, Optional

CATEGORIES = ["Vocabulary", "Grammar", "Reading"]

CATEGORY_CONFIG = {
    "Vocabulary": {
        "color": "#0369A1",
        "bg_color": "#E0F2FE",
        "border_color": "#BAE6FD",
        "icon": "📚",
        "description": "Everyday objects, food, directions, time expressions & personal details",
    },
    "Grammar": {
        "color": "#6D28D9",
        "bg_color": "#EDE9FE",
        "border_color": "#DDD6FE",
        "icon": "🧩",
        "description": "Articles (der/die/das), verb conjugation, prepositions & negation",
    },
    "Reading": {
        "color": "#B45309",
        "bg_color": "#FEF3C7",
        "border_color": "#FDE68A",
        "icon": "📖",
        "description": "Short emails, store opening hours, transit timetables & classified ads",
    },
}

QUESTIONS: List[Dict[str, Any]] = [
    # ==========================================
    # 1. VOCABULARY (Questions 1 - 4)
    # ==========================================
    {
        "id": 1,
        "category": "Vocabulary",
        "subtopic": "Food & Everyday Shopping",
        "prompt": "Im Supermarkt: „Guten Tag! Ich brauche ein Kilo Äpfel und ein _____ Brot, bitte.“",
        "context_snippet": None,
        "options": [
            "Laib",
            "Flasche",
            "Becher",
            "Glas"
        ],
        "correct_answer_index": 0,
        "explanation": (
            "Richtig ist „Laib“ (ein Laib Brot = a loaf of bread). "
            "„Flasche“ wird für Flüssigkeiten verwendet (eine Flasche Wasser), "
            "„Becher“ für Joghurt oder Sahne, und „Glas“ für Marmelade oder Honig."
        ),
    },
    {
        "id": 2,
        "category": "Vocabulary",
        "subtopic": "City & Directions",
        "prompt": "Auf der Straße: „Entschuldigung, wie komme ich zum Bahnhof?“ – „Gehen Sie hier geradeaus und an der Kreuzung nach _____ .“",
        "context_snippet": None,
        "options": [
            "oben",
            "rechts",
            "hinten",
            "dort"
        ],
        "correct_answer_index": 1,
        "explanation": (
            "Richtig ist „rechts“ (nach rechts / nach links = turn right / turn left). "
            "„nach oben“ bedeutet 'upwards', „nach hinten“ bedeutet 'to the rear', "
            "und bei „dort“ sagt man 'dorthin', nicht 'nach dort'."
        ),
    },
    {
        "id": 3,
        "category": "Vocabulary",
        "subtopic": "Time & Schedule Expressions",
        "prompt": "Die Uhrzeit: Wie sagt man im Alltag zu 14:45 Uhr?",
        "context_snippet": None,
        "options": [
            "Viertel nach zwei",
            "Viertel vor drei",
            "Halb drei",
            "Zehn vor drei"
        ],
        "correct_answer_index": 1,
        "explanation": (
            "14:45 Uhr bedeutet „Viertel vor drei“ (quarter to three in the afternoon). "
            "„Viertel nach zwei“ wäre 14:15 Uhr, und „Halb drei“ ist 14:30 Uhr."
        ),
    },
    {
        "id": 4,
        "category": "Vocabulary",
        "subtopic": "Professions & Personal Details",
        "prompt": "Beim Vorstellungsgespräch: „Was sind Sie von Beruf?“ – „Ich arbeite _____ Ingenieur bei Siemens.“",
        "context_snippet": None,
        "options": [
            "wie",
            "für",
            "als",
            "bei"
        ],
        "correct_answer_index": 2,
        "explanation": (
            "Im Deutschen sagt man „arbeiten als + Beruf“ (Ich arbeite als Ingenieur / als Lehrerin). "
            "„bei Siemens“ benennt den Arbeitgeber, aber vor der Berufsbezeichnung steht „als“."
        ),
    },

    # ==========================================
    # 2. GRAMMAR (Questions 5 - 8)
    # ==========================================
    {
        "id": 5,
        "category": "Grammar",
        "subtopic": "Articles (der/die/das)",
        "prompt": "Ergänzen Sie den bestimmten Artikel: „Kaufst du _____ Schreibtisch (maskulin)? Er gefällt mir sehr gut.“",
        "context_snippet": None,
        "options": [
            "der",
            "den",
            "dem",
            "das"
        ],
        "correct_answer_index": 1,
        "explanation": (
            "Richtig ist „den“. Das Verb „kaufen“ verlangt den Akkusativ (Wen oder was kaufst du?). "
            "Der maskuline Artikel „der“ wird im Akkusativ zu „den“ (der Schreibtisch -> den Schreibtisch)."
        ),
    },
    {
        "id": 6,
        "category": "Grammar",
        "subtopic": "Present Tense Verb Conjugation",
        "prompt": "Konjugation im Präsens: „_____ du am Wochenende deine Großeltern in München?“ (besuchen)",
        "context_snippet": None,
        "options": [
            "Besuche",
            "Besuchst",
            "Besucht",
            "Besuchen"
        ],
        "correct_answer_index": 1,
        "explanation": (
            "Richtig ist „Besuchst“. Die 2. Person Singular („du“) hat im Präsens die Endung „-st“: "
            "du besuchst. (ich besuche, du besuchst, er/sie/es besucht, wir besuchen)."
        ),
    },
    {
        "id": 7,
        "category": "Grammar",
        "subtopic": "Prepositions (im, am, um, nach)",
        "prompt": "Ergänzen Sie die Zeitpräpositionen: „Der Deutschkurs beginnt _____ Montag _____ 09:00 Uhr.“",
        "context_snippet": None,
        "options": [
            "am / um",
            "im / um",
            "um / am",
            "am / im"
        ],
        "correct_answer_index": 0,
        "explanation": (
            "Für Wochentage und Tageszeiten verwendet man „am“ (am Montag, am Morgen). "
            "Für genaue Uhrzeiten verwendet man immer „um“ (um 09:00 Uhr). "
            "Daher ist „am / um“ die einzig richtige Kombination."
        ),
    },
    {
        "id": 8,
        "category": "Grammar",
        "subtopic": "Negation (nicht/kein)",
        "prompt": "Ergänzen Sie die richtige Negation: „Haben Sie einen Moment Zeit?“ – „Nein, leider habe ich heute _____ Zeit.“",
        "context_snippet": None,
        "options": [
            "nicht",
            "kein",
            "keine",
            "keinen"
        ],
        "correct_answer_index": 2,
        "explanation": (
            "Das Nomen „Zeit“ ist feminin („die Zeit“). Um Nomen ohne bestimmten Artikel zu verneinen, "
            "benutzt man „kein-“. Im Akkusativ Femininum lautet die Endung „-e“: „keine Zeit“."
        ),
    },

    # ==========================================
    # 3. READING COMPREHENSION (Questions 9 - 12)
    # ==========================================
    {
        "id": 9,
        "category": "Reading",
        "subtopic": "Reading Personal Messages",
        "prompt": "Lesen Sie die kurze E-Mail. Was soll Markus mitbringen?",
        "context_snippet": (
            "Lieber Markus,\n"
            "am Samstag feiere ich meinen Geburtstag ab 19:00 Uhr im Garten. "
            "Getränke und Fleisch zum Grillen habe ich schon gekauft. "
            "Könntest du bitte einen Salat oder einen Nachtisch mitbringen? "
            "Bitte sag mir bis Donnerstag Bescheid!\n"
            "Viele Grüße,\n"
            "Lena"
        ),
        "options": [
            "Fleisch und Würstchen",
            "Einen Salat oder ein Dessert",
            "Getränke für die Gäste",
            "Einen Grill für den Garten"
        ],
        "correct_answer_index": 1,
        "explanation": (
            "In der E-Mail steht: „Könntest du bitte einen Salat oder einen Nachtisch mitbringen?“ "
            "(Nachtisch = Dessert). Fleisch und Getränke hat Lena bereits selbst gekauft."
        ),
    },
    {
        "id": 10,
        "category": "Reading",
        "subtopic": "Reading Notices & Opening Hours",
        "prompt": "Lesen Sie den Aushang an einer Arztpraxis. Wann hat die Praxis am Freitagnachmittag geöffnet?",
        "context_snippet": (
            "Praxis Dr. med. Weber — Allgemeinmedizin\n\n"
            "Sprechzeiten:\n"
            "• Montag – Donnerstag: 08:00 – 12:00 Uhr & 14:00 – 17:30 Uhr\n"
            "• Freitag: 08:00 – 13:00 Uhr\n"
            "• Freitagnachmittag geschlossen.\n\n"
            "In dringenden Notfällen wenden Sie sich bitte an den ärztlichen Bereitschaftsdienst: Tel. 116 117."
        ),
        "options": [
            "Von 14:00 bis 17:30 Uhr",
            "Von 08:00 bis 13:00 Uhr",
            "Am Freitagnachmittag ist geschlossen",
            "Bis 18:00 Uhr"
        ],
        "correct_answer_index": 2,
        "explanation": (
            "Auf dem Aushang steht ausdrücklich: „Freitag: 08:00 – 13:00 Uhr“ und "
            "„Freitagnachmittag geschlossen“. Die Praxis hat am Freitagnachmittag nicht geöffnet."
        ),
    },
    {
        "id": 11,
        "category": "Reading",
        "subtopic": "Reading Timetables & Notices",
        "prompt": "Lesen Sie die Zug-Information am Bahnhof. Von welchem Gleis fährt der ICE nach Hamburg ab?",
        "context_snippet": (
            "Deutsche Bahn — Abfahrt Berlin Hbf\n\n"
            "Zug: ICE 804  | Nach: Hamburg Hbf   | Abfahrt: 10:38 | Gleis: 7 | Pünktlich\n"
            "Zug: RE 1     | Nach: Frankfurt/Oder | Abfahrt: 10:42 | Gleis: 2 | +5 Min.\n"
            "Zug: ICE 573  | Nach: München Hbf   | Abfahrt: 10:45 | Gleis: 5 | Pünktlich"
        ),
        "options": [
            "Gleis 2",
            "Gleis 5",
            "Gleis 7",
            "Gleis 8"
        ],
        "correct_answer_index": 2,
        "explanation": (
            "Der ICE 804 nach Hamburg Hbf fährt planmäßig um 10:38 Uhr von Gleis 7 ab. "
            "Gleis 2 ist für den RE 1 nach Frankfurt/Oder und Gleis 5 für den ICE nach München."
        ),
    },
    {
        "id": 12,
        "category": "Reading",
        "subtopic": "Reading Short Advertisements",
        "prompt": "Lesen Sie die Wohnungsanzeige. Welche Aussage ist richtig?",
        "context_snippet": (
            "Wohnung zu vermieten:\n"
            "Helle 2-Zimmer-Wohnung in Köln-Ehrenfeld, 55 qm, mit Einbauküche und Balkon. "
            "Ruhige Lage nahe U-Bahn-Station. Frei ab 1. August. "
            "Kaltmiete: 650 € zzgl. 120 € Nebenkosten. "
            "Haustiere sind leider nicht erlaubt."
        ),
        "options": [
            "Die Wohnung hat drei Zimmer.",
            "Man darf Hunde oder Katzen mitbringen.",
            "Die Wohnung ist ab dem 1. August frei.",
            "Die Warmmiete beträgt insgesamt 650 €."
        ],
        "correct_answer_index": 2,
        "explanation": (
            "In der Anzeige steht: „Frei ab 1. August“. "
            "Die anderen Aussagen sind falsch: Es ist eine 2-Zimmer-Wohnung (nicht 3), "
            "Haustiere sind nicht erlaubt, und 650 € ist nur die Kaltmiete (zzgl. 120 € Nebenkosten = 770 € Warmmiete)."
        ),
    },
]


def get_all_questions() -> List[Dict[str, Any]]:
    """Return all 12 diagnostic questions."""
    return QUESTIONS


def get_questions_by_category(category: str) -> List[Dict[str, Any]]:
    """Filter questions by category (Vocabulary, Grammar, or Reading)."""
    return [q for q in QUESTIONS if q.get("category") == category]


def get_question_by_id(question_id: int) -> Optional[Dict[str, Any]]:
    """Retrieve a single question by its numeric ID (1-12)."""
    for q in QUESTIONS:
        if q.get("id") == question_id:
            return q
    return None
