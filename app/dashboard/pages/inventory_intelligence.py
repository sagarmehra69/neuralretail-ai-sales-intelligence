import streamlit as st
import plotly.express as px

from utils.loader import load_inventory_data

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
# LOAD DATA
# =========================================================

inventory_df = load_inventory_data()

# =========================================================
# KPI SECTION
# =========================================================

total_products = len(inventory_df)

avg_risk = inventory_df["Inventory_Risk_Score"].mean()

reorder_alerts = len(
    inventory_df[inventory_df["current_stock"] < inventory_df["ReorderPoint"]]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Products", total_products)

with col2:
    st.metric("Reorder Alerts", reorder_alerts)

with col3:
    st.metric("Average Risk Score", f"{avg_risk:.2f}")

# =========================================================
# INVENTORY RISK DISTRIBUTION
# =========================================================

st.markdown("---")

st.subheader("📊 Inventory Risk Distribution")

fig = px.histogram(inventory_df, x="Inventory_Risk_Score", nbins=30)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# STOCK VS REORDER POINT
# =========================================================

st.markdown("---")

st.subheader("📉 Current Stock vs Reorder Point")

sample_df = inventory_df.head(30)

fig2 = px.bar(
    sample_df, x="product", y=["current_stock", "ReorderPoint"], barmode="group"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# HIGH-RISK PRODUCTS
# =========================================================

st.markdown("---")

st.subheader("🚨 High-Risk Inventory")

high_risk = inventory_df[inventory_df["Inventory_Risk_Score"] > 0.7]

st.dataframe(high_risk, use_container_width=True)

# =========================================================
# EOQ ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📦 EOQ Analysis")

fig3 = px.scatter(
    inventory_df, x="current_stock", y="EOQ", color="Inventory_Risk_Score"
)

st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Inventory Intelligence Module")
