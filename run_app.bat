@echo off
title Am I Exam-Ready? (A1 German Readiness Check)
cd /d "%~dp0"

echo ================================================================
echo    Am I Exam-Ready? (A1 German Diagnostic Application)
echo    Aligned with Goethe-Zertifikat A1 & OESD Zertifikat A1
echo ================================================================
echo.

:: 1. Check if Python is installed
where python >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Python was not found in your system PATH.
    echo Please install Python 3.10+ and ensure "Add Python to PATH" is checked.
    echo.
    pause
    exit /b 1
)

:: 2. Check if Streamlit is installed
python -c "import streamlit" >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [INFO] Streamlit is not installed. Installing required dependencies...
    python -m pip install -r requirements.txt
    if %ERRORLEVEL% neq 0 (
        echo [ERROR] Failed to install dependencies.
        pause
        exit /b 1
    )
)

:: 3. Launch the web application
echo [INFO] Launching Streamlit web application...
echo [INFO] Opening in your default browser at http://localhost:8501
echo [INFO] (Press Ctrl+C in this window anytime to stop the server)
echo.

python -m streamlit run app.py

if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] The application encountered an unexpected issue.
    pause
)
