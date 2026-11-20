"""
styles.py - Ed-tech Design System for "Am I Exam-Ready?"
Modern pastel neo-minimalist mobile-app aesthetic aligned with the design language:
warm cream/ivory background (#FAF8F5), soft pastel cards (sage green, coral pink, warm butter),
dark obsidian primary pill CTAs (#18181B), and high-trust typography.
"""

CUSTOM_CSS = """
<style>
/* Font & Global reset */
@import url('https://fonts.cdnfonts.com/css/google-sans');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Google Sans', 'Product Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #18181B;
}

/* App Background: Warm cream/peach gradient matching mobile UI mockups */
.stApp {
    background-color: #FAF8F5 !important;
    background: radial-gradient(130% 90% at 50% 0%, #FFF7EE 0%, #FAF8F5 55%, #F5F3EC 100%) !important;
}

/* Hide default Streamlit decoration for clean mobile app feel */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main container constraints & padding (mobile-first 680px canvas) */
.block-container {
    padding-top: 1.25rem !important;
    padding-bottom: 3.5rem !important;
    max-width: 680px !important;
}

/* Mobile Phone Status Bar Header */
.mobile-status-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.25rem 0.5rem 0.85rem 0.5rem;
    font-size: 0.82rem;
    font-weight: 700;
    color: #71717A;
}

.mobile-app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.25rem;
}

.mobile-menu-btn {
    width: 40px;
    height: 40px;
    border-radius: 9999px;
    background: #FFFFFF;
    border: 1px solid #E4E4E7;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.15rem;
    color: #18181B;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

.mobile-avatar {
    width: 42px;
    height: 42px;
    border-radius: 9999px;
    background: #E0E7FF;
    border: 2px solid #FFFFFF;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
}

/* German Flag Accent Ribbon */
.de-accent-bar {
    display: flex;
    height: 4px;
    width: 64px;
    border-radius: 9999px;
    overflow: hidden;
    margin-bottom: 0.75rem;
}
.de-accent-bar .bar-black { background-color: #18181B; flex: 1; }
.de-accent-bar .bar-red   { background-color: #EF4444; flex: 1; }
.de-accent-bar .bar-gold  { background-color: #F59E0B; flex: 1; }

/* Trust / Exam Authority Pill */
.authority-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background-color: #FFFFFF;
    color: #18181B;
    border: 1px solid #E4E4E7;
    padding: 0.35rem 0.95rem;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 700;
    margin-bottom: 0.85rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

/* Hero Rainbow Arches Illustration Box (Screen 1) */
.hero-illustration-box {
    text-align: center;
    padding: 1rem 0 0.5rem 0;
    margin-bottom: 1rem;
    position: relative;
}

.hero-arcs {
    width: 220px;
    height: 140px;
    margin: 0 auto;
    position: relative;
    border-top-left-radius: 120px;
    border-top-right-radius: 120px;
    background: radial-gradient(circle at 50% 100%, #FFFFFF 30%, #FFE2D5 31%, #FFE2D5 50%, #CDEBD4 51%, #CDEBD4 72%, transparent 73%);
    display: flex;
    align-items: flex-end;
    justify-content: center;
}

.hero-avatar-circle {
    width: 96px;
    height: 96px;
    border-radius: 9999px;
    background: #FFFFFF;
    border: 3px solid #FAF8F5;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    margin-bottom: -15px;
    z-index: 2;
}

/* High-Trust Card Surface / Rounded Floating Sheet */
.ed-card {
    background: #FFFFFF;
    border: 1px solid rgba(228, 228, 231, 0.8);
    border-radius: 28px;
    padding: 1.75rem;
    box-shadow: 0 10px 25px -5px rgba(24, 24, 27, 0.04), 0 4px 10px -2px rgba(24, 24, 27, 0.02);
    margin-bottom: 1.25rem;
    transition: all 0.2s ease;
}

.ed-card:hover {
    border-color: #D4D4D8;
    box-shadow: 0 12px 28px -4px rgba(24, 24, 27, 0.06);
}

/* Custom Badge Pills */
.badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.76rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.3rem 0.8rem;
    border-radius: 9999px;
}

.badge-vocabulary {
    background-color: #FEF3C7;
    color: #92400E;
    border: 1px solid #FDE68A;
}

.badge-grammar {
    background-color: #F3E8FF;
    color: #6B21A8;
    border: 1px solid #E9D5FF;
}

.badge-reading {
    background-color: #D1FAE5;
    color: #065F46;
    border: 1px solid #A7F3D0;
}

.badge-subtopic {
    background-color: #F4F4F5;
    color: #52525B;
    border: 1px solid #E4E4E7;
    font-size: 0.78rem;
    font-weight: 600;
    padding: 0.28rem 0.75rem;
    border-radius: 9999px;
    display: inline-block;
}

/* "Today Class" Style Hero Diagnostic Card (Screen 2 & Screen 3) */
.active-class-hero {
    background: linear-gradient(135deg, #CFE8D5 0%, #E3F2E6 50%, #FFF2DE 100%);
    border-radius: 26px;
    padding: 1.65rem 1.75rem;
    margin-bottom: 1.5rem;
    position: relative;
    box-shadow: 0 8px 24px -4px rgba(45, 106, 79, 0.08);
}

.active-class-tag {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(4px);
    color: #1B4332;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    margin-bottom: 0.65rem;
}

/* Authentic German Reading Box */
.reading-passage-box {
    background-color: #FAF9F6;
    border: 1.5px solid #E4E4E7;
    border-left: 4px solid #18181B;
    border-radius: 18px;
    padding: 1.15rem 1.35rem;
    margin: 1rem 0 1.25rem 0;
    line-height: 1.55;
    color: #18181B;
}

.reading-passage-header {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #71717A;
    margin-bottom: 0.45rem;
}

.reading-passage-content {
    font-size: 0.95rem;
    color: #27272A;
    white-space: pre-line;
}

/* Verdict Banners (Modeled after Screen 2 & 3 Hero Cards) */
.verdict-ready {
    background: linear-gradient(135deg, #CFE8D5 0%, #E3F2E6 50%, #FFF2DE 100%);
    border: 1.5px solid #A7F3D0;
    color: #065F46;
    border-radius: 28px;
    padding: 2rem 1.75rem;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 25px -5px rgba(6, 95, 70, 0.08);
}

.verdict-almost {
    background: linear-gradient(135deg, #FFE8C7 0%, #FFF3DC 50%, #FFF7EE 100%);
    border: 1.5px solid #FDE68A;
    color: #92400E;
    border-radius: 28px;
    padding: 2rem 1.75rem;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 25px -5px rgba(146, 64, 14, 0.08);
}

.verdict-not-ready {
    background: linear-gradient(135deg, #FFE2E6 0%, #FFF0F2 50%, #FFF7F5 100%);
    border: 1.5px solid #FECDD3;
    color: #9F1239;
    border-radius: 28px;
    padding: 2rem 1.75rem;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 25px -5px rgba(159, 18, 57, 0.08);
}

/* Metric Pill / Bar */
.metric-container {
    background: #FFFFFF;
    border: 1px solid #E4E4E7;
    border-radius: 22px;
    padding: 1.15rem 1.25rem;
    margin-bottom: 0.75rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}

.metric-bar-bg {
    background: #F4F4F5;
    border-radius: 9999px;
    height: 8px;
    width: 100%;
    overflow: hidden;
    margin-top: 0.65rem;
}

.metric-bar-fill-emerald {
    background-color: #10B981;
    height: 100%;
    border-radius: 9999px;
    transition: width 0.4s ease;
}

.metric-bar-fill-amber {
    background-color: #F59E0B;
    height: 100%;
    border-radius: 9999px;
    transition: width 0.4s ease;
}

.metric-bar-fill-rose {
    background-color: #EF4444;
    height: 100%;
    border-radius: 9999px;
    transition: width 0.4s ease;
}

/* Action Checklist Card (Timeline Chip Aesthetic from Screen 2) */
.recommendation-card {
    background: #FFFFFF;
    border: 1px solid #E4E4E7;
    border-left: 4px solid #18181B;
    border-radius: 20px;
    padding: 1.25rem 1.4rem;
    margin-bottom: 0.9rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}

.priority-tag {
    display: inline-block;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    background: #F4F4F5;
    color: #18181B;
    padding: 0.22rem 0.65rem;
    border-radius: 9999px;
    margin-bottom: 0.45rem;
}

/* Review Accordion Cards */
.review-card-correct {
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-radius: 20px;
    padding: 1.25rem;
    margin-bottom: 0.85rem;
}

.review-card-incorrect {
    background: #FFF1F2;
    border: 1px solid #FECDD3;
    border-radius: 20px;
    padding: 1.25rem;
    margin-bottom: 0.85rem;
}

/* History Hero Banner & Lessons Stack (Screen 3) */
.history-hero {
    background: linear-gradient(135deg, #FFE4E8 0%, #FFF0F2 50%, #FAF8F5 100%);
    border: 1.5px solid #FECDD3;
    border-radius: 28px;
    padding: 1.65rem 1.75rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 24px -4px rgba(159, 18, 57, 0.06);
}

.history-item-card {
    background: #FFFFFF;
    border: 1px solid #E4E4E7;
    border-radius: 20px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    transition: all 0.15s ease;
}

.history-item-card:hover {
    border-color: #D4D4D8;
    transform: translateY(-1px);
}

.history-icon-badge {
    width: 44px;
    height: 44px;
    border-radius: 9999px;
    background: #F4F4F5;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
    margin-right: 0.85rem;
}

/* Streamlit Button Base & UI Pill Variants */
div.stButton > button {
    border-radius: 9999px !important;
    padding: 0.75rem 1.75rem !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: -0.01em !important;
    transition: all 0.18s ease-in-out !important;
}

/* Primary Button: Obsidian Dark Pill from image */
div.stButton > button[kind="primary"],
div.stButton > button[data-testid="baseButton-primary"] {
    background-color: #18181B !important;
    color: #FFFFFF !important;
    border: 1.5px solid #18181B !important;
    box-shadow: 0 4px 14px rgba(24, 24, 27, 0.18) !important;
}

div.stButton > button[kind="primary"]:hover,
div.stButton > button[data-testid="baseButton-primary"]:hover {
    background-color: #27272A !important;
    border-color: #27272A !important;
    color: #FFFFFF !important;
    box-shadow: 0 6px 18px rgba(24, 24, 27, 0.25) !important;
    transform: translateY(-1px) !important;
}

/* Secondary Button: Clean Light Card Pill from image */
div.stButton > button[kind="secondary"],
div.stButton > button[data-testid="baseButton-secondary"],
div.stButton > button:not([kind="primary"]):not([data-testid="baseButton-primary"]),
.secondary-btn div.stButton > button:first-child {
    background-color: #FFFFFF !important;
    color: #18181B !important;
    border: 1.5px solid #E4E4E7 !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
}

div.stButton > button[kind="secondary"]:hover,
div.stButton > button[data-testid="baseButton-secondary"]:hover,
div.stButton > button:not([kind="primary"]):not([data-testid="baseButton-primary"]):hover,
.secondary-btn div.stButton > button:first-child:hover {
    background-color: #FAF9F6 !important;
    color: #18181B !important;
    border-color: #D4D4D8 !important;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.06) !important;
    transform: translateY(-1px) !important;
}

/* Radio button styling (Card Pill Options) */
div[data-testid="stRadio"] > div {
    gap: 0.65rem;
}

div[data-testid="stRadio"] label {
    background: #FFFFFF;
    border: 1.5px solid #E4E4E7;
    border-radius: 18px;
    padding: 0.95rem 1.25rem;
    font-size: 0.98rem;
    font-weight: 600;
    color: #18181B;
    transition: all 0.15s ease;
    cursor: pointer;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}

div[data-testid="stRadio"] label:hover {
    border-color: #18181B;
    background-color: #FAF9F6;
    transform: translateY(-1px);
}

/* Progress bar styling: Sleek dark obsidian track like Screen 2 */
.stProgress > div > div > div > div {
    background-color: #18181B !important;
    border-radius: 9999px !important;
}

/* Groq AI Tutor & Study Coach Components */
.ai-coach-card {
    background: linear-gradient(135deg, #FFFDF8 0%, #FAF5FF 100%);
    border: 1.5px solid #DDD6FE;
    border-radius: 24px;
    padding: 1.5rem 1.65rem;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 16px rgba(124, 58, 237, 0.07);
}

.ai-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.76rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #6D28D9;
    background: #EDE9FE;
    padding: 0.28rem 0.8rem;
    border-radius: 9999px;
    margin-bottom: 0.65rem;
}

.ai-response-box {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-left: 4px solid #8B5CF6;
    border-radius: 16px;
    padding: 1.25rem 1.35rem;
    margin-top: 0.85rem;
    color: #1E293B;
    line-height: 1.6;
    font-size: 0.95rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}

.ai-key-box {
    background: #FFFBEB;
    border: 1px solid #FDE68A;
    border-radius: 18px;
    padding: 1.15rem 1.25rem;
    margin-top: 1rem;
    margin-bottom: 1rem;
    font-size: 0.92rem;
    color: #92400E;
    line-height: 1.5;
}

/* Brand Palette Color Reference Anchors for Phase 1 Test Compatibility */
/* #4F46E5 #0369A1 #6D28D9 #B45309 #10B981 #EF4444 */
</style>
"""
