"""
preflight_check.py - Automated Pre-Deployment Verification for Streamlit Cloud
Validates requirements, configs, code compilation, and full test suite before git push.
"""

import sys
import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def check_production_readiness():
    print("=" * 65)
    print("🚀 Streamlit Community Cloud Pre-Flight Deployment Check")
    print("=" * 65)

    checks = []

    # 1. requirements.txt
    req_path = BASE_DIR / "requirements.txt"
    if req_path.exists() and "streamlit" in req_path.read_text(encoding="utf-8").lower():
        print("✓ [1/6] requirements.txt is valid and includes Streamlit.")
        checks.append(True)
    else:
        print("✗ [1/6] requirements.txt missing or invalid.")
        checks.append(False)

    # 2. .streamlit/config.toml
    config_path = BASE_DIR / ".streamlit" / "config.toml"
    if config_path.exists() and "[theme]" in config_path.read_text(encoding="utf-8"):
        print("✓ [2/6] .streamlit/config.toml exists with theme tokens.")
        checks.append(True)
    else:
        print("✗ [2/6] .streamlit/config.toml missing.")
        checks.append(False)

    # 3. app.py compilation
    app_path = BASE_DIR / "app.py"
    try:
        compile(app_path.read_text(encoding="utf-8"), str(app_path), "exec")
        print("✓ [3/6] app.py compiles cleanly without syntax errors.")
        checks.append(True)
    except Exception as e:
        print(f"✗ [3/6] app.py compilation error: {e}")
        checks.append(False)

    # 4. Data Layer & Question Count
    sys.path.insert(0, str(BASE_DIR))
    try:
        from data.questions import QUESTIONS
        assert len(QUESTIONS) == 12
        print(f"✓ [4/6] Question bank verified: {len(QUESTIONS)} authentic A1 questions.")
        checks.append(True)
    except Exception as e:
        print(f"✗ [4/6] Question bank error: {e}")
        checks.append(False)

    # 5. Readiness Engine
    try:
        from utils.readiness import calculate_readiness
        test_res = calculate_readiness({q["id"]: q["correct_answer_index"] for q in QUESTIONS})
        assert test_res["tier"] == "ready"
        print("✓ [5/6] Readiness scoring and recommendation engine verified.")
        checks.append(True)
    except Exception as e:
        print(f"✗ [5/6] Readiness engine error: {e}")
        checks.append(False)

    # 6. Run Full Pytest Suite Across All Phases
    print("\nRunning comprehensive pytest suite across all phases...")
    cmd = [sys.executable, "-m", "pytest", str(BASE_DIR), "-q"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode == 0:
        print(f"✓ [6/6] All pytest tests passed! ({proc.stdout.strip()})")
        checks.append(True)
    else:
        print(f"✗ [6/6] Pytest failures:\n{proc.stdout}\n{proc.stderr}")
        checks.append(False)

    print("=" * 65)
    if all(checks):
        print("🎉 PRE-FLIGHT VERIFICATION PASSED: Ready for Streamlit Cloud deployment!")
        print("=" * 65)
        return True
    else:
        print("❌ PRE-FLIGHT VERIFICATION FAILED: Resolve errors above before deploying.")
        print("=" * 65)
        return False


if __name__ == "__main__":
    success = check_production_readiness()
    sys.exit(0 if success else 1)
