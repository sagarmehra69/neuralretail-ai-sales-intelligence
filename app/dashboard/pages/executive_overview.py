# =========================================================
# NeuralRetail AI — Executive Overview
# Amdox Technologies
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.theme import load_css
from utils.chart_theme import apply_dark_theme
from utils.loader import (
    load_sales_data,
    load_model_metrics
)

# =========================================================
# LOAD CSS
# =========================================================

load_css()

# =========================================================
# LOAD DATA
# =========================================================

sales_df = load_sales_data()
metrics_df = load_model_metrics()

# =========================================================
# COLUMN STANDARDIZATION
# =========================================================

sales_df.rename(
    columns={
        "invoicedate": "InvoiceDate",
        "invoiceno": "InvoiceNo",
        "stockcode": "StockCode",
        "description": "Description",
        "quantity": "Quantity",
        "unitprice": "UnitPrice",
        "customerid": "CustomerID",
        "country": "Country",
    },
    inplace=True,
)

# =========================================================
# DATA PROCESSING
# =========================================================

sales_df["InvoiceDate"] = pd.to_datetime(
    sales_df["InvoiceDate"]
)

sales_df["Revenue"] = (
    sales_df["Quantity"] *
    sales_df["UnitPrice"]
)

sales_df["YearMonth"] = (
    sales_df["InvoiceDate"]
    .dt.to_period("M")
    .astype(str)
)

sales_df["Month"] = (
    sales_df["InvoiceDate"]
    .dt.strftime("%b")
)

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🎯 Executive Controls")

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=sorted(sales_df["Country"].dropna().unique()),
    default=sorted(sales_df["Country"].dropna().unique())[:10]
)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [
        sales_df["InvoiceDate"].min(),
        sales_df["InvoiceDate"].max()
    ]
)

# =========================================================
# FILTER DATA
# =========================================================

filtered_df = sales_df[
    (sales_df["Country"].isin(selected_countries)) &
    (sales_df["InvoiceDate"] >= pd.to_datetime(date_range[0])) &
    (sales_df["InvoiceDate"] <= pd.to_datetime(date_range[1]))
]

# =========================================================
# PAGE TITLE
# =========================================================

st.title("🧠 Executive Overview")

st.markdown("""
Enterprise retail intelligence dashboard powered by AI forecasting,
customer analytics, and operational performance monitoring.
""")

# =========================================================
# EXECUTIVE KPIs
# =========================================================

total_revenue = filtered_df["Revenue"].sum()

total_orders = (
    filtered_df["InvoiceNo"]
    .nunique()
)

total_customers = (
    filtered_df["CustomerID"]
    .nunique()
)

total_products = (
    filtered_df["StockCode"]
    .nunique()
)

avg_order_value = (
    total_revenue / total_orders
)

st.markdown("## 📌 Executive KPI Overview")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "💰 Total Revenue",
        f"${total_revenue:,.0f}"
    )

with col2:
    st.metric(
        "🧾 Orders",
        f"{total_orders:,}"
    )

with col3:
    st.metric(
        "👥 Customers",
        f"{total_customers:,}"
    )

with col4:
    st.metric(
        "📦 Products",
        f"{total_products:,}"
    )

with col5:
    st.metric(
        "📊 Avg Order Value",
        f"${avg_order_value:,.2f}"
    )

# =========================================================
# MONTHLY REVENUE TREND
# =========================================================

st.markdown("---")

st.subheader("📈 Monthly Revenue Trend")

monthly_revenue = (
    filtered_df
    .groupby("YearMonth")["Revenue"]
    .sum()
    .reset_index()
)

fig1 = px.line(
    monthly_revenue,
    x="YearMonth",
    y="Revenue",
    markers=True,
    title="Monthly Revenue Performance"
)

fig1.update_traces(
    line=dict(
        color="#F97316",
        width=4
    )
)

fig1.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue",
    hovermode="x unified"
)

fig1 = apply_dark_theme(fig1)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =========================================================
# REVENUE BY COUNTRY
# =========================================================

st.markdown("---")

st.subheader("🌍 Revenue by Country")

country_revenue = (
    filtered_df
    .groupby("Country")["Revenue"]
    .sum()
    .reset_index()
    .sort_values(
        by="Revenue",
        ascending=False
    )
    .head(10)
)

fig2 = px.bar(
    country_revenue,
    x="Revenue",
    y="Country",
    orientation="h",
    color="Revenue",
    color_continuous_scale=[
        "#F59E0B",
        "#F97316",
        "#EA580C"
    ],
    title="Top Revenue Generating Countries"
)

fig2.update_layout(
    coloraxis_showscale=False
)

fig2 = apply_dark_theme(fig2)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =========================================================
# TOP PRODUCTS
# =========================================================

st.markdown("---")

st.subheader("🏆 Top Revenue Products")

top_products = (
    filtered_df
    .groupby("Description")["Revenue"]
    .sum()
    .reset_index()
    .sort_values(
        by="Revenue",
        ascending=False
    )
    .head(10)
)

fig3 = px.bar(
    top_products,
    x="Revenue",
    y="Description",
    orientation="h",
    color="Revenue",
    color_continuous_scale=[
        "#F59E0B",
        "#F97316",
        "#EA580C"
    ],
    title="Highest Revenue Products"
)

fig3.update_layout(
    coloraxis_showscale=False
)

fig3 = apply_dark_theme(fig3)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# =========================================================
# DAILY SALES TREND
# =========================================================

st.markdown("---")

st.subheader("📅 Daily Revenue Trend")

daily_sales = (
    filtered_df
    .groupby(filtered_df["InvoiceDate"].dt.date)
    ["Revenue"]
    .sum()
    .reset_index()
)

fig4 = px.area(
    daily_sales,
    x="InvoiceDate",
    y="Revenue",
    color_discrete_sequence=["#F97316"],
    title="Daily Revenue Analysis"
)

fig4.update_traces(
    opacity=0.7
)

fig4 = apply_dark_theme(fig4)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# =========================================================
# COUNTRY DEMAND HEATMAP
# =========================================================

st.markdown("---")

st.subheader("🔥 Revenue Heatmap")

heatmap_df = (
    filtered_df
    .pivot_table(
        values="Revenue",
        index=filtered_df["InvoiceDate"].dt.month,
        columns="Country",
        aggfunc="sum"
    )
    .fillna(0)
)

top_heatmap_countries = (
    country_revenue["Country"]
    .head(8)
    .tolist()
)

heatmap_df = heatmap_df[
    [
        country for country in top_heatmap_countries
        if country in heatmap_df.columns
    ]
]

fig_heat = px.imshow(
    heatmap_df,
    aspect="auto",
    text_auto=True,
    color_continuous_scale="Oranges"
)

fig_heat.update_layout(
    xaxis_title="Country",
    yaxis_title="Month"
)

fig_heat = apply_dark_theme(fig_heat)

st.plotly_chart(
    fig_heat,
    use_container_width=True
)

# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.markdown("---")

st.subheader("⚙️ AI Model Performance")

st.dataframe(
    metrics_df,
    use_container_width=True,
    height=350
)

# =========================================================
# EXECUTIVE INSIGHTS
# =========================================================

st.markdown("---")

st.subheader("🧠 AI Executive Insights")

top_country = (
    country_revenue
    .iloc[0]["Country"]
)

top_product = (
    top_products
    .iloc[0]["Description"]
)

st.info(f"""
• Total platform revenue reached ${total_revenue:,.0f}

• Highest revenue contribution observed from {top_country}

• Best-performing product category: {top_product}

• Average order value currently at ${avg_order_value:,.2f}

• AI forecasting and operational monitoring systems active
""")

# =========================================================
# AI RECOMMENDATION ENGINE
# =========================================================

st.markdown("---")

st.subheader("🤖 AI Strategic Recommendations")

if avg_order_value > 500:
    st.success(
        "Average order value indicates strong premium customer activity."
    )

if total_customers < 1000:
    st.warning(
        "Customer acquisition growth opportunity detected."
    )

if total_revenue > 1000000:
    st.info(
        "Revenue performance exceeds enterprise benchmark threshold."
    )

st.error(
    "Recommendation: Focus expansion efforts on high-performing countries and top-selling product categories."
)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "NeuralRetail AI • Executive Intelligence • Amdox Technologies"
)

