# 🇩🇪 Am I Exam-Ready? (A1 German Readiness Check)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Tests Passing](https://img.shields.io/badge/tests-59%20passed-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, responsive, 100% client-side web application designed to help A1 German learners objectively assess whether they are prepared to book and pass the **Goethe-Zertifikat A1: Start Deutsch 1** or **ÖSD Zertifikat A1** exam without risking expensive exam registration fees (~€100–€180).

---

## 🌟 Key Features

- **Official Exam Calibration**: 12 authentic A1 multiple-choice questions aligned with Goethe-Institut (*Start Deutsch 1*) and ÖSD test standards.
- **3 Core Diagnostic Pillars**:
  - 📚 **Vocabulary (4 Qs)**: Food, everyday shopping, city directions, clock times, professions.
  - 🧩 **Grammar (4 Qs)**: Articles (*der/die/das* & accusative), verb conjugation, temporal prepositions (*am/um/im*), negation (*nicht/kein*).
  - 📖 **Reading (4 Qs)**: Authentic German signs, emails, Deutsche Bahn train timetables, and classified ads.
- **Goethe/ÖSD 60% Benchmark + Safety Buffer**:
  - **Ready to Book (Green)**: Overall $\ge 80\%$ **AND** every individual skill $\ge 60\%$.
  - **Almost Ready (Amber)**: Overall $65\% - 79\%$, **OR** overall $\ge 80\%$ with one skill $< 60\%$ (safety rule prevents false confidence when a critical skill fails).
  - **Not Ready Yet (Red)**: Overall $< 65\%$.
- **Personalized Action Checklist**: Dynamically generates 2–3 actionable, high-yield practice cards based on exact missed subtopics (or 2 exam-day strategy tips if 100%).
- **Interactive Answer Review**: Expandable question-by-question review drawer with user choice, correct answer, and full grammatical explanations.
- **Ed-Tech Aesthetic**: Clean slate-50 background, deep indigo primary accent, and semantic indicators.

---

## 🗂️ Project & Phase Architecture

```
am_i_ready/
├── app.py                             # Main Streamlit web application
├── requirements.txt                   # Production dependencies (streamlit>=1.35.0)
├── .streamlit/
│   └── config.toml                    # Theme design tokens & server configuration
├── src/
│   └── styles.py                      # Ed-tech design system & custom CSS
├── data/
│   └── questions.py                   # 12 authentic A1 German exam questions
├── utils/
│   └── readiness.py                   # Pure scoring logic, tier benchmarks & recommendations
├── phase_1_setup/                     # Phase 1: Environment, design tokens & smoke tests
├── phase_2_question_bank/             # Phase 2: Question bank module & schema tests
├── phase_3_readiness_engine/          # Phase 3: Pure scoring & recommendation engine
├── phase_4_app_interface/             # Phase 4: Streamlit interactive views & navigation guards
├── phase_5_testing_and_polish/        # Phase 5: End-to-end learner persona integration tests
└── phase_6_streamlit_deployment/      # Phase 6: Deployment guide & pre-flight verification
```

---

## 🚀 Quickstart & Local Execution

### 1. Clone & Install
```bash
git clone https://github.com/<your-username>/am-i-exam-ready.git
cd am-i-exam-ready
pip install -r requirements.txt
```

### 2. Run the App Locally
```bash
streamlit run app.py
```
The app will launch at `http://localhost:8501`.

### 3. Run Automated Tests
```bash
pytest
# 59 passed in ~0.9s
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
