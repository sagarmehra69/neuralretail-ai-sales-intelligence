import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


def authenticate_user():

    with open("auth_config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"]
    )

    authenticator.login()

    if st.session_state["authentication_status"]:

        authenticator.logout("Logout", "sidebar")

        st.sidebar.success(
            f"Welcome {st.session_state['name']}"
        )

        return True

    elif st.session_state["authentication_status"] is False:
        st.error("Incorrect username or password")

    elif st.session_state["authentication_status"] is None:
        st.warning("Please login")

    return False