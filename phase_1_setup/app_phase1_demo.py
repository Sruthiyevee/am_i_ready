"""
app_phase1_demo.py - Phase 1 Verification Demo
Tests Streamlit environment, theme configuration, custom CSS, and brand design system.
"""

import streamlit as st
from styles import CUSTOM_CSS

st.set_page_config(
    page_title="Phase 1 Verification: Am I Exam-Ready?",
    page_icon="🇩🇪",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Inject modern ed-tech design system
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Header & Authority Ribbon
st.markdown("""
<div class="de-accent-bar">
    <div class="bar-black"></div>
    <div class="bar-red"></div>
    <div class="bar-gold"></div>
</div>
<div class="authority-pill">
    <span>🇩🇪</span> Goethe-Zertifikat A1 & ÖSD A1 Diagnostic Standard
</div>
""", unsafe_allow_html=True)

st.title("Am I ready for my A1 German exam?")
st.write(
    "Phase 1 Verification: Environment initialized with Streamlit, custom design tokens, "
    "and ed-tech styling."
)

# Demo Card displaying category badges and design tokens
st.markdown("""
<div class="ed-card">
    <h3 style="margin-top:0; color:#0F172A; font-size:1.25rem; font-weight:700;">Design System & Theme Tokens</h3>
    <p style="color:#475569; font-size:0.95rem; margin-bottom:1.25rem;">
        The three diagnostic pillars evaluated in the 12-question readiness check:
    </p>
    <div style="display:flex; flex-wrap:wrap; gap:0.75rem; margin-bottom:1.5rem;">
        <span class="badge-pill badge-vocabulary">📚 Vocabulary (4 Qs)</span>
        <span class="badge-pill badge-grammar">🧩 Grammar (4 Qs)</span>
        <span class="badge-pill badge-reading">📖 Reading (4 Qs)</span>
    </div>
    
    <div style="margin-top:1rem;">
        <span class="badge-subtopic">Sample Subtopic: Articles (der/die/das)</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Demo German Reading Passage Card
st.markdown("""
<div class="reading-passage-box">
    <div class="reading-passage-header">A1 Leseverstehen Kontext (Authentic Notice)</div>
    <div class="reading-passage-content">
<strong>Bäckerei Schmidt — Öffnungszeiten</strong><br>
Montag bis Freitag: 06:30 – 18:30 Uhr<br>
Samstag: 07:00 – 13:00 Uhr<br>
Sonn- und Feiertage: Geschlossen
    </div>
</div>
""", unsafe_allow_html=True)

# Test Button
if st.button("✓ Phase 1 Environment Verified", use_container_width=True):
    st.success("Phase 1 verified! Runtime, dependencies, and styling tokens are active.")
