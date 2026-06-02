# =========================================================
# NeuralRetail AI - Smart Inventory Intelligence
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.theme import load_css
from utils.chart_theme import apply_dark_theme
from utils.loader import load_inventory_data

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Inventory Intelligence", layout="wide")

load_css()

# =========================================================
# LOAD DATA
# =========================================================

inventory_df = load_inventory_data()

# =========================================================
# DATA CLEANING
# =========================================================

inventory_df = inventory_df.dropna()

inventory_df = inventory_df[inventory_df["annual_revenue"] > 0]

inventory_df = inventory_df[inventory_df["current_stock"] >= 0]

inventory_df = inventory_df[inventory_df["Inventory_Risk_Score"] >= 0]

# Remove Extreme Outliers

inventory_df = inventory_df[inventory_df["Inventory_Risk_Score"] <= 100]

# =========================================================
# TITLE
# =========================================================

st.title("📦 Inventory Intelligence")

st.markdown("""
AI-powered inventory optimization and stock risk monitoring system.
""")

# =========================================================
# KPI SECTION
# =========================================================

total_products = inventory_df["product"].nunique()

critical_products = len(
    inventory_df[inventory_df["current_stock"] <= inventory_df["Reorder_Point"]]
)

dead_stock = len(inventory_df[inventory_df["Dead_Stock"] == 1])

avg_inventory_risk = round(inventory_df["Inventory_Risk_Score"].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Products", f"{total_products:,}")

with col2:
    st.metric("Critical Alerts", critical_products)

with col3:
    st.metric("Dead Stock", dead_stock)

with col4:
    st.metric("Avg Risk Score", avg_inventory_risk)

# =========================================================
# INVENTORY HEALTH OVERVIEW
# =========================================================

st.markdown("---")

st.subheader("📊 Inventory Health Overview")

health_df = pd.DataFrame(
    {
        "Category": ["Healthy", "Critical", "Dead Stock"],
        "Count": [
            len(inventory_df) - critical_products - dead_stock,
            critical_products,
            dead_stock,
        ],
    }
)

fig_health = px.pie(
    health_df,
    names="Category",
    values="Count",
    hole=0.55,
)

fig_health.update_traces(textposition="inside", textinfo="percent+label")

fig_health.update_layout(title="Inventory Status Distribution", showlegend=True)

fig_health = apply_dark_theme(fig_health)

st.plotly_chart(fig_health, use_container_width=True)

# =========================================================
# TOP REVENUE PRODUCTS
# =========================================================

st.markdown("---")

st.subheader("💰 Top Revenue Products")

top_revenue = inventory_df.sort_values(by="annual_revenue", ascending=False).head(10)

fig_revenue = px.treemap(
    top_revenue,
    path=["product"],
    values="annual_revenue",
    color="annual_revenue",
)

fig_revenue.update_layout(title="Revenue Contribution by Products")

fig_revenue = apply_dark_theme(fig_revenue)

st.plotly_chart(fig_revenue, use_container_width=True)

# =========================================================
# STOCK COVERAGE ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📈 Stock Coverage Analysis")

coverage_df = inventory_df.sort_values(by="monthly_sales", ascending=False).head(20)

fig_stock = px.scatter(
    coverage_df,
    x="monthly_sales",
    y="current_stock",
    size="annual_revenue",
    color="Inventory_Risk_Score",
    hover_name="product",
)

fig_stock.update_layout(title="Monthly Demand vs Current Stock")

fig_stock = apply_dark_theme(fig_stock)

st.plotly_chart(fig_stock, use_container_width=True)

# =========================================================
# DEMAND VARIABILITY
# =========================================================

st.markdown("---")

st.subheader("🧠 Demand Variability Classification")

xyz_counts = inventory_df["XYZ_Class"].value_counts().reset_index()

xyz_counts.columns = ["Class", "Count"]
fig_xyz = px.pie(
    xyz_counts,
    names="Class",
    values="Count",
    hole=0.55,
    color_discrete_sequence=["#E84E1B", "#F7941D", "#FBBA13"],
)

fig_xyz.update_layout(title="XYZ Inventory Segmentation")

fig_xyz = apply_dark_theme(fig_xyz)

st.plotly_chart(fig_xyz, use_container_width=True)

# =========================================================
# AI RECOMMENDATION ENGINE
# =========================================================

st.markdown("---")

st.subheader("🤖 AI Inventory Recommendations")

high_risk_count = len(inventory_df[inventory_df["Inventory_Risk_Score"] > 70])

if high_risk_count > 50:
    st.warning("""
    ⚠️ High inventory instability detected.
    
    Recommended Actions:
    - Reduce overstocked SKUs
    - Increase reorder monitoring
    - Optimize procurement cycle
    """)

elif dead_stock > 20:
    st.error("""
    🚨 Dead stock volume is increasing.
    
    Recommended Actions:
    - Launch discount clearance campaigns
    - Reduce future procurement
    - Improve demand forecasting
    """)

else:
    st.success("""
    ✅ Inventory system operating efficiently.
    
    AI Insight:
    - Stock levels are balanced
    - Reorder pipeline stable
    - Revenue flow optimized
    """)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Inventory Intelligence • Amdox Technologies")
