"""
questions.py - Authentic A1 German Question Bank
Aligned with Goethe-Zertifikat A1 (Start Deutsch 1) & ÖSD Zertifikat A1 standards.

Contains 12 questions:
- 4 Vocabulary questions
- 4 Grammar questions
- 4 Reading comprehension questions (with authentic German context snippets)
- Bilingual explanations (German & English) and English prompt translations
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
        "prompt_en": "At the supermarket: \"Hello! I need a kilo of apples and a _____ of bread, please.\"",
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
        "explanation_de": (
            "Richtig ist „Laib“ (ein Laib Brot = a loaf of bread). "
            "„Flasche“ wird für Flüssigkeiten verwendet (eine Flasche Wasser), "
            "„Becher“ für Joghurt oder Sahne, und „Glas“ für Marmelade oder Honig."
        ),
        "explanation_en": (
            "Correct answer: \"Laib\" (a loaf of bread). In German, specific measurement and packaging nouns are used for food items: "
            "\"ein Laib Brot\" = a loaf of bread. \"Flasche\" is used for liquids (eine Flasche Wasser = a bottle of water), "
            "\"Becher\" is used for tubs/cups of yogurt or sour cream (ein Becher Joghurt), and \"Glas\" is used for jars (ein Glas Marmelade = a jar of jam)."
        ),
    },
    {
        "id": 2,
        "category": "Vocabulary",
        "subtopic": "City & Directions",
        "prompt": "Auf der Straße: „Entschuldigung, wie komme ich zum Bahnhof?“ – „Gehen Sie hier geradeaus und an der Kreuzung nach _____ .“",
        "prompt_en": "On the street: \"Excuse me, how do I get to the train station?\" – \"Go straight ahead here, and at the intersection turn _____ .\"",
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
        "explanation_de": (
            "Richtig ist „rechts“ (nach rechts / nach links = turn right / turn left). "
            "„nach oben“ bedeutet 'upwards', „nach hinten“ bedeutet 'to the rear', "
            "und bei „dort“ sagt man 'dorthin', nicht 'nach dort'."
        ),
        "explanation_en": (
            "Correct answer: \"rechts\" (right). When giving spatial directions, German uses the preposition \"nach\" with directions: "
            "\"nach rechts\" (to the right / turn right) and \"nach links\" (to the left / turn left). "
            "\"nach oben\" means upwards, \"nach hinten\" means to the rear/back, and the location adverb \"dort\" (there) takes the directional form \"dorthin\", never \"nach dort\"."
        ),
    },
    {
        "id": 3,
        "category": "Vocabulary",
        "subtopic": "Time & Schedule Expressions",
        "prompt": "Die Uhrzeit: Wie sagt man im Alltag zu 14:45 Uhr?",
        "prompt_en": "Clock time: How do you say 14:45 (2:45 PM) in everyday conversational German?",
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
        "explanation_de": (
            "14:45 Uhr bedeutet „Viertel vor drei“ (quarter to three in the afternoon). "
            "„Viertel nach zwei“ wäre 14:15 Uhr, und „Halb drei“ ist 14:30 Uhr."
        ),
        "explanation_en": (
            "Correct answer: \"Viertel vor drei\" (quarter to three). In colloquial German, clock times refer to the upcoming hour: "
            "14:45 is 15 minutes before 3:00, hence \"Viertel vor drei\". "
            "\"Viertel nach zwei\" is 14:15 (quarter past two), \"Halb drei\" is 14:30 (half-way to 3:00, not 3:30!), and \"Zehn vor drei\" is 14:50 (ten to three)."
        ),
    },
    {
        "id": 4,
        "category": "Vocabulary",
        "subtopic": "Professions & Personal Details",
        "prompt": "Beim Vorstellungsgespräch: „Was sind Sie von Beruf?“ – „Ich arbeite _____ Ingenieur bei Siemens.“",
        "prompt_en": "At a job interview: \"What is your profession?\" – \"I work _____ an engineer at Siemens.\"",
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
        "explanation_de": (
            "Im Deutschen sagt man „arbeiten als + Beruf“ (Ich arbeite als Ingenieur / als Lehrerin). "
            "„bei Siemens“ benennt den Arbeitgeber, aber vor der Berufsbezeichnung steht „als“."
        ),
        "explanation_en": (
            "Correct answer: \"als\" (as). In German, the standard construction for stating your job title is \"arbeiten als + profession\" "
            "(e.g. \"Ich arbeite als Ingenieur\" = I work as an engineer; \"Ich arbeite als Lehrerin\" = I work as a female teacher). "
            "\"bei\" is used for the employer (\"bei Siemens\"), while \"wie\" means like/as in comparison, and \"für\" means for."
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
        "prompt_en": "Fill in the definite article: \"Are you buying _____ desk (masculine)? I like it very much.\"",
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
        "explanation_de": (
            "Richtig ist „den“. Das Verb „kaufen“ verlangt den Akkusativ (Wen oder was kaufst du?). "
            "Der maskuline Artikel „der“ wird im Akkusativ zu „den“ (der Schreibtisch -> den Schreibtisch)."
        ),
        "explanation_en": (
            "Correct answer: \"den\" (the). The noun \"Schreibtisch\" is masculine (\"der Schreibtisch\"). "
            "The verb \"kaufen\" (to buy) takes a direct object in the Accusative case (Wen oder was kaufst du? = What are you buying?). "
            "In the Accusative case, only masculine articles change: \"der\" becomes \"den\". Feminine (\"die\") and neuter (\"das\") remain unchanged."
        ),
    },
    {
        "id": 6,
        "category": "Grammar",
        "subtopic": "Present Tense Verb Conjugation",
        "prompt": "Konjugation im Präsens: „_____ du am Wochenende deine Großeltern in München?“ (besuchen)",
        "prompt_en": "Conjugation in present tense: \"_____ you your grandparents in Munich this weekend?\" (besuchen = to visit)",
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
        "explanation_de": (
            "Richtig ist „Besuchst“. Die 2. Person Singular („du“) hat im Präsens die Endung „-st“: "
            "du besuchst. (ich besuche, du besuchst, er/sie/es besucht, wir besuchen)."
        ),
        "explanation_en": (
            "Correct answer: \"Besuchst\" (Do you visit / Are you visiting...?). "
            "In German present tense verb conjugation, regular verbs take the ending \"-st\" for the second-person singular pronoun \"du\": "
            "ich besuche (-e), du besuchst (-st), er/sie/es besucht (-t), wir besuchen (-en)."
        ),
    },
    {
        "id": 7,
        "category": "Grammar",
        "subtopic": "Prepositions (im, am, um, nach)",
        "prompt": "Ergänzen Sie die Zeitpräpositionen: „Der Deutschkurs beginnt _____ Montag _____ 09:00 Uhr.“",
        "prompt_en": "Complete the time prepositions: \"The German course begins _____ Monday _____ 09:00 AM.\"",
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
        "explanation_de": (
            "Für Wochentage und Tageszeiten verwendet man „am“ (am Montag, am Morgen). "
            "Für genaue Uhrzeiten verwendet man immer „um“ (um 09:00 Uhr). "
            "Daher ist „am / um“ die einzig richtige Kombination."
        ),
        "explanation_en": (
            "Correct answer: \"am / um\". In German time expressions: "
            "1. Use \"am\" (an + dem) for days of the week, dates, and parts of the day: \"am Montag\" (on Monday), \"am Vormittag\" (in the morning). "
            "2. Use \"um\" for exact clock times: \"um 09:00 Uhr\" (at 9:00 AM). "
            "\"im\" (in + dem) is reserved for months and seasons (im August, im Sommer)."
        ),
    },
    {
        "id": 8,
        "category": "Grammar",
        "subtopic": "Negation (nicht/kein)",
        "prompt": "Ergänzen Sie die richtige Negation: „Haben Sie einen Moment Zeit?“ – „Nein, leider habe ich heute _____ Zeit.“",
        "prompt_en": "Fill in the correct negation: \"Do you have a moment?\" – \"No, unfortunately I have _____ time today.\"",
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
        "explanation_de": (
            "Das Nomen „Zeit“ ist feminin („die Zeit“). Um Nomen ohne bestimmten Artikel zu verneinen, "
            "benutzt man „kein-“. Im Akkusativ Femininum lautet die Endung „-e“: „keine Zeit“."
        ),
        "explanation_en": (
            "Correct answer: \"keine\" (no / not any). In German, nouns without a definite article or nouns that take an indefinite article (\"ein/eine\") are negated using \"kein-\", never \"nicht\". "
            "The noun \"Zeit\" (time) is feminine (\"die Zeit\"). In the Accusative case (haben + object), the feminine form takes the ending \"-e\": \"keine Zeit\". "
            "\"nicht\" is only used to negate verbs, adjectives, adverbs, or nouns with a definite article."
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
        "prompt_en": "Read the short email. What is Markus asked to bring?",
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
        "explanation_de": (
            "In der E-Mail steht: „Könntest du bitte einen Salat oder einen Nachtisch mitbringen?“ "
            "(Nachtisch = Dessert). Fleisch und Getränke hat Lena bereits selbst gekauft."
        ),
        "explanation_en": (
            "Correct answer: \"Einen Salat oder ein Dessert\" (A salad or a dessert). "
            "In the email, Lena writes: \"Könntest du bitte einen Salat oder einen Nachtisch mitbringen?\" (\"Nachtisch\" is the German word for dessert). "
            "The other options are wrong: Lena explicitly writes that she already bought the drinks and meat for grilling (\"Getränke und Fleisch zum Grillen habe ich schon gekauft\")."
        ),
    },
    {
        "id": 10,
        "category": "Reading",
        "subtopic": "Reading Notices & Opening Hours",
        "prompt": "Lesen Sie den Aushang an einer Arztpraxis. Wann hat die Praxis am Freitagnachmittag geöffnet?",
        "prompt_en": "Read the doctor's office notice. When is the clinic open on Friday afternoon?",
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
        "explanation_de": (
            "Auf dem Aushang steht ausdrücklich: „Freitag: 08:00 – 13:00 Uhr“ und "
            "„Freitagnachmittag geschlossen“. Die Praxis hat am Freitagnachmittag nicht geöffnet."
        ),
        "explanation_en": (
            "Correct answer: \"Am Freitagnachmittag ist geschlossen\" (It is closed on Friday afternoon). "
            "The clinic schedule states: \"Freitag: 08:00 – 13:00 Uhr\" and explicitly notes \"Freitagnachmittag geschlossen\" (closed Friday afternoon). "
            "The afternoon hours (14:00 – 17:30) only apply Monday through Thursday (\"Montag – Donnerstag\")."
        ),
    },
    {
        "id": 11,
        "category": "Reading",
        "subtopic": "Reading Timetables & Notices",
        "prompt": "Lesen Sie die Zug-Information am Bahnhof. Von welchem Gleis fährt der ICE nach Hamburg ab?",
        "prompt_en": "Read the train schedule display at the station. From which platform does the ICE to Hamburg depart?",
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
        "explanation_de": (
            "Der ICE 804 nach Hamburg Hbf fährt planmäßig um 10:38 Uhr von Gleis 7 ab. "
            "Gleis 2 ist für den RE 1 nach Frankfurt/Oder und Gleis 5 für den ICE nach München."
        ),
        "explanation_en": (
            "Correct answer: \"Gleis 7\" (Track / Platform 7). "
            "Looking at the departure board for destination Hamburg Hbf: \"Zug: ICE 804 | Nach: Hamburg Hbf | Abfahrt: 10:38 | Gleis: 7\". "
            "Gleis 2 is for the regional train RE 1 to Frankfurt/Oder, and Gleis 5 is for the ICE to München."
        ),
    },
    {
        "id": 12,
        "category": "Reading",
        "subtopic": "Reading Short Advertisements",
        "prompt": "Lesen Sie die Wohnungsanzeige. Welche Aussage ist richtig?",
        "prompt_en": "Read the apartment rental listing. Which statement is correct?",
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
        "explanation_de": (
            "In der Anzeige steht: „Frei ab 1. August“. "
            "Die anderen Aussagen sind falsch: Es ist eine 2-Zimmer-Wohnung (nicht 3), "
            "Haustiere sind nicht erlaubt, und 650 € ist nur die Kaltmiete (zzgl. 120 € Nebenkosten = 770 € Warmmiete)."
        ),
        "explanation_en": (
            "Correct answer: \"Die Wohnung ist ab dem 1. August frei.\" (The apartment is available from August 1st). "
            "The advertisement states: \"Frei ab 1. August\". The other options are false: it is a 2-room apartment (not 3), "
            "pets are not permitted (\"Haustiere sind leider nicht erlaubt\"), and 650 € is only the cold rent without utilities (\"Kaltmiete: 650 € zzgl. 120 € Nebenkosten\" = 770 € total warm rent)."
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
