
# =========================================================
# NeuralRetail - Demand Forecasting Dashboard
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from utils.loader import load_forecast_data
from utils.chart_theme import apply_dark_theme
# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Demand Forecasting Intelligence",
    layout="wide"
)

# =========================================================
# TITLE
# =========================================================

st.title("📈 Demand Forecasting Intelligence")

st.markdown("""
AI-powered retail demand forecasting and forecasting analytics dashboard.
""")

# =========================================================
# LOAD DATA
# =========================================================

forecast_df = load_forecast_data()

# =========================================================
# COLUMN STANDARDIZATION
# =========================================================

forecast_df = forecast_df.rename(
    columns={
        "Actual_Sales": "Actual",
        "Forecasted_Sales": "Forecast",
    }
)

# =========================================================
# VALIDATION
# =========================================================

required_cols = [
    "Date",
    "Actual",
    "Forecast",
    "Forecast_Error",
]

missing_cols = [
    col for col in required_cols
    if col not in forecast_df.columns
]

if missing_cols:
    st.error(f"Missing columns: {missing_cols}")
    st.stop()



# =========================================================
# DATA CLEANING
# =========================================================

forecast_df = forecast_df.dropna()

forecast_df = forecast_df[
    forecast_df["Actual"] >= 0
]

forecast_df = forecast_df[
    forecast_df["Forecast"] >= 0
]

# =========================================================
# DATA TYPES
# =========================================================

forecast_df["Date"] = pd.to_datetime(
    forecast_df["Date"]
)

forecast_df = forecast_df.sort_values(
    by="Date"
)

# =========================================================
# FEATURE ENGINEERING
# =========================================================

# Daily Forecast Accuracy

forecast_df["Daily_Accuracy"] = np.where( 
    forecast_df["Actual"] != 0,
    100 - 
    ( np.abs(forecast_df["Forecast_Error"]) 
     / forecast_df["Actual"] ) * 100, 0 )

forecast_df["Daily_Accuracy"] = (
    forecast_df["Daily_Accuracy"]
    .clip(lower=0)
)

# Rolling Trends

forecast_df["Rolling_Actual"] = (
    forecast_df["Actual"]
    .rolling(window=7)
    .mean()
)

forecast_df["Rolling_Forecast"] = (
    forecast_df["Forecast"]
    .rolling(window=7)
    .mean()
)

# Cumulative Trends

forecast_df["Cumulative_Actual"] = (
    forecast_df["Actual"]
    .cumsum()
)

forecast_df["Cumulative_Forecast"] = (
    forecast_df["Forecast"]
    .cumsum()
)

# Weekday Analysis

forecast_df["Day_Name"] = (
    forecast_df["Date"]
    .dt.day_name()
)

# Monthly Analysis

forecast_df["Month"] = (
    forecast_df["Date"]
    .dt.strftime("%b")
)



# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("Forecast Controls")

forecast_days = st.sidebar.slider(
    "Forecast Horizon",
    min_value=7,
    max_value=90,
    value=30,
)

selected_model = st.sidebar.selectbox(
    "Forecast Model",
    ["XGBoost", "Prophet", "LSTM", "Ensemble"]
)

# =========================================================
# KPI SECTION
# =========================================================

st.markdown("## 📌 Forecasting KPIs")

col1, col2, col3, col4 = st.columns(4)


mape_df = forecast_df[
    forecast_df["Actual"] != 0
]

mape = round(
    (
        np.mean(
            np.abs(
                mape_df["Forecast_Error"]
            )
            / mape_df["Actual"]
        )
    ) * 100,
    2,
)

accuracy = round(100 - mape, 2)



avg_actual_sales = int(
    forecast_df["Actual"].mean()
)

avg_forecast_sales = int(
    forecast_df["Forecast"].mean()
)

with col1:
    st.metric(
        "Selected Model",
        selected_model
    )

with col2:
    st.metric(
        "Forecast MAPE",
        f"{mape}%"
    )

with col3:
    st.metric(
        "Forecast Accuracy",
        f"{accuracy}%"
    )

with col4:
    st.metric(
        "Avg Daily Demand",
        f"{avg_actual_sales:,}"
    )

# =========================================================
# FORECAST TREND
# =========================================================

st.markdown("---")

st.subheader("📊 Actual vs Forecasted Sales")

fig_forecast = go.Figure()
fig_forecast = apply_dark_theme(fig_forecast)
# Actual Sales

fig_forecast.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Actual"],
        mode="lines",
        name="Actual Sales",
    )
)

# Forecasted Sales

fig_forecast.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Forecast"],
        mode="lines",
        name="Forecasted Sales",
    )
)

fig_forecast.update_layout(
    title="Sales Forecast Trend",
    xaxis_title="Date",
    yaxis_title="Sales",
    hovermode="x unified",
)

st.plotly_chart(
    fig_forecast,
    use_container_width=True
)

# =========================================================
# ROLLING TREND ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📈 7-Day Rolling Forecast Trend")

fig_rolling = go.Figure()
fig_rolling = apply_dark_theme(fig_rolling)
fig_rolling.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Rolling_Actual"],
        mode="lines",
        name="Rolling Actual",
    )
)

fig_rolling.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Rolling_Forecast"],
        mode="lines",
        name="Rolling Forecast",
    )
)

fig_rolling.update_layout(
    title="Rolling Forecast Trend",
    xaxis_title="Date",
    yaxis_title="Sales",
)

st.plotly_chart(
    fig_rolling,
    use_container_width=True
)

# =========================================================
# FORECAST ERROR ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📉 Forecast Error Analysis")

fig_error = px.line(
    forecast_df,
    x="Date",
    y="Forecast_Error",
    title="Forecast Error Over Time",
)
fig_error = apply_dark_theme(fig_error)
st.plotly_chart(
    fig_error,
    use_container_width=True
)

# =========================================================
# DAILY FORECAST ACCURACY
# =========================================================

st.markdown("---")

st.subheader("🎯 Daily Forecast Accuracy")

fig_accuracy = px.line(
    forecast_df,
    x="Date",
    y="Daily_Accuracy",
    title="Daily Forecast Accuracy Trend",
)
fig_accuracy = apply_dark_theme(fig_accuracy)
st.plotly_chart(
    fig_accuracy,
    use_container_width=True
)

# =========================================================
# RESIDUAL DISTRIBUTION
# =========================================================

st.markdown("---")

st.subheader("📦 Forecast Residual Distribution")

fig_hist = px.histogram(
    forecast_df,
    x="Forecast_Error",
    nbins=30,
    title="Forecast Error Distribution",
)
fig_hist = apply_dark_theme(fig_hist)
st.plotly_chart(
    fig_hist,
    use_container_width=True
)

# =========================================================
# WEEKDAY DEMAND ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📅 Weekly Demand Pattern")

weekday_sales = (
    forecast_df
    .groupby("Day_Name")["Actual"]
    .mean()
    .reset_index()
)

weekday_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

weekday_sales["Day_Name"] = pd.Categorical(
    weekday_sales["Day_Name"],
    categories=weekday_order,
    ordered=True,
)

weekday_sales = weekday_sales.sort_values(
    by="Day_Name"
)

fig_weekday = px.bar(
    weekday_sales,
    x="Day_Name",
    y="Actual",
    title="Average Sales by Weekday",
)
fig_weekday = apply_dark_theme(fig_weekday)
st.plotly_chart(
    fig_weekday,
    use_container_width=True
)

# =========================================================
# MONTHLY SALES TREND
# =========================================================

st.markdown("---")

st.subheader("📆 Monthly Sales Trend")

monthly_sales = (
    forecast_df
    .groupby("Month")["Actual"]
    .mean()
    .reset_index()
)

fig_monthly = px.line(
    monthly_sales,
    x="Month",
    y="Actual",
    markers=True,
    title="Average Monthly Sales",
)
fig_monthly = apply_dark_theme(fig_monthly)
st.plotly_chart(
    fig_monthly,
    use_container_width=True
)

# =========================================================
# CUMULATIVE FORECAST TREND
# =========================================================

st.markdown("---")

st.subheader("📊 Cumulative Sales vs Forecast")

fig_cumulative = go.Figure()

fig_cumulative.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Cumulative_Actual"],
        mode="lines",
        name="Cumulative Actual",
    )
)

fig_cumulative.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Cumulative_Forecast"],
        mode="lines",
        name="Cumulative Forecast",
    )
)

fig_cumulative.update_layout(
    title="Cumulative Forecast Performance",
    xaxis_title="Date",
    yaxis_title="Cumulative Sales",
)
fig_cumulative = apply_dark_theme(fig_cumulative)
st.plotly_chart(
    fig_cumulative,
    use_container_width=True
)

# =========================================================
# ACTUAL VS FORECAST SCATTER
# =========================================================

st.markdown("---")

st.subheader("🔍 Actual vs Forecast Scatter")

fig_scatter = px.scatter(
    forecast_df,
    x="Actual",
    y="Forecast",
    trendline="ols",
    title="Actual vs Forecasted Sales",
)
fig_scatter = apply_dark_theme(fig_scatter)
st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

# =========================================================
# FORECAST TABLE
# =========================================================

st.markdown("---")

st.subheader("📋 Forecast Data")

st.dataframe(
    forecast_df.tail(forecast_days),
    use_container_width=True,
)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "NeuralRetail AI • Demand Forecasting Intelligence • Amdox Technologies"
)

