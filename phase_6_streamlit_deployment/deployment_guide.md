# Phase 6: Streamlit Community Cloud Deployment Guide

This guide walks you through deploying **"Am I Exam-Ready?"** for free to **Streamlit Community Cloud (`share.streamlit.io`)** in less than 2 minutes.

---

## 1. Architecture for Streamlit Cloud

Streamlit Community Cloud connects directly to your GitHub repository and runs `app.py` in an isolated container:

```
┌─────────────────────────────────┐
│     Your GitHub Repository      │
│  https://github.com/<user>/...  │
└────────────────┬────────────────┘
                 │ Webhook on Git Push
                 ▼
┌─────────────────────────────────┐
│    Streamlit Community Cloud    │
│  - Reads requirements.txt       │
│  - Reads .streamlit/config.toml │
│  - Executes app.py              │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│       Live Production URL       │
│  https://<app>.streamlit.app    │
└─────────────────────────────────┘
```

---

## 2. Step-by-Step Deployment Walkthrough

### Step 1: Initialize Git and Commit Your Project
From the project root directory (`e:\Proj\am_i_ready`), run:

```bash
# 1. Initialize git (if not already done)
git init

# 2. Stage all project files
git add .

# 3. Create your initial commit
git commit -m "feat: complete A1 German exam readiness web app"
```

### Step 2: Push to GitHub
1. Go to [GitHub.com](https://github.com) and click **New repository**.
2. Name your repository (e.g., `am-i-exam-ready` or `german-a1-readiness`).
3. Set visibility to **Public** (or Private).
4. Do **not** initialize with a README (you already have one).
5. Link your local repo and push:

```bash
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/am-i-exam-ready.git
git push -u origin main
```

---

### Step 3: Deploy on Streamlit Community Cloud
1. Open [share.streamlit.io](https://share.streamlit.io) and log in with your **GitHub** account.
2. Click the **"Create app"** button in the top right.
3. Select **"I already have an app"**.
4. Configure the 3 fields:
   - **Repository**: `<YOUR_GITHUB_USERNAME>/am-i-exam-ready`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. *(Optional)* Click **"Advanced settings"** to choose your custom URL subdomain (e.g., `am-i-exam-ready.streamlit.app`).
6. Click **"Deploy!"**.

---

### Step 4: Verification & Live Updates
- Streamlit Cloud will install dependencies from `requirements.txt`, load theme tokens from `.streamlit/config.toml`, and spin up the app.
- Once deployed, **any future git commit pushed to `main` will automatically trigger an instant live redeploy!**

---

## 3. Local Execution Before Deploying
To preview the app locally before pushing:

```bash
streamlit run app.py
```
The app will open automatically in your browser at `http://localhost:8501`.
