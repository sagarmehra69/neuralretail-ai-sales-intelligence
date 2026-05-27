import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NeuralRetail AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# LOAD CSS
# =========================================================


def load_css():

    with open("app/dashboard/assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.title("🧠 NeuralRetail AI")

    st.markdown("""
    Enterprise Retail Intelligence Platform
    """)

    st.markdown("---")

    st.subheader("📡 System Status")

    st.success("Forecast Engine Online")

    st.success("Churn Engine Online")

    st.success("Inventory Engine Online")

    st.markdown("---")

    st.subheader("⚙️ Platform Stack")

    st.markdown("""
    - Prophet Forecasting
    - XGBoost Models
    - Churn Prediction
    - Inventory Intelligence
    - Streamlit Dashboard
    - ML Analytics Pipeline
    """)

    st.markdown("---")

    st.caption("Built with AI + Data Science")

# =========================================================
# MAIN PAGE
# =========================================================

st.title("🧠 NeuralRetail AI")

st.markdown("""
Welcome to the enterprise AI retail intelligence platform.

Use the sidebar to navigate between intelligence modules.
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📈 Forecasting Intelligence")

with col2:
    st.info("👥 Customer Intelligence")

with col3:
    st.info("📦 Inventory Intelligence")

st.markdown("---")

st.success("✅ Platform Operational")
