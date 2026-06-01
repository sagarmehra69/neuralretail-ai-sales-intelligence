import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from utils.chart_theme import apply_dark_theme
from utils.loader import (
    load_forecast_data,
    load_churn_data,
    load_inventory_data,
    load_model_metrics,
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Executive Overview", layout="wide")

# =========================================================
# LOAD DATA
# =========================================================

forecast_df = load_forecast_data()

churn_df = load_churn_data()

inventory_df = load_inventory_data()

metrics_df = load_model_metrics()

# =========================================================
# TITLE
# =========================================================

st.title("🧠 NeuralRetail AI")

st.markdown("""
Enterprise AI-powered retail intelligence and forecasting platform.
""")

# =========================================================
# GLOBAL KPIs
# =========================================================

latest_sales = forecast_df["Actual_Sales"].iloc[-1]
latest_forecast = forecast_df["Forecasted_Sales"].iloc[-1]
avg_churn = churn_df["Churn_Probability"].mean()
inventory_risk = inventory_df["Inventory_Risk_Score"].mean()
total_products = len(inventory_df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Latest Sales", f"{latest_sales:,.0f}")

with col2:
    st.metric("Avg Churn Risk", f"{avg_churn:.2f}")

with col3:
    st.metric("Inventory Risk", f"{inventory_risk:.2f}")

with col4:
    st.metric("Products Tracked", total_products)

# =========================================================
# SALES TREND
# =========================================================

st.markdown("---")

st.subheader("📈 Sales Forecast Trend")

fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(
        x=forecast_df["Date"], y=forecast_df["Actual_Sales"], name="Actual Sales"
    )
)

fig1.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Forecasted_Sales"],
        name="Forecasted Sales",
    )
)
fig1 = apply_dark_theme(fig1)

st.plotly_chart(fig1, use_container_width=True)

# =========================================================
# CHURN DISTRIBUTION
# =========================================================

st.markdown("---")

st.subheader("👥 Customer Churn Distribution")

fig2 = px.histogram(churn_df, x="Churn_Probability", nbins=30)
fig2 = apply_dark_theme(fig2)

st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# INVENTORY RISK
# =========================================================

st.markdown("---")

st.subheader("📦 Inventory Risk Overview")

fig3 = px.histogram(inventory_df, x="Inventory_Risk_Score", nbins=30)
fig3 = apply_dark_theme(fig3)

st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.markdown("---")

st.subheader("⚙️ Model Performance Metrics")

st.dataframe(metrics_df, use_container_width=True)

# =========================================================
# SYSTEM STATUS
# =========================================================

st.markdown("---")

st.success("✅ All AI systems operational")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Executive Command Center")
