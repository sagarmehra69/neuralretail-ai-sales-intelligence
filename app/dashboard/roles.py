import streamlit as st


def is_admin():
    return st.session_state.get("username") == "admin"


def is_viewer():
    return st.session_state.get("username") == "viewer"