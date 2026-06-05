# =========================================================
# NeuralRetail AI — MLOps Monitoring Center
# Amdox Technologies
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from auth_guard import check_auth
from utils.theme import load_css
from utils.chart_theme import apply_dark_theme

load_css()
check_auth()


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="MLOps Monitor",
    layout="wide"
)



# =========================================================
# PAGE TITLE
# =========================================================

st.title("⚙️ MLOps Monitoring Center")

st.markdown("""
Production monitoring, model governance, experiment tracking,
and AI infrastructure intelligence.
""")

# =========================================================
# MODEL PERFORMANCE DATA
# =========================================================

model_df = pd.DataFrame({
    "Model": [
        "XGBoost Forecast",
        "Prophet Forecast",
        "Ensemble Forecast",
        "Churn Classifier",
        "Inventory Risk Model"
    ],

    "Metric": [
        "MAPE",
        "MAPE",
        "MAPE",
        "ROC-AUC",
        "Accuracy"
    ],

    "Score": [
        21.45,
        30.75,
        18.20,
        0.91,
        0.87
    ]
})

# =========================================================
# SYSTEM HEALTH KPIs
# =========================================================

st.markdown("## 📌 AI System Health")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "🤖 Active Models",
        "5"
    )

with col2:
    st.metric(
        "📂 MLflow Runs",
        "42",
        "+5"
    )

with col3:
    st.metric(
        "🔄 Last Retraining",
        "2 Days Ago"
    )

with col4:
    st.metric(
        "⚠️ Drift Alerts",
        "1",
        "-2"
    )

with col5:
    st.metric(
        "🟢 Uptime",
        "99.2%"
    )

# =========================================================
# MODEL PERFORMANCE OVERVIEW
# =========================================================

st.markdown("---")

st.subheader("📊 Model Performance Overview")

fig_models = px.bar(
    model_df,
    x="Model",
    y="Score",
    color="Metric",
    text_auto=".2f",
    color_discrete_sequence=[
        "#F97316",
        "#EA580C",
        "#FB923C"
    ],
    title="Production Model Performance"
)

fig_models.update_layout(
    height=550,
    xaxis_title="Models",
    yaxis_title="Performance Score"
)

fig_models = apply_dark_theme(fig_models)

st.plotly_chart(
    fig_models,
    use_container_width=True
)

# =========================================================
# FEATURE DRIFT MONITORING
# =========================================================

st.markdown("---")

st.subheader("🧠 Feature Drift Monitoring")

drift_df = pd.DataFrame({
    "Feature": [
        "Sales",
        "Recency",
        "Frequency",
        "Inventory",
        "Demand",
        "Revenue",
        "Customer Value"
    ],

    "Drift_Score": [
        0.12,
        0.08,
        0.04,
        0.16,
        0.09,
        0.13,
        0.05
    ]
})

fig_drift = px.bar(
    drift_df,
    x="Feature",
    y="Drift_Score",
    color="Drift_Score",
    text_auto=".2f",
    color_continuous_scale=[
        "#22C55E",
        "#F59E0B",
        "#DC2626"
    ],
    title="Feature Drift Detection"
)

fig_drift.update_layout(
    height=500,
    coloraxis_showscale=False
)

fig_drift = apply_dark_theme(fig_drift)

st.plotly_chart(
    fig_drift,
    use_container_width=True
)

# =========================================================
# MODEL STABILITY SCORE
# =========================================================

st.markdown("---")

st.subheader("📈 AI Stability Monitoring")

stability_df = pd.DataFrame({
    "Environment": [
        "Forecast API",
        "Churn Engine",
        "Inventory Engine",
        "Recommendation Engine",
        "MLflow Tracking"
    ],

    "Stability": [
        98,
        97,
        94,
        96,
        99
    ]
})

fig_stability = px.line(
    stability_df,
    x="Environment",
    y="Stability",
    markers=True,
    title="Operational Stability Score"
)

fig_stability.update_traces(
    line=dict(
        width=4,
        color="#F97316"
    ),
    marker=dict(
        size=10
    )
)

fig_stability.update_layout(
    height=500,
    yaxis_range=[85, 100]
)

fig_stability = apply_dark_theme(fig_stability)

st.plotly_chart(
    fig_stability,
    use_container_width=True
)

# =========================================================
# SYSTEM STATUS
# =========================================================

st.markdown("---")

st.subheader("🖥️ Infrastructure Status")

system_df = pd.DataFrame({
    "Service": [
        "Forecast API",
        "Churn Engine",
        "Inventory Engine",
        "MLflow Tracking",
        "Dashboard Server",
        "Recommendation Engine"
    ],

    "Status": [
        "Online",
        "Online",
        "Online",
        "Online",
        "Online",
        "Online"
    ],

    "Latency_ms": [
        121,
        98,
        143,
        75,
        64,
        132
    ]
})

fig_system = px.bar(
    system_df,
    x="Service",
    y="Latency_ms",
    color="Latency_ms",
    text_auto=True,
    color_continuous_scale=[
        "#22C55E",
        "#F59E0B",
        "#DC2626"
    ],
    title="Infrastructure Latency Monitoring"
)

fig_system.update_layout(
    height=550,
    coloraxis_showscale=False
)

fig_system = apply_dark_theme(fig_system)

st.plotly_chart(
    fig_system,
    use_container_width=True
)

# =========================================================
# MLFLOW EXPERIMENT TRACKING
# =========================================================

st.markdown("---")

st.subheader("📂 MLflow Experiment Tracking")

mlflow_df = pd.DataFrame({
    "Run_ID": [
        "RUN_001",
        "RUN_002",
        "RUN_003",
        "RUN_004",
        "RUN_005"
    ],

    "Model": [
        "XGBoost",
        "Prophet",
        "LightGBM",
        "Ensemble",
        "CatBoost"
    ],

    "Metric": [
        21.45,
        30.75,
        19.60,
        18.20,
        20.14
    ],

    "Status": [
        "Completed",
        "Completed",
        "Completed",
        "Production",
        "Testing"
    ]
})

st.dataframe(
    mlflow_df,
    use_container_width=True,
    height=350
)

# =========================================================
# RETRAINING PIPELINE
# =========================================================

st.markdown("---")

st.subheader("🔄 Retraining Pipeline Schedule")

schedule_df = pd.DataFrame({
    "Model": [
        "Forecast Model",
        "Churn Model",
        "Inventory Model",
        "Recommendation Engine"
    ],

    "Next_Retrain": [
        "2026-06-01",
        "2026-06-05",
        "2026-06-08",
        "2026-06-12"
    ],

    "Frequency": [
        "Weekly",
        "Bi-Weekly",
        "Weekly",
        "Monthly"
    ]
})

st.dataframe(
    schedule_df,
    use_container_width=True,
    height=300
)

# =========================================================
# LIVE SYSTEM LOGS
# =========================================================

st.markdown("---")

st.subheader("📜 Live System Logs")

logs = [
    "[INFO] Forecast pipeline executed successfully.",
    "[INFO] Churn predictions generated.",
    "[WARNING] Minor drift detected in Inventory feature set.",
    "[INFO] MLflow experiment logged.",
    "[INFO] Dashboard services synchronized.",
    "[INFO] Recommendation engine latency optimized.",
    "[SUCCESS] Automated retraining completed."
]

for log in logs:
    st.code(log)

# =========================================================
# AI GOVERNANCE INSIGHTS
# =========================================================

st.markdown("---")

st.subheader("🧠 AI Governance Insights")

best_model = (
    model_df
    .sort_values(
        by="Score",
        ascending=False
    )
    .iloc[0]["Model"]
)

highest_drift = (
    drift_df
    .sort_values(
        by="Drift_Score",
        ascending=False
    )
    .iloc[0]["Feature"]
)

st.info(f"""
• Best performing production model: {best_model}

• Highest feature drift detected in: {highest_drift}

• All critical AI infrastructure services operational

• Automated retraining pipelines functioning normally

• MLOps governance system active and stable
""")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "NeuralRetail AI • MLOps Monitoring Center • Amdox Technologies"
)
