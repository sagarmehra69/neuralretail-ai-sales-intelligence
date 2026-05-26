# =========================================================
# NeuralRetail AI Dashboard
# =========================================================

import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NeuralRetail AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# MAIN TITLE
# =========================================================

st.title("🧠 NeuralRetail AI Sales Intelligence")

st.markdown("""
### AI-Powered Retail Forecasting, Customer Intelligence & Inventory Optimization
""")

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Navigation")

st.sidebar.info("""
NeuralRetail AI Platform

Modules:
- Executive Overview
- Demand Forecasting
- Customer Intelligence
- Inventory Intelligence
- MLOps Monitor
""")

# =========================================================
# HOME PAGE CONTENT
# =========================================================

st.markdown("---")

st.subheader("📊 Platform Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Forecast Accuracy", value="78.5%", delta="+4.2%")

with col2:
    st.metric(label="Churn Detection AUC", value="0.91", delta="+0.03")

with col3:
    st.metric(label="Inventory Risk Alerts", value="42", delta="-8")

# =========================================================
# DESCRIPTION
# =========================================================

st.markdown("---")

st.write("""
NeuralRetail AI is a production-style retail intelligence platform that combines:

- 📈 Demand Forecasting
- 👥 Customer Churn Prediction
- 📦 Inventory Intelligence
- ⚙️ MLOps Monitoring
- 🧠 Explainable AI

Built using:
- Streamlit
- XGBoost
- LightGBM
- Prophet
- SHAP
- MLflow
""")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Amdox Technologies Project")
