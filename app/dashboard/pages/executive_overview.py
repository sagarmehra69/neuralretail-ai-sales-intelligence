# =========================================================
# NeuralRetail AI - Executive Overview
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.theme import load_css
from utils.chart_theme import apply_dark_theme
from utils.loader import load_sales_data, load_model_metrics

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Executive Overview", layout="wide")

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

sales_df["InvoiceDate"] = pd.to_datetime(sales_df["InvoiceDate"])

sales_df["Revenue"] = sales_df["Quantity"] * sales_df["UnitPrice"]

sales_df["YearMonth"] = sales_df["InvoiceDate"].dt.to_period("M").astype(str)

# =========================================================
# TITLE
# =========================================================

st.title("🧠 Executive Overview")

st.markdown("""
Enterprise retail performance and AI-powered business intelligence platform.
""")

# =========================================================
# EXECUTIVE KPIs
# =========================================================

total_revenue = sales_df["Revenue"].sum()

total_orders = sales_df["InvoiceNo"].nunique()

total_customers = sales_df["CustomerID"].nunique()

total_products = sales_df["StockCode"].nunique()

avg_order_value = total_revenue / total_orders

st.markdown("## 📌 Executive KPIs")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Revenue", f"${total_revenue:,.0f}")

with col2:
    st.metric("Orders", f"{total_orders:,}")

with col3:
    st.metric("Customers", f"{total_customers:,}")

with col4:
    st.metric("Products", f"{total_products:,}")

with col5:
    st.metric("Avg Order Value", f"${avg_order_value:,.2f}")

# =========================================================
# MONTHLY REVENUE TREND
# =========================================================

st.markdown("---")

st.subheader("📈 Monthly Revenue Trend")

monthly_revenue = sales_df.groupby("YearMonth")["Revenue"].sum().reset_index()

fig1 = px.line(
    monthly_revenue,
    x="YearMonth",
    y="Revenue",
    markers=True,
)

fig1.update_traces(line=dict(color="#F97316", width=4))

fig1 = apply_dark_theme(fig1)

st.plotly_chart(fig1, use_container_width=True)

# =========================================================
# REVENUE BY COUNTRY
# =========================================================

st.markdown("---")

st.subheader("🌍 Revenue by Country")

country_revenue = (
    sales_df.groupby("Country")["Revenue"]
    .sum()
    .reset_index()
    .sort_values(by="Revenue", ascending=False)
    .head(10)
)

fig2 = px.bar(
    country_revenue,
    x="Country",
    y="Revenue",
    color="Revenue",
    color_continuous_scale=["#F59E0B", "#F97316", "#EA580C"],
)

fig2 = apply_dark_theme(fig2)

st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# TOP PRODUCTS
# =========================================================

st.markdown("---")

st.subheader("🏆 Top Revenue Products")

top_products = (
    sales_df.groupby("Description")["Revenue"]
    .sum()
    .reset_index()
    .sort_values(by="Revenue", ascending=False)
    .head(10)
)

fig3 = px.bar(
    top_products,
    x="Revenue",
    y="Description",
    orientation="h",
    color="Revenue",
    color_continuous_scale=["#F59E0B", "#F97316", "#EA580C"],
)

fig3 = apply_dark_theme(fig3)

st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.markdown("---")

st.subheader("⚙️ AI Model Performance")

st.dataframe(metrics_df, use_container_width=True)

# =========================================================
# AI BUSINESS INSIGHTS
# =========================================================

st.markdown("---")

st.subheader("🧠 AI Business Insights")

top_country = country_revenue.iloc[0]["Country"]

top_product = top_products.iloc[0]["Description"]

st.info(f"""
• Total platform revenue reached ${total_revenue:,.0f}

• Highest revenue contribution from {top_country}

• Best performing product: {top_product}

• Average order value currently at ${avg_order_value:,.2f}

• AI forecasting and monitoring systems operational
""")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Executive Intelligence • Amdox Technologies")
