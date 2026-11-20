# 🇩🇪 Am I Exam-Ready? (A1 German Readiness Check)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Tests Passing](https://img.shields.io/badge/tests-74%20passed-brightgreen.svg)]()
[![Groq Powered](https://img.shields.io/badge/Groq%20LLM-Llama%203.3%20%7C%203.1-orange.svg)](https://groq.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, responsive, 100% client-side web application designed to help A1 German learners objectively assess whether they are prepared to book and pass the **Goethe-Zertifikat A1: Start Deutsch 1** or **ÖSD Zertifikat A1** exam without risking expensive exam registration fees (~€100–€180). Now enhanced with high-speed **Groq LLM** AI coaching (Llama 3.3 70B & Llama 3.1 8B).

---

## 🌟 Key Features

- **Official Exam Calibration**: 12 authentic A1 multiple-choice questions aligned with Goethe-Institut (*Start Deutsch 1*) and ÖSD test standards.
- **🤖 Groq LLM AI Exam Coach & Study Planner**:
  - **✨ Personalized 7-Day Study Blueprint**: Groq analyzes your exact diagnostic score, tier, and missed questions to generate a customized, day-by-day practice roadmap with memorable German mnemonics (*Eselsbrücken*).
  - **🔍 Question-by-Question Deep Dive**: On-demand pedagogical breakdown for any question with grammatical explanations, distractor analysis, and natural practice sentences.
  - **💬 Interactive German Coach**: Real-time Q&A assistant in the sidebar to clarify grammar rules (*der/die/das*, *am/um/im*, *Akkusativ*, etc.) with ultra-low latency.
- **3 Core Diagnostic Pillars**:
  - 📚 **Vocabulary (4 Qs)**: Food, everyday shopping, city directions, clock times, professions.
  - 🧩 **Grammar (4 Qs)**: Articles (*der/die/das* & accusative), verb conjugation, temporal prepositions (*am/um/im*), negation (*nicht/kein*).
  - 📖 **Reading (4 Qs)**: Authentic German signs, emails, Deutsche Bahn train timetables, and classified ads.
- **Goethe/ÖSD 60% Benchmark + Safety Buffer**:
  - **Ready to Book (Green)**: Overall $\ge 80\%$ **AND** every individual skill $\ge 60\%$.
  - **Almost Ready (Amber)**: Overall $65\% - 79\%$, **OR** overall $\ge 80\%$ with one skill $< 60\%$ (safety rule prevents false confidence when a critical skill fails).
  - **Not Ready Yet (Red)**: Overall $< 65\%$.
- **Personalized Action Checklist**: Dynamically generates 2–3 actionable, high-yield practice cards based on exact missed subtopics (or 2 exam-day strategy tips if 100%).
- **Bilingual Explanation Switcher**: Toggle explanations seamlessly between **🇬🇧 English** and **🇩🇪 Deutsch** inside the review drawer for low-stress learning.
- **Historical Test Reviews (Zero Login / Mock Data)**: Review past exam diagnostic attempts with progression metrics (Baseline 41.7% → Mid-Prep 66.7% → Recent 83.3%), full question breakdowns, and teacher notes without requiring an account.
- **One-Click Windows Launcher**:
  - Double-click `run_app.bat` to launch the application instantly at `http://localhost:8501`.
- **Modern Pastel Mobile UI**: Beautiful ed-tech aesthetic matching the pastel card design system (sage green, coral pink, warm butter) with dark obsidian pill buttons.

---

## 🗂️ Project & Phase Architecture

```
am_i_ready/
├── run_app.bat                        # One-click Windows launcher for Streamlit app
├── app.py                             # Main Streamlit web application
├── requirements.txt                   # Production dependencies (streamlit>=1.35.0)
├── .streamlit/
│   └── config.toml                    # Theme design tokens & server configuration
├── src/
│   └── styles.py                      # Ed-tech design system & custom CSS
├── data/
│   ├── questions.py                   # 12 authentic A1 German exam questions
│   └── history.py                     # Historical attempts & mock diagnostic data
├── utils/
│   └── readiness.py                   # Pure scoring logic, tier benchmarks & recommendations
├── phase_1_setup/                     # Phase 1: Environment, design tokens & smoke tests
├── phase_2_question_bank/             # Phase 2: Question bank module & schema tests
├── phase_3_readiness_engine/          # Phase 3: Pure scoring & recommendation engine
├── phase_4_app_interface/             # Phase 4: App Interface & Views
│   ├── views.py                       # Python Streamlit interactive views & navigation guards
│   ├── app.py                         # Standalone runner for Phase 4 interface
│   └── test_phase4.py                 # Interface unit tests
├── phase_5_testing_and_polish/        # Phase 5: End-to-end learner persona integration tests
└── phase_6_streamlit_deployment/      # Phase 6: Deployment guide & pre-flight verification
```

---

## 🚀 Quickstart & Local Execution

### 1. Launch the Application
Double-click `run_app.bat` or run:
```bash
streamlit run app.py
```
The app will launch at `http://localhost:8501`.

### 2. Configure Groq LLM (Optional for AI Tutor & Custom Study Plans)
The app works 100% offline out-of-the-box for scoring and diagnostics. To enable the **Groq AI Tutor & Study Plan Generator**:
1. Get a free API key at [console.groq.com/keys](https://console.groq.com/keys).
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Set your API key in `.env`:
   ```env
   GROQ_API_KEY=gsk_your_groq_api_key_here
   ```
   *(Alternatively, you can enter your key directly in the app's sidebar during your session, or add it to `.streamlit/secrets.toml`)*
4. **Security**: `.gitignore` is pre-configured to strictly ignore `.env`, `*.env`, `.streamlit/secrets.toml`, and all API key files to protect your credentials.

### 3. Run Automated Tests
```bash
pytest
# 74 passed in ~5.0s
```

---

## ☁️ Deploying to Streamlit Community Cloud (Free)

1. Push this repository to GitHub:
   ```bash
   git init
   git add .
   git commit -m "feat: complete A1 German exam readiness web app"
   git remote add origin https://github.com/<your-username>/am-i-exam-ready.git
   git push -u origin main
   ```
2. Go to **[share.streamlit.io](https://share.streamlit.io)** and sign in with GitHub.
3. Click **"Create app"** and enter:
   - **Repository**: `<your-username>/am-i-exam-ready`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Click **"Deploy!"** — Your app goes live with a free public HTTPS domain (e.g. `https://am-i-exam-ready.streamlit.app`)!

---

## 📊 Diagnostic Scoring Rubric

| Tier | Status | Criteria | Verdict & Recommendation |
| :---: | :---: | :--- | :--- |
| **Ready to Book** | **Green** | Overall $\ge 80\%$ & all skills $\ge 60\%$ | High confidence. Comfortably clears the 60% passing benchmark with optimal safety buffer. Book your exam date. |
| **Almost Ready** | **Amber** | Overall $65\% - 79\%$ OR overall $\ge 80\%$ with one skill $< 60\%$ | Close to passing, but protect your €100–€180 exam fee. Dedicate 1–2 weeks to your focus areas before booking. |
| **Not Ready Yet** | **Red** | Overall $< 65\%$ | High risk of failing. Reinforce core vocabulary and grammar fundamentals before paying the registration fee. |
