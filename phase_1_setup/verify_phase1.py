"""
verify_phase1.py - Automated verification for Phase 1 setup
"""

import sys
import os

def test_phase1():
    print("Running Phase 1 Verification Checks...")
    
    # Check 1: Streamlit import
    try:
        import streamlit
        print(f"✓ Streamlit successfully imported (version: {streamlit.__version__})")
    except ImportError as e:
        print(f"✗ Streamlit import failed: {e}")
        return False

    # Check 2: Configuration files existence
    expected_files = [
        "requirements.txt",
        ".streamlit/config.toml",
        ".gitignore",
        "phase_1_setup/styles.py",
        "phase_1_setup/README.md",
        "phase_1_setup/app_phase1_demo.py",
        "phase_2_question_bank/README.md",
        "phase_3_readiness_engine/README.md",
        "phase_4_app_interface/README.md",
        "phase_5_testing_and_polish/README.md",
        "phase_6_streamlit_deployment/README.md",
    ]

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    all_found = True
    for rel_path in expected_files:
        full_path = os.path.join(base_dir, rel_path)
        if os.path.exists(full_path):
            print(f"✓ File exists: {rel_path}")
        else:
            print(f"✗ Missing file: {rel_path}")
            all_found = False

    # Check 3: Verify styles module imports without syntax error
    sys.path.insert(0, os.path.join(base_dir, "phase_1_setup"))
    try:
        from styles import CUSTOM_CSS
        assert len(CUSTOM_CSS) > 500
        print(f"✓ Custom CSS design system loaded successfully ({len(CUSTOM_CSS)} characters)")
    except Exception as e:
        print(f"✗ Styles import failed: {e}")
        return False

    if all_found:
        print("\n===> Phase 1 Verification PASSED: All folders, configs, and design system ready!")
        return True
    else:
        print("\n===> Phase 1 Verification FAILED: Some files missing.")
        return False

if __name__ == "__main__":
    success = test_phase1()
    sys.exit(0 if success else 1)
