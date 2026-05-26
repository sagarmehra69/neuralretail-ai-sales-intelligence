# =========================================================
# Customer Intelligence Dashboard
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Customer Intelligence", layout="wide")

# =========================================================
# TITLE
# =========================================================

st.title("👥 Customer Intelligence")

st.markdown("""
AI-powered churn prediction and retention analytics.
""")

# =========================================================
# SIMULATED CUSTOMER DATA
# (Replace later with real churn outputs)
# =========================================================

np.random.seed(42)

customer_count = 500

customer_df = pd.DataFrame(
    {
        "CustomerID": np.arange(1000, 1500),
        "Churn_Probability": np.random.uniform(0, 1, customer_count),
        "Segment": np.random.choice(
            ["Bronze", "Silver", "Gold", "VIP"], customer_count
        ),
        "Recency": np.random.randint(1, 180, customer_count),
        "Frequency": np.random.randint(1, 20, customer_count),
        "Monetary": np.random.randint(100, 5000, customer_count),
    }
)

# =========================================================
# RETENTION ENGINE
# =========================================================


def retention_strategy(row):

    if row["Recency"] > 120:
        return "Win-back Campaign"

    elif row["Frequency"] < 3:
        return "Loyalty Incentive"

    elif row["Monetary"] > 3000:
        return "VIP Retention Offer"

    else:
        return "Personalized Email"


customer_df["Retention_Action"] = customer_df.apply(retention_strategy, axis=1)

# =========================================================
# CHURN LABELS
# =========================================================

customer_df["Risk_Level"] = pd.cut(
    customer_df["Churn_Probability"],
    bins=[0, 0.4, 0.7, 1],
    labels=["Low Risk", "Medium Risk", "High Risk"],
)

# =========================================================
# KPI SECTION
# =========================================================

st.markdown("## 📌 Churn Intelligence KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Churn Rate", "18.4%", "-2.1%")

with col2:
    st.metric("High-Risk Customers", "94", "-8")

with col3:
    st.metric("ROC-AUC", "0.91", "+0.03")

with col4:
    st.metric("Precision@20%", "87%", "+5%")

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("Customer Filters")

selected_segment = st.sidebar.selectbox(
    "Customer Segment", ["All", "Bronze", "Silver", "Gold", "VIP"]
)

# =========================================================
# FILTER LOGIC
# =========================================================

filtered_df = customer_df.copy()

if selected_segment != "All":
    filtered_df = filtered_df[filtered_df["Segment"] == selected_segment]

# =========================================================
# CHURN DISTRIBUTION
# =========================================================

st.markdown("---")

st.subheader("📊 Churn Risk Distribution")

risk_counts = filtered_df["Risk_Level"].value_counts().reset_index()

risk_counts.columns = ["Risk_Level", "Customers"]

fig_risk = px.pie(risk_counts, names="Risk_Level", values="Customers", hole=0.4)

st.plotly_chart(fig_risk, use_container_width=True)

# =========================================================
# SHAP FEATURE IMPORTANCE
# =========================================================

st.markdown("---")

st.subheader("🧠 SHAP Feature Importance")

shap_df = pd.DataFrame(
    {
        "Feature": [
            "Recency",
            "Frequency",
            "Monetary",
            "Avg Purchase",
            "Customer Tenure",
        ],
        "Importance": [0.42, 0.24, 0.16, 0.11, 0.07],
    }
)

fig_shap = px.bar(
    shap_df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Top Features Driving Churn",
)

st.plotly_chart(fig_shap, use_container_width=True)

# =========================================================
# HIGH-RISK CUSTOMERS
# =========================================================

st.markdown("---")

st.subheader("🚨 High-Risk Customers")

high_risk_df = filtered_df[filtered_df["Churn_Probability"] > 0.7]

st.dataframe(
    high_risk_df[["CustomerID", "Churn_Probability", "Segment", "Retention_Action"]],
    use_container_width=True,
)

# =========================================================
# CUSTOMER SEGMENT ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("🏷️ Segment-Level Churn Analysis")

segment_analysis = (
    filtered_df.groupby("Segment")["Churn_Probability"].mean().reset_index()
)

fig_segment = px.bar(
    segment_analysis,
    x="Segment",
    y="Churn_Probability",
    title="Average Churn Probability by Segment",
)

st.plotly_chart(fig_segment, use_container_width=True)

# =========================================================
# RETENTION ACTION DISTRIBUTION
# =========================================================

st.markdown("---")

st.subheader("🎯 Retention Recommendation Distribution")

action_counts = filtered_df["Retention_Action"].value_counts().reset_index()

action_counts.columns = ["Action", "Count"]

fig_action = px.bar(
    action_counts, x="Action", y="Count", title="Recommended Retention Strategies"
)

st.plotly_chart(fig_action, use_container_width=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Customer Intelligence Module")
