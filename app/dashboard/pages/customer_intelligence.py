# =========================================================
# NeuralRetail AI — Customer Intelligence
# Amdox Technologies
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

from auth_guard import check_auth
from utils.theme import load_css
from utils.loader import load_churn_data
from utils.chart_theme import apply_dark_theme

check_auth()


# =========================================================
# LOAD STYLES
# =========================================================

load_css()

# =========================================================
# PAGE HEADER
# =========================================================

st.title("🧠 Customer Intelligence")

st.markdown("""
Advanced AI-powered customer intelligence platform for segmentation,
churn analysis, retention targeting, and customer value optimization.
""")

# =========================================================
# LOAD DATA
# =========================================================

churn_df = load_churn_data()

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🎯 Customer Filters")

selected_segments = st.sidebar.multiselect(
    "Select Customer Segment",
    options=sorted(churn_df["Segment"].unique()),
    default=sorted(churn_df["Segment"].unique())
)

risk_range = st.sidebar.slider(
    "Churn Probability Range",
    min_value=0.0,
    max_value=1.0,
    value=(0.0, 1.0)
)

filtered_df = churn_df[
    (churn_df["Segment"].isin(selected_segments)) &
    (churn_df["Churn_Probability"] >= risk_range[0]) &
    (churn_df["Churn_Probability"] <= risk_range[1])
]

# =========================================================
# KPI SECTION
# =========================================================

total_customers = filtered_df["CustomerID"].nunique()

high_risk_customers = len(
    filtered_df[
        filtered_df["Churn_Probability"] > 0.7
    ]
)

avg_churn = round(
    filtered_df["Churn_Probability"].mean(),
    2
)

avg_monetary = round(
    filtered_df["Monetary"].mean(),
    2
)

st.markdown("## 📌 Customer KPI Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="👥 Total Customers",
        value=f"{total_customers:,}",
        delta="Customer Base"
    )

with col2:
    st.metric(
        label="🚨 High Risk Customers",
        value=f"{high_risk_customers:,}",
        delta="Retention Required"
    )

with col3:
    st.metric(
        label="📉 Avg Churn Risk",
        value=f"{avg_churn:.2f}",
        delta="ML Prediction"
    )

with col4:
    st.metric(
        label="💰 Avg Customer Value",
        value=f"${avg_monetary:,.0f}",
        delta="Monetary Score"
    )

# =========================================================
# CHURN DISTRIBUTION
# =========================================================

st.markdown("---")

st.subheader("📊 Churn Probability Distribution")

fig1 = px.histogram(
    filtered_df,
    x="Churn_Probability",
    nbins=35,
    color_discrete_sequence=["#F97316"],
    title="Customer Churn Risk Distribution"
)

fig1.update_layout(
    bargap=0.05
)

fig1 = apply_dark_theme(fig1)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =========================================================
# CUSTOMER SEGMENTS
# =========================================================

st.markdown("---")

st.subheader("👥 Customer Segment Distribution")

segment_df = (
    filtered_df["Segment"]
    .value_counts()
    .reset_index()
)

segment_df.columns = [
    "Segment",
    "Customers"
]

fig2 = px.bar(
    segment_df.sort_values("Customers"),
    x="Customers",
    y="Segment",
    orientation="h",
    color="Customers",
    color_continuous_scale=[
        "#F59E0B",
        "#F97316",
        "#EA580C"
    ],
    title="Customer Segments by Size"
)

fig2.update_layout(
    showlegend=False
)

fig2 = apply_dark_theme(fig2)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =========================================================
# RFM ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📈 RFM Customer Analysis")

fig3 = px.scatter(
    filtered_df,
    x="Frequency",
    y="Monetary",
    size="Recency",
    color="Churn_Probability",
    opacity=0.7,
    hover_data=[
        "CustomerID",
        "Segment"
    ],
    color_continuous_scale=[
        "#F59E0B",
        "#F97316",
        "#EA580C"
    ],
    title="Customer Value vs Purchase Frequency"
)

fig3.update_layout(
    xaxis_type="log",
    yaxis_type="log"
)

fig3 = apply_dark_theme(fig3)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# =========================================================
# CUSTOMER VALUE BY SEGMENT
# =========================================================

st.markdown("---")

st.subheader("💰 Customer Value by Segment")

segment_value = (
    filtered_df
    .groupby("Segment")["Monetary"]
    .mean()
    .reset_index()
)

fig4 = px.bar(
    segment_value,
    x="Segment",
    y="Monetary",
    color="Monetary",
    color_continuous_scale=[
        "#F59E0B",
        "#F97316",
        "#EA580C"
    ],
    title="Average Monetary Value by Segment"
)

fig4.update_layout(
    coloraxis_showscale=False
)

fig4 = apply_dark_theme(fig4)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# =========================================================
# CHURN RISK BY SEGMENT
# =========================================================

st.markdown("---")

st.subheader("⚠️ Churn Risk by Segment")

segment_churn = (
    filtered_df
    .groupby("Segment")["Churn_Probability"]
    .mean()
    .reset_index()
)

fig5 = px.bar(
    segment_churn,
    x="Segment",
    y="Churn_Probability",
    color="Churn_Probability",
    color_continuous_scale=[
        "#F59E0B",
        "#F97316",
        "#EA580C"
    ],
    title="Average Churn Probability by Segment"
)

fig5.update_layout(
    coloraxis_showscale=False
)

fig5 = apply_dark_theme(fig5)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# =========================================================
# CHURN HEATMAP
# =========================================================

st.markdown("---")

st.subheader("🔥 Segment Intelligence Heatmap")

heatmap_df = (
    filtered_df
    .groupby("Segment")
    [
        [
            "Recency",
            "Frequency",
            "Monetary",
            "Churn_Probability"
        ]
    ]
    .mean()
)

fig_heat = px.imshow(
    heatmap_df,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="Oranges"
)

fig_heat = apply_dark_theme(fig_heat)

st.plotly_chart(
    fig_heat,
    use_container_width=True
)

# =========================================================
# TOP CUSTOMERS
# =========================================================

st.markdown("---")

st.subheader("🏆 Top High-Value Customers")

top_customers = (
    filtered_df
    .sort_values(
        by="Monetary",
        ascending=False
    )
    .head(20)
)

st.dataframe(
    top_customers[
        [
            "CustomerID",
            "Segment",
            "Monetary",
            "Frequency",
            "Recency",
            "Churn_Probability"
        ]
    ],
    use_container_width=True,
    height=400
)

# =========================================================
# HIGH RISK CUSTOMERS
# =========================================================

st.markdown("---")

st.subheader("🚨 High Churn Risk Customers")

high_risk_df = filtered_df[
    filtered_df["Churn_Probability"] > 0.7
]

st.dataframe(
    high_risk_df[
        [
            "CustomerID",
            "Segment",
            "Monetary",
            "Frequency",
            "Recency",
            "Churn_Probability"
        ]
    ],
    use_container_width=True,
    height=400
)

# =========================================================
# AI CUSTOMER INSIGHTS
# =========================================================

st.markdown("---")

st.subheader("🧠 AI Customer Insights")

top_segment = (
    filtered_df["Segment"]
    .value_counts()
    .idxmax()
)

highest_risk_segment = (
    segment_churn
    .sort_values(
        by="Churn_Probability",
        ascending=False
    )
    .iloc[0]["Segment"]
)

st.info(f"""
• Largest customer segment: {top_segment}

• Highest churn-risk segment: {highest_risk_segment}

• Average customer value is ${avg_monetary:,.0f}

• {high_risk_customers:,} customers require immediate retention targeting
""")

# =========================================================
# AI RETENTION ENGINE
# =========================================================

st.markdown("---")

st.subheader("🤖 AI Retention Recommendations")

if avg_churn > 0.6:
    st.warning(
        "Customer churn probability is elevated. Launch retention campaigns immediately."
    )

if high_risk_customers > total_customers * 0.3:
    st.error(
        "High-risk customer count exceeds healthy retention threshold."
    )

if avg_monetary > 500:
    st.success(
        "High customer lifetime value detected across active segments."
    )

st.info(
    "Recommendation: Prioritize loyalty rewards for high-frequency customers with increasing recency trends."
)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "NeuralRetail AI • Customer Intelligence Module • Amdox Technologies"
)

