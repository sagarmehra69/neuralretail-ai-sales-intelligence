
# # =========================================================
# # NeuralRetail AI — Smart Inventory Intelligence
# # Amdox Technologies
# # =========================================================

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# from auth_guard import check_auth
# from utils.theme import load_css
# from utils.chart_theme import apply_dark_theme
# from utils.loader import load_inventory_data

# check_auth()
# # =========================================================
# # PAGE CONFIG
# # =========================================================

# st.set_page_config(
#     page_title="Inventory Intelligence",
#     layout="wide"
# )

# load_css()

# # =========================================================
# # LOAD DATA
# # =========================================================

# inventory_df = load_inventory_data()

# # =========================================================
# # DATA CLEANING
# # =========================================================

# inventory_df = inventory_df.dropna()

# inventory_df = inventory_df[
#     inventory_df["annual_revenue"] > 0
# ]

# inventory_df = inventory_df[
#     inventory_df["current_stock"] >= 0
# ]

# inventory_df = inventory_df[
#     inventory_df["Inventory_Risk_Score"] >= 0
# ]

# inventory_df = inventory_df[
#     inventory_df["Inventory_Risk_Score"] <= 100
# ]

# # =========================================================
# # PAGE TITLE
# # =========================================================

# st.title("📦 Inventory Intelligence")

# st.markdown("""
# AI-powered inventory optimization and stock risk monitoring system.
# """)

# # =========================================================
# # KPI SECTION
# # =========================================================

# total_products = (
#     inventory_df["product"]
#     .nunique()
# )

# critical_products = len(
#     inventory_df[
#         inventory_df["current_stock"] <=
#         inventory_df["Reorder_Point"]
#     ]
# )

# dead_stock = len(
#     inventory_df[
#         inventory_df["Dead_Stock"] == 1
#     ]
# )

# avg_inventory_risk = round(
#     inventory_df["Inventory_Risk_Score"]
#     .mean(),
#     2
# )

# total_inventory_value = round(
#     inventory_df["annual_revenue"]
#     .sum(),
#     0
# )

# st.markdown("## 📌 Inventory KPI Overview")

# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     st.metric(
#         "📦 Products",
#         f"{total_products:,}"
#     )

# with col2:
#     st.metric(
#         "⚠️ Critical Alerts",
#         f"{critical_products:,}"
#     )

# with col3:
#     st.metric(
#         "🚨 Dead Stock",
#         f"{dead_stock:,}"
#     )

# with col4:
#     st.metric(
#         "📉 Avg Risk Score",
#         avg_inventory_risk
#     )

# with col5:
#     st.metric(
#         "💰 Inventory Value",
#         f"${total_inventory_value:,.0f}"
#     )

# # =========================================================
# # INVENTORY HEALTH OVERVIEW
# # =========================================================

# st.markdown("---")

# st.subheader("📊 Inventory Health Overview")

# healthy_products = max(
#     len(inventory_df) -
#     critical_products -
#     dead_stock,
#     0
# )

# health_df = pd.DataFrame({
#     "Category": [
#         "Healthy",
#         "Critical",
#         "Dead Stock"
#     ],
#     "Count": [
#         healthy_products,
#         critical_products,
#         dead_stock
#     ]
# })

# fig_health = px.bar(
#     health_df,
#     x="Category",
#     y="Count",
#     color="Category",
#     text_auto=True,
#     color_discrete_sequence=[
#         "#22C55E",
#         "#F97316",
#         "#DC2626"
#     ],
#     title="Inventory Status Distribution"
# )

# fig_health.update_layout(
#     height=500,
#     showlegend=False
# )

# fig_health = apply_dark_theme(fig_health)

# st.plotly_chart(
#     fig_health,
#     use_container_width=True
# )

# # =========================================================
# # TOP REVENUE PRODUCTS
# # =========================================================

# st.markdown("---")

# st.subheader("💰 Top Revenue Products")

# top_revenue = (
#     inventory_df
#     .sort_values(
#         by="annual_revenue",
#         ascending=False
#     )
#     .head(10)
# )

# fig_revenue = px.bar(
#     top_revenue,
#     x="annual_revenue",
#     y="product",
#     orientation="h",
#     color="annual_revenue",
#     color_continuous_scale=[
#         "#F59E0B",
#         "#F97316",
#         "#EA580C"
#     ],
#     title="Top Revenue Generating Products"
# )

# fig_revenue.update_layout(
#     height=550,
#     coloraxis_showscale=False
# )

# fig_revenue = apply_dark_theme(fig_revenue)

# st.plotly_chart(
#     fig_revenue,
#     use_container_width=True
# )

# # =========================================================
# # STOCK COVERAGE ANALYSIS
# # =========================================================

# st.markdown("---")

# st.subheader("📈 Stock Coverage Analysis")

# coverage_df = (
#     inventory_df
#     .sort_values(
#         by="monthly_sales",
#         ascending=False
#     )
#     .head(25)
# )

# fig_stock = px.scatter(
#     coverage_df,
#     x="monthly_sales",
#     y="current_stock",
#     size="annual_revenue",
#     color="Inventory_Risk_Score",
#     hover_name="product",
#     color_continuous_scale=[
#         "#22C55E",
#         "#F59E0B",
#         "#DC2626"
#     ],
#     title="Monthly Demand vs Current Stock"
# )

# fig_stock.update_layout(
#     height=600
# )

# fig_stock = apply_dark_theme(fig_stock)

# st.plotly_chart(
#     fig_stock,
#     use_container_width=True
# )

# # =========================================================
# # INVENTORY RISK DISTRIBUTION
# # =========================================================

# st.markdown("---")

# st.subheader("🔥 Inventory Risk Distribution")

# fig_risk = px.histogram(
#     inventory_df,
#     x="Inventory_Risk_Score",
#     nbins=25,
#     color_discrete_sequence=["#F97316"],
#     title="Inventory Risk Score Spread"
# )

# fig_risk.update_layout(
#     height=500
# )

# fig_risk = apply_dark_theme(fig_risk)

# st.plotly_chart(
#     fig_risk,
#     use_container_width=True
# )

# # =========================================================
# # XYZ CLASSIFICATION
# # =========================================================

# st.markdown("---")

# st.subheader("🧠 Demand Variability Classification")

# xyz_counts = (
#     inventory_df["XYZ_Class"]
#     .value_counts()
#     .reset_index()
# )

# xyz_counts.columns = [
#     "Class",
#     "Count"
# ]

# fig_xyz = px.bar(
#     xyz_counts,
#     x="Class",
#     y="Count",
#     color="Class",
#     text_auto=True,
#     color_discrete_sequence=[
#         "#E84E1B",
#         "#F7941D",
#         "#FBBA13"
#     ],
#     title="XYZ Inventory Segmentation"
# )

# fig_xyz.update_layout(
#     height=500,
#     showlegend=False
# )

# fig_xyz = apply_dark_theme(fig_xyz)

# st.plotly_chart(
#     fig_xyz,
#     use_container_width=True
# )

# # =========================================================
# # HIGH RISK PRODUCTS
# # =========================================================

# st.markdown("---")

# st.subheader("🚨 High Risk Inventory Products")

# high_risk_df = inventory_df[
#     inventory_df["Inventory_Risk_Score"] > 70
# ]

# high_risk_df = high_risk_df.sort_values(
#     by="Inventory_Risk_Score",
#     ascending=False
# )

# st.dataframe(
#     high_risk_df.head(20),
#     use_container_width=True,
#     height=400
# )

# # =========================================================
# # AI RECOMMENDATION ENGINE
# # =========================================================

# st.markdown("---")

# st.subheader("🤖 AI Inventory Recommendations")

# high_risk_count = len(
#     inventory_df[
#         inventory_df["Inventory_Risk_Score"] > 70
#     ]
# )

# if high_risk_count > 50:

#     st.warning("""
#     ⚠️ High inventory instability detected.

#     Recommended Actions:
#     - Reduce overstocked SKUs
#     - Increase reorder monitoring
#     - Optimize procurement cycle
#     - Improve supplier forecasting
#     """)

# elif dead_stock > 20:

#     st.error("""
#     🚨 Dead stock volume increasing.

#     Recommended Actions:
#     - Launch clearance campaigns
#     - Reduce future procurement
#     - Optimize warehouse allocation
#     - Improve demand prediction
#     """)

# else:

#     st.success("""
#     ✅ Inventory system operating efficiently.

#     AI Insight:
#     - Stock levels balanced
#     - Reorder pipeline stable
#     - Revenue flow optimized
#     - Procurement cycle healthy
#     """)

# # =========================================================
# # STRATEGIC INSIGHTS
# # =========================================================

# st.markdown("---")

# st.subheader("🧠 AI Strategic Insights")

# highest_risk_product = (
#     inventory_df
#     .sort_values(
#         by="Inventory_Risk_Score",
#         ascending=False
#     )
#     .iloc[0]["product"]
# )

# top_product = (
#     top_revenue
#     .iloc[0]["product"]
# )

# st.info(f"""
# • Highest inventory risk detected in product: {highest_risk_product}

# • Best revenue-generating product: {top_product}

# • Total monitored inventory value: ${total_inventory_value:,.0f}

# • {critical_products:,} products require urgent stock review

# • Inventory optimization engine operational
# """)

# # =========================================================
# # FOOTER
# # =========================================================

# st.markdown("---")

# st.caption(
#     "NeuralRetail AI • Inventory Intelligence • Amdox Technologies"
# )


# =========================================================
# NeuralRetail AI — Smart Inventory Intelligence
# Amdox Technologies
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from auth_guard import check_auth
from utils.theme import load_css
from utils.chart_theme import apply_dark_theme
from utils.loader import load_inventory_data

check_auth()

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Inventory Intelligence",
    layout="wide"
)

load_css()

# =========================================================
# LOAD DATA
# =========================================================

inventory_df = load_inventory_data()

# =========================================================
# DATA CLEANING
# =========================================================

inventory_df = inventory_df.dropna()

inventory_df = inventory_df[
    inventory_df["annual_revenue"] > 0
]

inventory_df = inventory_df[
    inventory_df["current_stock"] >= 0
]

inventory_df = inventory_df[
    inventory_df["Inventory_Risk_Score"] >= 0
]

inventory_df = inventory_df[
    inventory_df["Inventory_Risk_Score"] <= 100
]

# =========================================================
# COMMON CHART LAYOUT
# =========================================================

COMMON_LAYOUT = dict(
    height=360,
    margin=dict(l=20, r=20, t=50, b=20)
)

# =========================================================
# PAGE TITLE
# =========================================================

st.title("📦 Inventory Intelligence")

st.markdown("""
AI-powered inventory optimization and stock risk monitoring system.
""")

# =========================================================
# KPI SECTION
# =========================================================

total_products = (
    inventory_df["product"]
    .nunique()
)

critical_products = len(
    inventory_df[
        inventory_df["current_stock"] <=
        inventory_df["Reorder_Point"]
    ]
)

dead_stock = len(
    inventory_df[
        inventory_df["Dead_Stock"] == 1
    ]
)

avg_inventory_risk = round(
    inventory_df["Inventory_Risk_Score"]
    .mean(),
    2
)

total_inventory_value = round(
    inventory_df["annual_revenue"]
    .sum(),
    0
)

st.markdown("## 📌 Inventory KPI Overview")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "📦 Products",
        f"{total_products:,}"
    )

with col2:
    st.metric(
        "⚠️ Critical Alerts",
        f"{critical_products:,}"
    )

with col3:
    st.metric(
        "🚨 Dead Stock",
        f"{dead_stock:,}"
    )

with col4:
    st.metric(
        "📉 Avg Risk Score",
        avg_inventory_risk
    )

with col5:
    st.metric(
        "💰 Inventory Value",
        f"${total_inventory_value:,.0f}"
    )

# =========================================================
# CHART ROW 1
# =========================================================

st.markdown("---")

col_left, col_right = st.columns(2)

# =========================================================
# INVENTORY HEALTH OVERVIEW
# =========================================================

with col_left:

    healthy_products = max(
        len(inventory_df) -
        critical_products -
        dead_stock,
        0
    )

    health_df = pd.DataFrame({
        "Category": [
            "Healthy",
            "Critical",
            "Dead Stock"
        ],
        "Count": [
            healthy_products,
            critical_products,
            dead_stock
        ]
    })

    fig_health = px.bar(
        health_df,
        x="Category",
        y="Count",
        color="Category",
        text_auto=True,
        color_discrete_sequence=[
            "#22C55E",
            "#F97316",
            "#DC2626"
        ],
        title="📊 Inventory Health Overview"
    )

    fig_health.update_layout(
        showlegend=False,
        **COMMON_LAYOUT
    )

    fig_health = apply_dark_theme(fig_health)

    st.plotly_chart(
        fig_health,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# =========================================================
# TOP REVENUE PRODUCTS
# =========================================================

with col_right:

    top_revenue = (
        inventory_df
        .sort_values(
            by="annual_revenue",
            ascending=True
        )
        .tail(10)
    )

    fig_revenue = px.bar(
        top_revenue,
        x="annual_revenue",
        y="product",
        orientation="h",
        color="annual_revenue",
        text_auto=".2s",
        color_continuous_scale=[
            "#F59E0B",
            "#F97316",
            "#EA580C"
        ],
        title="💰 Top Revenue Products"
    )

    fig_revenue.update_layout(
        coloraxis_showscale=False,
        **COMMON_LAYOUT
    )

    fig_revenue = apply_dark_theme(fig_revenue)

    st.plotly_chart(
        fig_revenue,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# =========================================================
# CHART ROW 2
# =========================================================

st.markdown("---")

col_left, col_right = st.columns(2)

# =========================================================
# STOCK COVERAGE ANALYSIS
# =========================================================

with col_left:

    coverage_df = (
        inventory_df
        .sort_values(
            by="monthly_sales",
            ascending=False
        )
        .head(25)
    )

    fig_stock = px.scatter(
        coverage_df,
        x="monthly_sales",
        y="current_stock",
        size="annual_revenue",
        color="Inventory_Risk_Score",
        hover_name="product",
        color_continuous_scale=[
            "#22C55E",
            "#F59E0B",
            "#DC2626"
        ],
        title="📈 Stock Coverage Analysis"
    )

    fig_stock.update_layout(
        coloraxis_showscale=False,
        **COMMON_LAYOUT
    )

    fig_stock = apply_dark_theme(fig_stock)

    st.plotly_chart(
        fig_stock,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# =========================================================
# INVENTORY RISK DISTRIBUTION
# =========================================================

with col_right:

    fig_risk = px.histogram(
        inventory_df,
        x="Inventory_Risk_Score",
        nbins=25,
        color_discrete_sequence=["#F97316"],
        title="🔥 Inventory Risk Distribution"
    )

    fig_risk.update_layout(
        showlegend=False,
        **COMMON_LAYOUT
    )

    fig_risk = apply_dark_theme(fig_risk)

    st.plotly_chart(
        fig_risk,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# =========================================================
# CHART ROW 3
# =========================================================

st.markdown("---")

col_left, col_right = st.columns(2)

# =========================================================
# XYZ CLASSIFICATION
# =========================================================

with col_left:

    xyz_counts = (
        inventory_df["XYZ_Class"]
        .value_counts()
        .reset_index()
    )

    xyz_counts.columns = [
        "Class",
        "Count"
    ]

    xyz_counts = xyz_counts.sort_values(
        by="Class",
        ascending=True
    )

    fig_xyz = px.bar(
        xyz_counts,
        x="Class",
        y="Count",
        color="Class",
        text_auto=True,
        color_discrete_sequence=[
            "#E84E1B",
            "#F7941D",
            "#FBBA13"
        ],
        title="🧠 Demand Variability Classification"
    )

    fig_xyz.update_layout(
        showlegend=False,
        **COMMON_LAYOUT
    )

    fig_xyz = apply_dark_theme(fig_xyz)

    st.plotly_chart(
        fig_xyz,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# =========================================================
# INVENTORY HEATMAP
# =========================================================

with col_right:

    heatmap_df = (
        inventory_df
        .groupby("XYZ_Class")
        [
            [
                "current_stock",
                "monthly_sales",
                "annual_revenue",
                "Inventory_Risk_Score"
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

    fig_heat.update_layout(
        title="🔥 Inventory Intelligence Heatmap",
        height=360,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    fig_heat = apply_dark_theme(fig_heat)

    st.plotly_chart(
        fig_heat,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# =========================================================
# HIGH RISK PRODUCTS
# =========================================================

st.markdown("---")

st.subheader("🚨 High Risk Inventory Products")

high_risk_df = inventory_df[
    inventory_df["Inventory_Risk_Score"] > 70
]

high_risk_df = high_risk_df.sort_values(
    by="Inventory_Risk_Score",
    ascending=False
)

st.dataframe(
    high_risk_df.head(20),
    use_container_width=True,
    height=350
)

# =========================================================
# AI RECOMMENDATION ENGINE
# =========================================================

st.markdown("---")

st.subheader("🤖 AI Inventory Recommendations")

high_risk_count = len(
    inventory_df[
        inventory_df["Inventory_Risk_Score"] > 70
    ]
)

if high_risk_count > 50:

    st.warning("""
    ⚠️ High inventory instability detected.

    Recommended Actions:
    - Reduce overstocked SKUs
    - Increase reorder monitoring
    - Optimize procurement cycle
    - Improve supplier forecasting
    """)

elif dead_stock > 20:

    st.error("""
    🚨 Dead stock volume increasing.

    Recommended Actions:
    - Launch clearance campaigns
    - Reduce future procurement
    - Optimize warehouse allocation
    - Improve demand prediction
    """)

else:

    st.success("""
    ✅ Inventory system operating efficiently.

    AI Insight:
    - Stock levels balanced
    - Reorder pipeline stable
    - Revenue flow optimized
    - Procurement cycle healthy
    """)

# =========================================================
# STRATEGIC INSIGHTS
# =========================================================

st.markdown("---")

st.subheader("🧠 AI Strategic Insights")

highest_risk_product = (
    inventory_df
    .sort_values(
        by="Inventory_Risk_Score",
        ascending=False
    )
    .iloc[0]["product"]
)

top_product = (
    top_revenue
    .sort_values(
        by="annual_revenue",
        ascending=False
    )
    .iloc[0]["product"]
)

st.info(f"""
• Highest inventory risk detected in product: {highest_risk_product}

• Best revenue-generating product: {top_product}

• Total monitored inventory value: ${total_inventory_value:,.0f}

• {critical_products:,} products require urgent stock review

• Inventory optimization engine operational
""")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "NeuralRetail AI • Inventory Intelligence • Amdox Technologies"
)