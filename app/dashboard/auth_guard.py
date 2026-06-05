import streamlit as st


def check_auth():

    if (
        "authentication_status" not in st.session_state
        or st.session_state["authentication_status"] is not True
    ):

        st.warning("Please login first")
        st.stop()