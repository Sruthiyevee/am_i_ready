"""
styles.py - Ed-tech Design System for "Am I Exam-Ready?"
Modern, calm, high-trust theme with slate-50 background, deep indigo primary,
and semantic indicators (emerald, amber, rose).
"""

CUSTOM_CSS = """
<style>
/* Font & Global reset */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #0F172A;
}

/* Hide default Streamlit header and footer decoration for clean app look */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main container constraints & padding */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 3.5rem !important;
    max-width: 820px !important;
}

/* German Flag Accent Ribbon */
.de-accent-bar {
    display: flex;
    height: 4px;
    width: 72px;
    border-radius: 9999px;
    overflow: hidden;
    margin-bottom: 1.25rem;
}
.de-accent-bar .bar-black { background-color: #111827; flex: 1; }
.de-accent-bar .bar-red   { background-color: #DC2626; flex: 1; }
.de-accent-bar .bar-gold  { background-color: #F59E0B; flex: 1; }

/* Custom Badge Pills */
.badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.28rem 0.75rem;
    border-radius: 9999px;
}

.badge-vocabulary {
    background-color: #E0F2FE;
    color: #0369A1;
    border: 1px solid #BAE6FD;
}

.badge-grammar {
    background-color: #EDE9FE;
    color: #6D28D9;
    border: 1px solid #DDD6FE;
}

.badge-reading {
    background-color: #FEF3C7;
    color: #B45309;
    border: 1px solid #FDE68A;
}

.badge-subtopic {
    background-color: #F1F5F9;
    color: #475569;
    border: 1px solid #E2E8F0;
    font-size: 0.8rem;
    font-weight: 600;
    padding: 0.25rem 0.7rem;
    border-radius: 6px;
    display: inline-block;
}

/* Trust / Exam Authority Pill */
.authority-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background-color: #EEF2FF;
    color: #4338CA;
    border: 1px solid #C7D2FE;
    padding: 0.35rem 0.85rem;
    border-radius: 9999px;
    font-size: 0.82rem;
    font-weight: 600;
    margin-bottom: 0.85rem;
}

/* High-Trust Card Surface */
.ed-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 1.75rem;
    box-shadow: 0 4px 6px -1px rgba(15, 23, 42, 0.04), 0 2px 4px -2px rgba(15, 23, 42, 0.02);
    margin-bottom: 1.5rem;
    transition: all 0.2s ease;
}

.ed-card:hover {
    border-color: #CBD5E1;
    box-shadow: 0 10px 15px -3px rgba(15, 23, 42, 0.06), 0 4px 6px -4px rgba(15, 23, 42, 0.03);
}

/* Authentic German Reading Box */
.reading-passage-box {
    background-color: #FAFAFA;
    border: 1.5px solid #E4E4E7;
    border-left: 4px solid #4F46E5;
    border-radius: 8px;
    padding: 1.15rem 1.35rem;
    margin: 1rem 0 1.35rem 0;
    font-family: 'Plus Jakarta Sans', sans-serif;
    line-height: 1.55;
    color: #18181B;
}

.reading-passage-header {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #6366F1;
    margin-bottom: 0.45rem;
}

.reading-passage-content {
    font-size: 0.95rem;
    color: #27272A;
    white-space: pre-line;
}

/* Verdict Banners */
.verdict-ready {
    background: linear-gradient(135deg, #ECFDF5 0%, #F0FDF4 100%);
    border: 1.5px solid #6EE7B7;
    color: #065F46;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-bottom: 1.75rem;
}

.verdict-almost {
    background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
    border: 1.5px solid #FCD34D;
    color: #92400E;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-bottom: 1.75rem;
}

.verdict-not-ready {
    background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
    border: 1.5px solid #FCA5A5;
    color: #991B1B;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-bottom: 1.75rem;
}

/* Metric Pill / Bar */
.metric-container {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 1.1rem;
    margin-bottom: 0.75rem;
}

.metric-bar-bg {
    background: #E2E8F0;
    border-radius: 9999px;
    height: 10px;
    width: 100%;
    overflow: hidden;
    margin-top: 0.5rem;
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

/* Action Checklist Card */
.recommendation-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-left: 4px solid #4F46E5;
    border-radius: 12px;
    padding: 1.25rem 1.4rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
}

.priority-tag {
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    background: #EEF2FF;
    color: #4F46E5;
    padding: 0.2rem 0.55rem;
    border-radius: 4px;
    margin-bottom: 0.4rem;
}

/* Review Accordion Cards */
.review-card-correct {
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-radius: 12px;
    padding: 1.15rem;
    margin-bottom: 0.85rem;
}

.review-card-incorrect {
    background: #FEF2F2;
    border: 1px solid #FECACA;
    border-radius: 12px;
    padding: 1.15rem;
    margin-bottom: 0.85rem;
}

/* Streamlit Button Overrides */
div.stButton > button:first-child {
    background-color: #4F46E5 !important;
    color: #FFFFFF !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 0.65rem 1.5rem !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    box-shadow: 0 2px 4px -1px rgba(79, 70, 229, 0.25) !important;
    transition: all 0.15s ease-in-out !important;
}

div.stButton > button:first-child:hover {
    background-color: #4338CA !important;
    box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.35) !important;
    transform: translateY(-1px) !important;
}

/* Secondary Button style for previous/back buttons */
.secondary-btn div.stButton > button:first-child {
    background-color: #F1F5F9 !important;
    color: #334155 !important;
    border: 1px solid #CBD5E1 !important;
    box-shadow: none !important;
}

.secondary-btn div.stButton > button:first-child:hover {
    background-color: #E2E8F0 !important;
    color: #0F172A !important;
}

/* Radio button styling */
div[data-testid="stRadio"] > div {
    gap: 0.65rem;
}

div[data-testid="stRadio"] label {
    background: #FFFFFF;
    border: 1.5px solid #E2E8F0;
    border-radius: 10px;
    padding: 0.75rem 1.1rem;
    font-size: 0.95rem;
    font-weight: 500;
    color: #1E293B;
    transition: all 0.15s ease;
    cursor: pointer;
}

div[data-testid="stRadio"] label:hover {
    border-color: #818CF8;
    background-color: #F8FAFC;
}

/* Progress bar styling */
.stProgress > div > div > div > div {
    background-color: #4F46E5 !important;
}
</style>
"""
