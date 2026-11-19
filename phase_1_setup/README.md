# Phase 1: Environment & Project Scaffolding

## Overview
Phase 1 establishes the core runtime foundation, design system, theme tokens, and directory structure for the **"Am I Exam-Ready?"** A1 German readiness diagnostic application.

## Deliverables in Phase 1
1. **Dependencies (`requirements.txt`)**:
   - `streamlit>=1.35.0`
2. **Streamlit Theme Configuration (`.streamlit/config.toml`)**:
   - Primary Accent: `#4F46E5` (Deep Indigo)
   - Background: `#F8FAFC` (Slate 50)
   - Secondary Surface: `#FFFFFF` (Card White)
   - Text Typography: `#0F172A` (Slate 900)
3. **Design System & Custom CSS (`styles.py` / `styles.css`)**:
   - High-trust ed-tech aesthetic.
   - Distinct category badges:
     - **Vocabulary**: Sky/Cyan (`#0284C7`)
     - **Grammar**: Purple/Indigo (`#7C3AED`)
     - **Reading**: Amber (`#D97706`)
   - Semantic readiness states:
     - **Ready to Book**: Emerald (`#10B981`)
     - **Almost Ready**: Amber (`#F59E0B`)
     - **Not Ready Yet**: Rose (`#EF4444`)
   - Responsive cards, custom radio styling, styled German reading passage containers, and smooth progress bars.
4. **Phase 1 Verification Script (`phase_1_setup/app_phase1_demo.py`)**:
   - Demonstrates the brand identity, typography, theme tokens, and component aesthetics.
