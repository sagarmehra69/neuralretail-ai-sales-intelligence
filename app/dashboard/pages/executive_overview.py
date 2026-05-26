# =========================================================
# Executive Overview Dashboard
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Executive Overview", layout="wide")

# =========================================================
# TITLE
# =========================================================

st.title("📊 Executive Overview")

st.markdown("""
Retail Intelligence Summary Dashboard
""")

# =========================================================
# SIMULATED DATA
# (Replace later with real CSV/model outputs)
# =========================================================

np.random.seed(42)

dates = pd.date_range(start="2025-01-01", periods=100)

revenue = np.random.randint(10000, 50000, size=100)

forecast = revenue + np.random.randint(-3000, 3000, size=100)

overview_df = pd.DataFrame({"Date": dates, "Revenue": revenue, "Forecast": forecast})

# =========================================================
# KPI SECTION
# =========================================================

st.markdown("## 📌 Key Business Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Revenue", "$2.4M", "+12%")

with col2:
    st.metric("Forecast Accuracy", "78.5%", "+4.2%")

with col3:
    st.metric("High-Risk Customers", "214", "-18")

with col4:
    st.metric("Inventory Alerts", "42", "-6")

# =========================================================
# REVENUE TREND
# =========================================================

st.markdown("---")

st.subheader("📈 Revenue Trend")

fig_revenue = px.line(
    overview_df, x="Date", y=["Revenue", "Forecast"], title="Revenue vs Forecast"
)

st.plotly_chart(fig_revenue, use_container_width=True)

# =========================================================
# CHURN + INVENTORY SECTION
# =========================================================

st.markdown("---")

col1, col2 = st.columns(2)

# =========================================================
# CHURN DISTRIBUTION
# =========================================================

with col1:
    st.subheader("👥 Customer Churn Distribution")

    churn_df = pd.DataFrame(
        {
            "Category": ["Low Risk", "Medium Risk", "High Risk"],
            "Customers": [1200, 430, 214],
        }
    )

    fig_churn = px.pie(churn_df, names="Category", values="Customers", hole=0.4)

    st.plotly_chart(fig_churn, use_container_width=True)

# =========================================================
# INVENTORY RISK
# =========================================================

with col2:
    st.subheader("📦 Inventory Risk Levels")

    inventory_df = pd.DataFrame(
        {"Category": ["Low", "Medium", "High"], "Count": [300, 120, 42]}
    )

    fig_inventory = px.bar(
        inventory_df, x="Category", y="Count", title="Inventory Risk Distribution"
    )

    st.plotly_chart(fig_inventory, use_container_width=True)

# =========================================================
# TOP PRODUCTS
# =========================================================

st.markdown("---")

st.subheader("🏆 Top Performing Products")

top_products = pd.DataFrame(
    {
        "Product": ["Laptop", "Smartphone", "Headphones", "Keyboard", "Monitor"],
        "Revenue": [450000, 390000, 210000, 180000, 150000],
    }
)

fig_products = px.bar(
    top_products, x="Product", y="Revenue", title="Top Product Revenue"
)

st.plotly_chart(fig_products, use_container_width=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Executive Intelligence Dashboard")
