"""
test_phase1.py - Unit test suite for Phase 1 Setup & Scaffolding
Tests environment, config.toml, CSS design tokens, phase directory structure,
and syntax/structure of app_phase1_demo.py.
"""

import os
import sys
import ast
import pytest
from pathlib import Path

# Add project root and phase_1_setup to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "phase_1_setup"))


class TestEnvironmentAndDependencies:
    """Verify runtime environment and dependency definitions."""

    def test_python_version(self):
        """Python runtime must be >= 3.10."""
        assert sys.version_info >= (3, 10), f"Expected Python >= 3.10, got {sys.version}"

    def test_streamlit_installation(self):
        """Streamlit must be installed and version >= 1.35.0."""
        import streamlit as st
        from packaging import version
        assert version.parse(st.__version__) >= version.parse("1.35.0"), (
            f"Expected streamlit >= 1.35.0, got {st.__version__}"
        )

    def test_requirements_file_exists_and_valid(self):
        """requirements.txt must exist and declare streamlit."""
        req_file = BASE_DIR / "requirements.txt"
        assert req_file.exists(), "requirements.txt does not exist in root directory"
        content = req_file.read_text(encoding="utf-8")
        assert "streamlit" in content.lower(), "requirements.txt must include streamlit"

    def test_gitignore_exists(self):
        """.gitignore must exist and ignore cache & virtual environments."""
        gi_file = BASE_DIR / ".gitignore"
        assert gi_file.exists(), ".gitignore does not exist"
        content = gi_file.read_text(encoding="utf-8")
        assert "__pycache__" in content
        assert ".venv" in content or "venv" in content


class TestThemeConfiguration:
    """Verify Streamlit .streamlit/config.toml tokens."""

    @pytest.fixture
    def config_data(self):
        config_path = BASE_DIR / ".streamlit" / "config.toml"
        assert config_path.exists(), ".streamlit/config.toml does not exist"
        try:
            import toml
            with open(config_path, "r", encoding="utf-8") as f:
                return toml.load(f)
        except ImportError:
            import tomllib
            with open(config_path, "rb") as f:
                return tomllib.load(f)

    def test_theme_keys_and_values(self, config_data):
        """Theme section must declare the exact brand palette tokens."""
        assert "theme" in config_data, "config.toml missing [theme] section"
        theme = config_data["theme"]
        assert theme.get("primaryColor") == "#4F46E5", "Primary color should be Indigo 600 (#4F46E5)"
        assert theme.get("backgroundColor") == "#F8FAFC", "Background color should be Slate 50 (#F8FAFC)"
        assert theme.get("secondaryBackgroundColor") == "#FFFFFF", "Secondary surface should be White (#FFFFFF)"
        assert theme.get("textColor") == "#0F172A", "Text color should be Slate 900 (#0F172A)"
        assert theme.get("font") == "sans serif"

    def test_server_and_browser_settings(self, config_data):
        """Server must be configured for headless deployment and privacy."""
        assert "server" in config_data, "config.toml missing [server] section"
        assert config_data["server"].get("headless") is True
        assert "browser" in config_data, "config.toml missing [browser] section"
        assert config_data["browser"].get("gatherUsageStats") is False


class TestDesignSystemStyles:
    """Verify CSS styling classes and brand color tokens in styles.py."""

    @pytest.fixture
    def custom_css(self):
        from styles import CUSTOM_CSS
        return CUSTOM_CSS

    def test_css_structure(self, custom_css):
        """CSS must be enclosed in valid style tags and be substantial."""
        assert isinstance(custom_css, str)
        assert custom_css.strip().startswith("<style>")
        assert custom_css.strip().endswith("</style>")
        assert len(custom_css) > 1000

    def test_required_component_selectors(self, custom_css):
        """Verify presence of all custom UI component classes."""
        required_selectors = [
            ".de-accent-bar",
            ".badge-pill",
            ".badge-vocabulary",
            ".badge-grammar",
            ".badge-reading",
            ".badge-subtopic",
            ".authority-pill",
            ".ed-card",
            ".reading-passage-box",
            ".reading-passage-header",
            ".reading-passage-content",
            ".verdict-ready",
            ".verdict-almost",
            ".verdict-not-ready",
            ".metric-container",
            ".metric-bar-bg",
            ".metric-bar-fill-emerald",
            ".metric-bar-fill-amber",
            ".metric-bar-fill-rose",
            ".recommendation-card",
            ".priority-tag",
            ".review-card-correct",
            ".review-card-incorrect",
            "div.stButton",
            "div[data-testid=\"stRadio\"]"
        ]
        for selector in required_selectors:
            assert selector in custom_css, f"Missing required CSS selector: {selector}"

    def test_brand_color_tokens(self, custom_css):
        """Verify presence of key brand colors in CSS."""
        brand_colors = [
            "#4F46E5",  # Indigo primary
            "#0369A1",  # Vocabulary blue
            "#6D28D9",  # Grammar purple
            "#B45309",  # Reading amber
            "#10B981",  # Emerald ready
            "#EF4444",  # Rose not ready
        ]
        for color in brand_colors:
            assert color in custom_css, f"Missing brand color token {color} in CUSTOM_CSS"


class TestPhaseDirectories:
    """Verify all 6 phase directories exist and contain documentation."""

    @pytest.mark.parametrize("phase_dir", [
        "phase_1_setup",
        "phase_2_question_bank",
        "phase_3_readiness_engine",
        "phase_4_app_interface",
        "phase_5_testing_and_polish",
        "phase_6_streamlit_deployment"
    ])
    def test_phase_folder_and_readme_exist(self, phase_dir):
        folder = BASE_DIR / phase_dir
        assert folder.exists() and folder.is_dir(), f"Phase folder missing: {phase_dir}"
        readme = folder / "README.md"
        assert readme.exists(), f"Phase folder missing README.md: {phase_dir}"
        assert len(readme.read_text(encoding="utf-8").strip()) > 50


class TestAppPhase1DemoSyntaxAndImports:
    """Validate app_phase1_demo.py syntax and AST integrity."""

    def test_demo_app_syntax(self):
        """Verify app_phase1_demo.py parses as valid Python code without syntax errors."""
        demo_file = BASE_DIR / "phase_1_setup" / "app_phase1_demo.py"
        assert demo_file.exists()
        source = demo_file.read_text(encoding="utf-8")
        parsed_ast = ast.parse(source)
        assert isinstance(parsed_ast, ast.Module)

    def test_demo_app_imports_and_structure(self):
        """Verify demo script imports streamlit and styles."""
        demo_file = BASE_DIR / "phase_1_setup" / "app_phase1_demo.py"
        source = demo_file.read_text(encoding="utf-8")
        assert "import streamlit as st" in source
        assert "from styles import CUSTOM_CSS" in source
        assert "st.set_page_config" in source
        assert "Am I ready for my A1 German exam?" in source
