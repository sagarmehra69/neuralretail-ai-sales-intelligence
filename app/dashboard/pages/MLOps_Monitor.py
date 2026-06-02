# =========================================================
# MLOps Monitoring Dashboard
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from utils.theme import load_css
from utils.loader import load_model_metrics

# =========================================================
# PAGE CONFIG
# =========================================================

load_css()
st.set_page_config(page_title="MLOps Monitor", layout="wide")

# =========================================================
# TITLE
# =========================================================

st.title("⚙️ MLOps Monitoring")

st.markdown("""
Production monitoring, experiment tracking, and AI system health.
""")

# =========================================================
# MODEL PERFORMANCE DATA
# =========================================================

model_df = pd.DataFrame(
    {
        "Model": [
            "XGBoost Forecast",
            "Prophet Forecast",
            "Ensemble Forecast",
            "Churn Classifier",
            "Inventory Risk Model",
        ],
        "Metric": ["MAPE", "MAPE", "MAPE", "ROC-AUC", "Accuracy"],
        "Score": [21.45, 30.75, 18.20, 0.91, 0.87],
    }
)

# =========================================================
# KPI SECTION
# =========================================================

st.markdown("## 📌 System Health KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Models Active", "5")

with col2:
    st.metric("MLflow Runs", "42", "+5")

with col3:
    st.metric("Last Retraining", "2 Days Ago")

with col4:
    st.metric("Drift Alerts", "1", "-2")

# =========================================================
# MODEL PERFORMANCE TABLE
# =========================================================

st.markdown("---")

st.subheader("📊 Model Performance Metrics")

st.dataframe(model_df, use_container_width=True)

# =========================================================
# MODEL PERFORMANCE CHART
# =========================================================

fig_models = px.bar(
    model_df, x="Model", y="Score", color="Metric", title="Model Performance Overview"
)

st.plotly_chart(fig_models, use_container_width=True)

# =========================================================
# DATA DRIFT MONITORING
# =========================================================

st.markdown("---")

st.subheader("🧠 Feature Drift Monitoring")

drift_df = pd.DataFrame(
    {
        "Feature": ["Sales", "Recency", "Frequency", "Inventory", "Demand"],
        "Drift_Score": [0.12, 0.08, 0.04, 0.16, 0.09],
    }
)

fig_drift = px.bar(
    drift_df, x="Feature", y="Drift_Score", title="Feature Drift Detection"
)

st.plotly_chart(fig_drift, use_container_width=True)

# =========================================================
# SYSTEM STATUS
# =========================================================

st.markdown("---")

st.subheader("🖥️ System Status")

system_df = pd.DataFrame(
    {
        "Service": [
            "Forecast API",
            "Churn Engine",
            "Inventory Engine",
            "MLflow Tracking",
            "Dashboard Server",
        ],
        "Status": ["Online", "Online", "Online", "Online", "Online"],
    }
)

st.dataframe(system_df, use_container_width=True)

# =========================================================
# MLFLOW EXPERIMENT TRACKING
# =========================================================

st.markdown("---")

st.subheader("📂 MLflow Experiment Tracking")

mlflow_df = pd.DataFrame(
    {
        "Run_ID": ["RUN_001", "RUN_002", "RUN_003", "RUN_004"],
        "Model": ["XGBoost", "Prophet", "LightGBM", "Ensemble"],
        "Metric": [21.45, 30.75, 19.60, 18.20],
    }
)

st.dataframe(mlflow_df, use_container_width=True)

# =========================================================
# RETRAINING SCHEDULE
# =========================================================

st.markdown("---")

st.subheader("🔄 Retraining Schedule")

schedule_df = pd.DataFrame(
    {
        "Model": ["Forecast Model", "Churn Model", "Inventory Model"],
        "Next_Retrain": ["2026-06-01", "2026-06-05", "2026-06-08"],
    }
)

st.dataframe(schedule_df, use_container_width=True)

# =========================================================
# SYSTEM LOGS
# =========================================================

st.markdown("---")

st.subheader("📜 System Logs")

logs = [
    "[INFO] Forecast pipeline completed successfully.",
    "[INFO] Churn predictions generated.",
    "[WARNING] Minor feature drift detected in Inventory.",
    "[INFO] MLflow experiment logged.",
    "[INFO] Dashboard refreshed successfully.",
]

for log in logs:
    st.code(log)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • MLOps Monitoring Module")
