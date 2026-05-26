# =========================================================
# Inventory Intelligence Dashboard
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Inventory Intelligence", layout="wide")

# =========================================================
# TITLE
# =========================================================

st.title("📦 Inventory Intelligence")

st.markdown("""
AI-powered inventory optimization and stock risk analytics.
""")

# =========================================================
# SIMULATED INVENTORY DATA
# (Replace later with real inventory outputs)
# =========================================================

np.random.seed(42)

inventory_count = 300

inventory_df = pd.DataFrame(
    {
        "Product": [f"Product_{i}" for i in range(1, inventory_count + 1)],
        "Current_Stock": np.random.randint(10, 500, inventory_count),
        "Reorder_Point": np.random.randint(20, 150, inventory_count),
        "EOQ": np.random.randint(50, 300, inventory_count),
        "Inventory_Risk_Score": np.random.uniform(0, 1, inventory_count),
    }
)

# =========================================================
# INVENTORY RISK LABELS
# =========================================================

inventory_df["Risk_Level"] = pd.cut(
    inventory_df["Inventory_Risk_Score"],
    bins=[0, 0.4, 0.7, 1],
    labels=["Low Risk", "Medium Risk", "High Risk"],
)

# =========================================================
# KPI SECTION
# =========================================================

st.markdown("## 📌 Inventory KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Low Stock Items", "42", "-6")

with col2:
    st.metric("Dead Stock", "18", "-3")

with col3:
    st.metric("Reorder Alerts", "27", "+4")

with col4:
    st.metric("Avg Risk Score", "0.46", "-0.02")

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("Inventory Filters")

selected_risk = st.sidebar.selectbox(
    "Risk Level", ["All", "Low Risk", "Medium Risk", "High Risk"]
)

# =========================================================
# FILTER LOGIC
# =========================================================

filtered_df = inventory_df.copy()

if selected_risk != "All":
    filtered_df = filtered_df[filtered_df["Risk_Level"] == selected_risk]

# =========================================================
# INVENTORY RISK DISTRIBUTION
# =========================================================

st.markdown("---")

st.subheader("📊 Inventory Risk Distribution")

risk_counts = filtered_df["Risk_Level"].value_counts().reset_index()

risk_counts.columns = ["Risk_Level", "Count"]

fig_risk = px.pie(risk_counts, names="Risk_Level", values="Count", hole=0.4)

st.plotly_chart(fig_risk, use_container_width=True)

# =========================================================
# STOCK VS REORDER POINT
# =========================================================

st.markdown("---")

st.subheader("📉 Current Stock vs Reorder Point")

sample_products = filtered_df.head(25)

fig_stock = px.bar(
    sample_products,
    x="Product",
    y=["Current_Stock", "Reorder_Point"],
    barmode="group",
    title="Stock Monitoring",
)

st.plotly_chart(fig_stock, use_container_width=True)

# =========================================================
# EOQ ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📦 Economic Order Quantity (EOQ)")

fig_eoq = px.scatter(
    filtered_df,
    x="Current_Stock",
    y="EOQ",
    color="Inventory_Risk_Score",
    title="EOQ Optimization",
)

st.plotly_chart(fig_eoq, use_container_width=True)

# =========================================================
# HIGH-RISK PRODUCTS
# =========================================================

st.markdown("---")

st.subheader("🚨 High-Risk Inventory")

high_risk_inventory = filtered_df[filtered_df["Inventory_Risk_Score"] > 0.7]

st.dataframe(
    high_risk_inventory[
        ["Product", "Current_Stock", "Reorder_Point", "EOQ", "Inventory_Risk_Score"]
    ],
    use_container_width=True,
)

# =========================================================
# ABC CLASSIFICATION
# =========================================================

st.markdown("---")

st.subheader("🏷️ ABC Inventory Classification")

abc_df = pd.DataFrame({"Category": ["A", "B", "C"], "Products": [50, 120, 130]})

fig_abc = px.bar(abc_df, x="Category", y="Products", title="ABC Inventory Analysis")

st.plotly_chart(fig_abc, use_container_width=True)

# =========================================================
# REORDER RECOMMENDATIONS
# =========================================================

st.markdown("---")

st.subheader("🔄 Reorder Recommendations")

reorder_df = filtered_df[filtered_df["Current_Stock"] < filtered_df["Reorder_Point"]]

st.dataframe(
    reorder_df[["Product", "Current_Stock", "Reorder_Point", "EOQ"]],
    use_container_width=True,
)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Inventory Intelligence Module")
