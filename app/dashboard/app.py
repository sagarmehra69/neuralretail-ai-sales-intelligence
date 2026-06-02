import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NeuralRetail AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# LOAD CSS
# =========================================================


def load_css():

    with open("app/dashboard/assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.title("🧠 NeuralRetail AI")

    st.markdown("""
    Enterprise Retail Intelligence Platform
    """)

    st.markdown("---")

    st.subheader("📡 System Status")

    st.success("Forecast Engine Online")

    st.success("Churn Engine Online")

    st.success("Inventory Engine Online")

    st.markdown("---")

    st.subheader("⚙️ Platform Stack")

    st.markdown("""
    - Prophet Forecasting
    - XGBoost Models
    - Churn Prediction
    - Inventory Intelligence
    - Streamlit Dashboard
    - ML Analytics Pipeline
    """)

    st.markdown("---")

    st.caption("Built with AI + Data Science")

# =========================================================
# MAIN PAGE
# =========================================================

st.title("🧠 NeuralRetail AI")

st.markdown("""
Welcome to the enterprise AI retail intelligence platform.

Use the sidebar to navigate between intelligence modules.
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📈 Forecasting Intelligence")

with col2:
    st.info("👥 Customer Intelligence")

with col3:
    st.info("📦 Inventory Intelligence")

st.markdown("---")

st.success("✅ Platform Operational")


# =========================================================
# NeuralRetail AI - Main Command Center
# Amdox Technologies
# =========================================================

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# from utils.chart_theme import apply_dark_theme

# from utils.loader import (
#     load_sales_data,
#     load_forecast_data,
#     load_inventory_data,
#     load_churn_data,
#     load_model_metrics,
# )

# # =========================================================
# # PAGE CONFIG
# # =========================================================

# st.set_page_config(
#     page_title="NeuralRetail AI",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # =========================================================
# # LOAD CSS
# # =========================================================


# def load_css():

#     with open("app/dashboard/assets/style.css") as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# load_css()

# # =========================================================
# # LOAD DATA
# # =========================================================

# sales_df = load_sales_data()

# forecast_df = load_forecast_data()

# inventory_df = load_inventory_data()

# churn_df = load_churn_data()

# metrics_df = load_model_metrics()

# # =========================================================
# # DATA PREPROCESSING
# # =========================================================

# sales_df["invoicedate"] = pd.to_datetime(sales_df["invoicedate"])

# sales_df["Revenue"] = sales_df["quantity"] * sales_df["unitprice"]

# # =========================================================
# # GLOBAL KPIs
# # =========================================================

# total_revenue = sales_df["Revenue"].sum()

# total_orders = sales_df["invoiceno"].nunique()

# total_customers = sales_df["customerid"].nunique()

# total_products = sales_df["stockcode"].nunique()

# avg_order_value = total_revenue / total_orders

# forecast_accuracy = round(
#     100
#     - (forecast_df["Forecast_Error"].abs().mean() / forecast_df["Actual_Sales"].mean())
#     * 100,
#     2,
# )

# avg_churn = round(churn_df["Churn_Probability"].mean(), 2)

# inventory_risk = round(inventory_df["Inventory_Risk_Score"].mean(), 2)

# # =========================================================
# # HERO SECTION
# # =========================================================

# st.title("🧠 NeuralRetail AI")

# st.markdown("""
# Enterprise AI-powered Retail Intelligence & Forecasting Platform
# """)

# # =========================================================
# # KPI ROW
# # =========================================================

# st.markdown("## 📌 Executive KPIs")

# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     st.metric("Total Revenue", f"${total_revenue:,.0f}")

# with col2:
#     st.metric("Total Orders", f"{total_orders:,}")

# with col3:
#     st.metric("Customers", f"{total_customers:,}")

# with col4:
#     st.metric("Products", f"{total_products:,}")

# with col5:
#     st.metric("Avg Order Value", f"${avg_order_value:,.2f}")

# # =========================================================
# # AI SYSTEM KPIs
# # =========================================================

# st.markdown("---")

# st.markdown("## 🤖 AI System Intelligence")

# col6, col7, col8 = st.columns(3)

# with col6:
#     st.metric("Forecast Accuracy", f"{forecast_accuracy}%")

# with col7:
#     st.metric("Avg Churn Risk", f"{avg_churn}")

# with col8:
#     st.metric("Inventory Risk", f"{inventory_risk}")


# # =========================================================
# # MODEL PERFORMANCE
# # =========================================================

# st.markdown("---")

# st.subheader("⚙️ AI Model Performance")

# st.dataframe(metrics_df, use_container_width=True)

# # =========================================================
# # SYSTEM STATUS
# # =========================================================

# st.markdown("---")

# st.success("✅ All AI Systems Operational")

# # =========================================================
# # FOOTER
# # =========================================================

# st.markdown("---")

# st.caption(
#     "NeuralRetail AI • Enterprise Retail Intelligence Platform • Amdox Technologies"
# )
