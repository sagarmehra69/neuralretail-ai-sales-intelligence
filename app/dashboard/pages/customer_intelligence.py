import streamlit as st
import plotly.express as px

from utils.loader import load_churn_data

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Customer Intelligence", layout="wide")

# =========================================================
# TITLE
# =========================================================

st.title("🧠 Customer Intelligence")

st.markdown("""
AI-powered churn prediction and customer segmentation analytics.
""")

# =========================================================
# LOAD DATA
# =========================================================

churn_df = load_churn_data()

# =========================================================
# KPI SECTION
# =========================================================

total_customers = len(churn_df)

high_risk = len(churn_df[churn_df["Churn_Probability"] > 0.7])

avg_churn = churn_df["Churn_Probability"].mean()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", f"{total_customers:,}")

with col2:
    st.metric("High Churn Risk", high_risk)

with col3:
    st.metric("Average Churn Probability", f"{avg_churn:.2f}")

# =========================================================
# CHURN DISTRIBUTION
# =========================================================

st.markdown("---")

st.subheader("📊 Churn Probability Distribution")

fig = px.histogram(
    churn_df, x="Churn_Probability", nbins=30, title="Churn Probability Distribution"
)

fig.update_traces(opacity=0.85)
fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# CUSTOMER SEGMENTS
# =========================================================

st.markdown("---")

st.subheader("👥 Customer Segments")

segment_counts = churn_df["Segment"].value_counts().reset_index()

segment_counts.columns = ["Segment", "Count"]

fig2 = px.pie(segment_counts, names="Segment", values="Count", hole=0.4)

st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# HIGH-RISK CUSTOMERS
# =========================================================

st.markdown("---")

st.subheader("🚨 High-Risk Customers")

high_risk_df = churn_df[churn_df["Churn_Probability"] > 0.7]

st.dataframe(high_risk_df, use_container_width=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Customer Intelligence Module")
