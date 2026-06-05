# =========================================================
# NeuralRetail AI — Demand Forecasting Intelligence
# Amdox Technologies
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from auth_guard import check_auth
from utils.theme import load_css
from utils.loader import load_forecast_data
from utils.chart_theme import apply_dark_theme


check_auth()
# =========================================================
# LOAD CSS
# =========================================================

load_css()

# =========================================================
# PAGE HEADER
# =========================================================

st.title("📈 Demand Forecasting Intelligence")

st.markdown("""
Advanced AI-powered retail demand forecasting and predictive sales intelligence platform.
""")

# =========================================================
# LOAD DATA
# =========================================================

forecast_df = load_forecast_data()

# =========================================================
# STANDARDIZE COLUMNS
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
# DATA PROCESSING
# =========================================================

forecast_df["Date"] = pd.to_datetime(
    forecast_df["Date"]
)

forecast_df = (
    forecast_df
    .sort_values(by="Date")
    .dropna()
)

# =========================================================
# FEATURE ENGINEERING
# =========================================================

forecast_df["Rolling_Actual"] = (
    forecast_df["Actual"]
    .rolling(7)
    .mean()
)

forecast_df["Rolling_Forecast"] = (
    forecast_df["Forecast"]
    .rolling(7)
    .mean()
)

forecast_df["Day_Name"] = (
    forecast_df["Date"]
    .dt.day_name()
)

forecast_df["Month"] = (
    forecast_df["Date"]
    .dt.strftime("%b")
)

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🎯 Forecast Controls")

forecast_days = st.sidebar.slider(
    "Forecast Horizon",
    min_value=7,
    max_value=90,
    value=30,
)

selected_model = st.sidebar.selectbox(
    "Forecast Model",
    [
        "Ensemble",
        "XGBoost",
        "Prophet",
        "LSTM"
    ]
)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [
        forecast_df["Date"].min(),
        forecast_df["Date"].max()
    ]
)

# =========================================================
# FILTER DATA
# =========================================================

filtered_df = forecast_df[
    (forecast_df["Date"] >= pd.to_datetime(date_range[0])) &
    (forecast_df["Date"] <= pd.to_datetime(date_range[1]))
]

# =========================================================
# KPI SECTION
# =========================================================

st.markdown("## 📌 Forecasting KPI Overview")

mape_df = filtered_df[
    filtered_df["Actual"] != 0
]

mape = round(
    (
        np.mean(
            np.abs(
                mape_df["Forecast_Error"]
            ) / mape_df["Actual"]
        )
    ) * 100,
    2
)

forecast_accuracy = round(
    100 - mape,
    2
)

avg_daily_demand = int(
    filtered_df["Actual"].mean()
)

forecast_variance = round(
    filtered_df["Forecast_Error"].std(),
    2
)

total_forecast = int(
    filtered_df["Forecast"].sum()
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "🤖 Forecast Model",
        selected_model
    )

with col2:
    st.metric(
        "🎯 Forecast Accuracy",
        f"{forecast_accuracy}%"
    )

with col3:
    st.metric(
        "📉 Forecast MAPE",
        f"{mape}%"
    )

with col4:
    st.metric(
        "📦 Avg Daily Demand",
        f"{avg_daily_demand:,}"
    )

with col5:
    st.metric(
        "💰 Forecast Volume",
        f"{total_forecast:,}"
    )

# =========================================================
# ACTUAL VS FORECAST
# =========================================================

st.markdown("---")

st.subheader("📊 Actual vs Forecasted Sales")

fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["Actual"],
        mode="lines",
        name="Actual Sales",
        line=dict(
            color="#2C71E1",
            width=3
        )
    )
)

fig1.add_trace(
    go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["Forecast"],
        mode="lines",
        name="Forecasted Sales",
        line=dict(
            color="#F97316",
            width=3,
            dash="dash"
        )
    )
)

fig1.update_layout(
    title="Demand Forecast Trend",
    xaxis_title="Date",
    yaxis_title="Sales",
    hovermode="x unified"
)

fig1 = apply_dark_theme(fig1)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =========================================================
# ROLLING FORECAST TREND
# =========================================================

st.markdown("---")

st.subheader("📈 Rolling Forecast Trend")

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["Rolling_Actual"],
        mode="lines",
        name="7-Day Rolling Actual",
        line=dict(
            color="#2C71E1",
            width=3
        )
    )
)

fig2.add_trace(
    go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["Rolling_Forecast"],
        mode="lines",
        name="7-Day Rolling Forecast",
        line=dict(
            color="#F97316",
            width=3
        )
    )
)

fig2.update_layout(
    title="Rolling Forecast Analysis",
    xaxis_title="Date",
    yaxis_title="Sales"
)

fig2 = apply_dark_theme(fig2)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =========================================================
# FORECAST ERROR ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📉 Forecast Error Analysis")

fig3 = px.area(
    filtered_df,
    x="Date",
    y="Forecast_Error",
    color_discrete_sequence=["#F97316"],
    title="Forecast Error Over Time"
)

fig3.update_traces(
    opacity=0.7
)

fig3 = apply_dark_theme(fig3)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# =========================================================
# WEEKLY DEMAND PATTERN
# =========================================================

st.markdown("---")

st.subheader("📅 Weekly Demand Pattern")

weekday_sales = (
    filtered_df
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
    ordered=True
)

weekday_sales = weekday_sales.sort_values(
    by="Day_Name"
)

fig4 = px.bar(
    weekday_sales,
    x="Day_Name",
    y="Actual",
    color="Actual",
    color_continuous_scale=[
        "#F59E0B",
        "#F97316",
        "#EA580C"
    ],
    title="Average Demand by Weekday"
)

fig4.update_layout(
    coloraxis_showscale=False
)

fig4 = apply_dark_theme(fig4)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# =========================================================
# MONTHLY FORECAST TREND
# =========================================================

st.markdown("---")

st.subheader("🗓️ Monthly Sales Trend")

monthly_sales = (
    filtered_df
    .groupby("Month")
    [["Actual", "Forecast"]]
    .sum()
    .reset_index()
)

fig5 = go.Figure()

fig5.add_trace(
    go.Bar(
        x=monthly_sales["Month"],
        y=monthly_sales["Actual"],
        name="Actual",
        marker_color="#2C71E1"
    )
)

fig5.add_trace(
    go.Bar(
        x=monthly_sales["Month"],
        y=monthly_sales["Forecast"],
        name="Forecast",
        marker_color="#F97316"
    )
)

fig5.update_layout(
    barmode="group",
    title="Monthly Forecast Comparison",
    xaxis_title="Month",
    yaxis_title="Sales"
)

fig5 = apply_dark_theme(fig5)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# =========================================================
# DEMAND HEATMAP
# =========================================================

st.markdown("---")

st.subheader("🔥 Demand Heatmap")

heatmap_df = (
    filtered_df
    .pivot_table(
        values="Actual",
        index=filtered_df["Date"].dt.month,
        columns=filtered_df["Date"].dt.dayofweek,
        aggfunc="mean"
    )
)

fig_heat = px.imshow(
    heatmap_df,
    aspect="auto",
    color_continuous_scale="Oranges",
    text_auto=True
)

fig_heat.update_layout(
    xaxis_title="Day of Week",
    yaxis_title="Month"
)

fig_heat = apply_dark_theme(fig_heat)

st.plotly_chart(
    fig_heat,
    use_container_width=True
)

# =========================================================
# AI FORECAST INSIGHTS
# =========================================================

st.markdown("---")

st.subheader("🧠 AI Forecast Insights")

highest_day = (
    weekday_sales
    .sort_values(
        by="Actual",
        ascending=False
    )
    .iloc[0]["Day_Name"]
)

lowest_day = (
    weekday_sales
    .sort_values(
        by="Actual",
        ascending=True
    )
    .iloc[0]["Day_Name"]
)

st.info(f"""
• Forecast model currently operating at {forecast_accuracy}% accuracy

• Average daily demand is {avg_daily_demand:,} units

• Highest customer demand observed on {highest_day}

• Lowest customer demand observed on {lowest_day}

• Forecast volatility score: {forecast_variance}

• Forecast engine configured for {forecast_days}-day prediction horizon
""")

# =========================================================
# AI RECOMMENDATION ENGINE
# =========================================================

st.markdown("---")

st.subheader("🤖 AI Demand Recommendations")

if mape < 10:
    st.success(
        "Forecast model is performing within enterprise production threshold."
    )

if forecast_variance > 100:
    st.warning(
        "Demand volatility is elevated. Increase inventory safety stock."
    )

if avg_daily_demand > 5000:
    st.info(
        "High product demand detected. Supply chain scaling recommended."
    )

st.error(
    "Recommendation: Monitor seasonal spikes and optimize inventory replenishment cycles."
)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "NeuralRetail AI • Demand Forecasting Intelligence • Amdox Technologies"
)

