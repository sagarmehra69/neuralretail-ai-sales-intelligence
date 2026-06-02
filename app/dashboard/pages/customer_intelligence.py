# =========================================================
# NeuralRetail AI - Customer Intelligence
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.theme import load_css
from utils.loader import load_churn_data
from utils.chart_theme import apply_dark_theme

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Customer Intelligence", layout="wide")

load_css()

# =========================================================
# TITLE
# =========================================================

st.title("🧠 Customer Intelligence")

st.markdown("""
AI-powered customer analytics, churn prediction, and RFM intelligence platform.
""")

# =========================================================
# LOAD DATA
# =========================================================

churn_df = load_churn_data()

# =========================================================
# KPI SECTION
# =========================================================

total_customers = churn_df["CustomerID"].nunique()

high_risk_customers = len(churn_df[churn_df["Churn_Probability"] > 0.7])

avg_churn = round(churn_df["Churn_Probability"].mean(), 2)

avg_monetary = round(churn_df["Monetary"].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", f"{total_customers:,}")

with col2:
    st.metric("High Risk Customers", f"{high_risk_customers:,}")

with col3:
    st.metric("Avg Churn Probability", f"{avg_churn}")

with col4:
    st.metric("Avg Customer Value", f"${avg_monetary:,.0f}")

# =========================================================
# CHURN DISTRIBUTION
# =========================================================

st.markdown("---")

st.subheader("📊 Churn Probability Distribution")

fig1 = px.histogram(
    churn_df, x="Churn_Probability", nbins=30, title="Customer Churn Risk Distribution"
)

fig1 = apply_dark_theme(fig1)

st.plotly_chart(fig1, use_container_width=True)

# =========================================================
# CUSTOMER SEGMENTS
# =========================================================

st.markdown("---")

st.subheader("👥 Customer Segment Distribution")

segment_df = churn_df["Segment"].value_counts().reset_index()

segment_df.columns = ["Segment", "Customers"]

fig2 = px.pie(
    segment_df,
    names="Segment",
    values="Customers",
    hole=0.5,
    title="Customer Segmentation",
)

fig2 = apply_dark_theme(fig2)

st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# RFM ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📈 RFM Customer Analysis")

fig3 = px.scatter(
    churn_df,
    x="Frequency",
    y="Monetary",
    size="Recency",
    color="Churn_Probability",
    hover_data=["CustomerID", "Segment"],
    title="Customer Value vs Purchase Frequency",
)

fig3 = apply_dark_theme(fig3)

st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# CUSTOMER VALUE BY SEGMENT
# =========================================================

st.markdown("---")

st.subheader("💰 Customer Value by Segment")

segment_value = churn_df.groupby("Segment")["Monetary"].mean().reset_index()

fig4 = px.bar(
    segment_value,
    x="Segment",
    y="Monetary",
    color="Monetary",
    title="Average Monetary Value by Segment",
)

fig4 = apply_dark_theme(fig4)

st.plotly_chart(fig4, use_container_width=True)

# =========================================================
# CHURN RISK BY SEGMENT
# =========================================================

st.markdown("---")

st.subheader("⚠️ Churn Risk by Segment")

segment_churn = churn_df.groupby("Segment")["Churn_Probability"].mean().reset_index()

fig5 = px.bar(
    segment_churn,
    x="Segment",
    y="Churn_Probability",
    color="Churn_Probability",
    title="Average Churn Probability by Segment",
)

fig5 = apply_dark_theme(fig5)

st.plotly_chart(fig5, use_container_width=True)

# =========================================================
# TOP CUSTOMERS
# =========================================================

st.markdown("---")

st.subheader("🏆 Top High-Value Customers")

top_customers = churn_df.sort_values(by="Monetary", ascending=False).head(20)

st.dataframe(top_customers, use_container_width=True)

# =========================================================
# HIGH CHURN RISK CUSTOMERS
# =========================================================

st.markdown("---")

st.subheader("🚨 High Churn Risk Customers")

high_risk_df = churn_df[churn_df["Churn_Probability"] > 0.7]

st.dataframe(high_risk_df, use_container_width=True)

# =========================================================
# CUSTOMER INSIGHTS
# =========================================================

st.markdown("---")

st.subheader("🧠 AI Customer Insights")

top_segment = churn_df["Segment"].value_counts().idxmax()

highest_risk_segment = segment_churn.sort_values(
    by="Churn_Probability", ascending=False
).iloc[0]["Segment"]

st.info(f"""
• Largest customer segment: {top_segment}

• Highest churn-risk segment: {highest_risk_segment}

• Average customer value is ${avg_monetary:,.0f}

• {high_risk_customers:,} customers require retention targeting
""")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Customer Intelligence Module • Amdox Technologies")
