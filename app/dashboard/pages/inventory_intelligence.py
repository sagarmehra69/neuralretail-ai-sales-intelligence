import streamlit as st
import plotly.express as px

from utils.chart_theme import apply_dark_theme
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
top_inventory = inventory_df.sort_values(
    by="Inventory_Risk_Score", ascending=False
).head(20)

total_products = len(inventory_df)

avg_risk = inventory_df["Inventory_Risk_Score"].mean()

reorder_alerts = len(
    inventory_df[inventory_df["current_stock"] < inventory_df["Reorder_Point"]]
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
fig = apply_dark_theme(fig)

st.plotly_chart(fig, use_container_width=True)


fig = px.bar(
    top_inventory,
    x="product",
    y=["current_stock", "Reorder_Point"],
    barmode="group",
    title="Top 20 High-Risk Products",
)
fig = apply_dark_theme(fig)
st.plotly_chart(fig, use_container_width=True)
# =========================================================
# STOCK VS REORDER POINT
# =========================================================

st.markdown("---")

st.subheader("📉 Current Stock vs Reorder Point")

sample_df = inventory_df.head(30)

fig2 = px.bar(
    sample_df, x="product", y=["current_stock", "Reorder_Point"], barmode="group"
)
fig2 = apply_dark_theme(fig2)
st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# HIGH-RISK PRODUCTS
# =========================================================

st.markdown("---")

st.subheader("🚨 High-Risk Inventory")

high_risk = inventory_df[inventory_df["Inventory_Risk_Score"] > 0.7]

st.dataframe(high_risk, use_container_width=True)

# =========================================================
# EOQ VS CURRENT STOCK
# =========================================================

st.markdown("---")

st.subheader("📦 EOQ vs Current Stock")

top_stock = inventory_df.head(20)

fig5 = px.bar(
    top_stock,
    x="product",
    y=["EOQ", "current_stock"],
    barmode="group",
    title="EOQ vs Current Stock",
)
fig5 = apply_dark_theme(fig5)
st.plotly_chart(fig5, use_container_width=True)


# =========================================================
# REORDER ALERTS
# =========================================================

st.markdown("---")

st.subheader("🚨 Reorder Alert Dashboard")

reorder_df = inventory_df[
    inventory_df["Reorder_Alert"] == 1
]

st.dataframe(
    reorder_df[
        [
            "product",
            "current_stock",
            "Reorder_Point",
            "EOQ",
            "Inventory_Risk_Score",
        ]
    ],
    use_container_width=True,
)



# =========================================================
# REVENUE CONTRIBUTION
# =========================================================

st.markdown("---")

st.subheader("💰 Top Revenue Generating Products")

top_revenue = inventory_df.sort_values(
    by="annual_revenue",
    ascending=False
).head(15)

fig4 = px.bar(
    top_revenue,
    x="product",
    y="annual_revenue",
    color="annual_revenue",
    title="Top Revenue Products",
)
fig4 = apply_dark_theme(fig4)
st.plotly_chart(fig4, use_container_width=True)


# =========================================================
# DEAD STOCK ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("💀 Dead Stock Analysis")

dead_stock_df = inventory_df[
    inventory_df["Dead_Stock"] == 1
]

dead_stock_count = len(dead_stock_df)

st.metric(
    "Dead Stock Products",
    dead_stock_count
)

fig7 = px.bar(
    dead_stock_df.head(15),
    x="product",
    y="current_stock",
    color="Inventory_Risk_Score",
    title="Dead Stock Products",
)
fig7 = apply_dark_theme(fig7)
st.plotly_chart(fig7, use_container_width=True)

# =========================================================
# DEMAND VARIABILITY ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📈 Demand Variability Analysis")

fig8 = px.scatter(
    inventory_df,
    x="daily_demand",
    y="CV",
    color="XYZ_Class",
    size="annual_revenue",
    hover_name="product",
    title="Demand Variability vs Daily Demand",
)
fig8 = apply_dark_theme(fig8)
st.plotly_chart(fig8, use_container_width=True)



# =========================================================
# XYZ CLASSIFICATION
# =========================================================

st.markdown("---")

st.subheader("🧠 XYZ Demand Classification")

xyz_counts = (
    inventory_df["XYZ_Class"]
    .value_counts()
    .reset_index()
)

xyz_counts.columns = [
    "XYZ_Class",
    "Count",
]

fig6 = px.pie(
    xyz_counts,
    names="XYZ_Class",
    values="Count",
    title="XYZ Product Classification",
)
fig6 = apply_dark_theme(fig6)
st.plotly_chart(fig6, use_container_width=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Inventory Intelligence Module")
