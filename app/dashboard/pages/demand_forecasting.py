# =========================================================
# Demand Forecasting Dashboard
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Demand Forecasting", layout="wide")

# =========================================================
# TITLE
# =========================================================

st.title("📈 Demand Forecasting Intelligence")

st.markdown("""
AI-powered retail sales forecasting and trend analytics.
""")

# =========================================================
# SIMULATED FORECAST DATA
# (Replace later with real outputs)
# =========================================================

np.random.seed(42)

dates = pd.date_range(start="2025-01-01", periods=120)

actual_sales = np.random.randint(15000, 45000, size=120)

forecast_sales = actual_sales + np.random.randint(-2500, 2500, size=120)

upper_bound = forecast_sales + 3000

lower_bound = forecast_sales - 3000

forecast_df = pd.DataFrame(
    {
        "Date": dates,
        "Actual": actual_sales,
        "Forecast": forecast_sales,
        "Upper_Bound": upper_bound,
        "Lower_Bound": lower_bound,
    }
)

# =========================================================
# KPI SECTION
# =========================================================

st.markdown("## 📌 Forecasting KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Best Model", "XGBoost")

with col2:
    st.metric("Forecast MAPE", "21.45%", "-3.2%")

with col3:
    st.metric("Forecast Horizon", "30 Days")

with col4:
    st.metric("Confidence", "89%")

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("Forecast Controls")

forecast_days = st.sidebar.slider(
    "Forecast Horizon", min_value=7, max_value=90, value=30
)

selected_model = st.sidebar.selectbox(
    "Forecast Model", ["Prophet", "XGBoost", "Ensemble", "LSTM"]
)

# =========================================================
# FORECAST TREND
# =========================================================

st.markdown("---")

st.subheader("📊 Forecast Trend")

fig_forecast = go.Figure()

# Actual Sales

fig_forecast.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Actual"],
        mode="lines",
        name="Actual Sales",
    )
)

# Forecast

fig_forecast.add_trace(
    go.Scatter(
        x=forecast_df["Date"], y=forecast_df["Forecast"], mode="lines", name="Forecast"
    )
)

# Upper Bound

fig_forecast.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Upper_Bound"],
        mode="lines",
        line=dict(width=0),
        showlegend=False,
    )
)

# Lower Bound + Fill

fig_forecast.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Lower_Bound"],
        mode="lines",
        fill="tonexty",
        fillcolor="rgba(0,100,255,0.2)",
        line=dict(width=0),
        name="Confidence Interval",
    )
)

fig_forecast.update_layout(
    title="Sales Forecast with Confidence Interval",
    xaxis_title="Date",
    yaxis_title="Sales",
)

st.plotly_chart(fig_forecast, use_container_width=True)

# =========================================================
# MODEL COMPARISON
# =========================================================

st.markdown("---")

st.subheader("🏆 Forecast Model Comparison")

comparison_df = pd.DataFrame(
    {
        "Model": ["Prophet", "XGBoost", "Ensemble", "LSTM"],
        "MAPE (%)": [30.75, 21.45, 18.20, 16.80],
    }
)

fig_models = px.bar(
    comparison_df, x="Model", y="MAPE (%)", title="Forecast Accuracy Comparison"
)

st.plotly_chart(fig_models, use_container_width=True)

# =========================================================
# MONTHLY SALES PATTERN
# =========================================================

st.markdown("---")

st.subheader("📅 Monthly Sales Pattern")

forecast_df["Month"] = forecast_df["Date"].dt.month_name()

monthly_sales = forecast_df.groupby("Month")["Actual"].mean().reset_index()

fig_monthly = px.line(
    monthly_sales, x="Month", y="Actual", markers=True, title="Average Monthly Sales"
)

st.plotly_chart(fig_monthly, use_container_width=True)

# =========================================================
# ACTUAL VS PREDICTED
# =========================================================

st.markdown("---")

st.subheader("🎯 Actual vs Predicted")

fig_scatter = px.scatter(
    forecast_df,
    x="Actual",
    y="Forecast",
    trendline="ols",
    title="Actual vs Forecasted Sales",
)

st.plotly_chart(fig_scatter, use_container_width=True)

# =========================================================
# FORECAST TABLE
# =========================================================

st.markdown("---")

st.subheader("📋 Forecast Data")

st.dataframe(forecast_df.tail(forecast_days), use_container_width=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Forecasting Intelligence Module")
