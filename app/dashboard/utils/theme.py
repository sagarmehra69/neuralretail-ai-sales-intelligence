# =========================================================
# NeuralRetail AI — Global Theme Loader
# Amdox Technologies
# =========================================================

import streamlit as st

from pathlib import Path

# =========================================================
# LOAD GLOBAL CSS
# =========================================================

def load_css():

    try:

        css_path = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "assets"
            / "style.css"
        )

        if not css_path.exists():

            st.error(
                f"CSS file not found: {css_path}"
            )

            return

        with open(
            css_path,
            encoding="utf-8"
        ) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except Exception as e:

        st.error(
            f"Failed to load CSS theme: {e}"
        )