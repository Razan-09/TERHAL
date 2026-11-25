"""Shared helpers used by every page.

Paths are built from this file's location, so they work no matter which
folder Streamlit is started from (locally or on Streamlit Cloud).
"""
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
STYLES_DIR = BASE_DIR / "styles"
IMAGES_DIR = BASE_DIR / "images"


def load_css(file_name):
    """Inject a CSS file from the styles/ folder."""
    css = (STYLES_DIR / file_name).read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def image_path(file_name):
    """Full path of an image in images/, or None if the file is missing."""
    if not file_name:
        return None
    path = IMAGES_DIR / file_name
    return str(path) if path.exists() else None


def show_image(file_name):
    """Show an image only if it exists (a missing image never crashes the app)."""
    path = image_path(file_name)
    if path:
        st.image(path, use_container_width=True)
    return path is not None


def require_login():
    """Send visitors who are not logged in back to the login page."""
    if not st.session_state.get("logged_in"):
        st.switch_page("app.py")
