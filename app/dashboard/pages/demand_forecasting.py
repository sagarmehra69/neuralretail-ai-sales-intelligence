# =========================================================
# NeuralRetail AI - Demand Forecasting Intelligence
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from utils.theme import load_css
from utils.loader import load_forecast_data
from utils.chart_theme import apply_dark_theme

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Demand Forecasting Intelligence", layout="wide")

load_css()

# =========================================================
# TITLE
# =========================================================

st.title("📈 Demand Forecasting Intelligence")

st.markdown("""
AI-powered retail demand forecasting and sales trend intelligence platform.
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

missing_cols = [col for col in required_cols if col not in forecast_df.columns]

if missing_cols:
    st.error(f"Missing columns: {missing_cols}")

    st.stop()

# =========================================================
# DATA PROCESSING
# =========================================================

forecast_df["Date"] = pd.to_datetime(forecast_df["Date"])
forecast_df = forecast_df.sort_values(by="Date")
forecast_df = forecast_df.dropna()

# =========================================================
# FEATURE ENGINEERING
# =========================================================

forecast_df["Rolling_Actual"] = forecast_df["Actual"].rolling(7).mean()
forecast_df["Rolling_Forecast"] = forecast_df["Forecast"].rolling(7).mean()
forecast_df["Day_Name"] = forecast_df["Date"].dt.day_name()

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
    "Forecast Model", ["XGBoost", "Prophet", "LSTM", "Ensemble"]
)

# =========================================================
# KPI SECTION
# =========================================================

st.markdown("## 📌 Forecasting KPIs")

mape_df = forecast_df[forecast_df["Actual"] != 0]
mape = round((np.mean(np.abs(mape_df["Forecast_Error"]) / mape_df["Actual"])) * 100, 2)
forecast_accuracy = round(100 - mape, 2)
avg_daily_demand = int(forecast_df["Actual"].mean())
forecast_variance = round(forecast_df["Forecast_Error"].std(), 2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Forecast Model", selected_model)

with col2:
    st.metric("Forecast Accuracy", f"{forecast_accuracy}%")

with col3:
    st.metric("Forecast MAPE", f"{mape}%")

with col4:
    st.metric("Avg Daily Demand", f"{avg_daily_demand:,}")

# =========================================================
# ACTUAL VS FORECAST
# =========================================================

st.markdown("---")

st.subheader("📊 Actual vs Forecasted Sales")

fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Actual"],
        mode="lines",
        name="Actual Sales",
    )
)

fig1.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Forecast"],
        mode="lines",
        name="Forecasted Sales",
    )
)

fig1.update_layout(
    title="Demand Forecast Trend",
    xaxis_title="Date",
    yaxis_title="Sales",
    colorway=["#2C71E1", "#F97316"],
    hovermode="x unified",
)

fig1 = apply_dark_theme(fig1)

st.plotly_chart(fig1, use_container_width=True)

# =========================================================
# ROLLING FORECAST TREND
# =========================================================

st.markdown("---")

st.subheader("📈 Rolling Forecast Trend")

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Rolling_Actual"],
        mode="lines",
        name="Rolling Actual",
    )
)

fig2.add_trace(
    go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Rolling_Forecast"],
        mode="lines",
        name="Rolling Forecast",
    )
)

fig2.update_layout(
    title="7-Day Rolling Forecast Analysis",
    xaxis_title="Date",
    colorway=["#2C71E1", "#F97316"],
    yaxis_title="Sales",
)

fig2 = apply_dark_theme(fig2)

st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# FORECAST ERROR ANALYSIS
# =========================================================

st.markdown("---")

st.subheader("📉 Forecast Error Trend")

fig3 = px.line(
    forecast_df,
    x="Date",
    y="Forecast_Error",
    color_discrete_sequence=["#F97316"],
    title="Forecast Error Over Time",
)

fig3 = apply_dark_theme(fig3)

st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# WEEKLY DEMAND PATTERN
# =========================================================

st.markdown("---")

st.subheader("📅 Weekly Demand Pattern")

weekday_sales = forecast_df.groupby("Day_Name")["Actual"].mean().reset_index()

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
    weekday_sales["Day_Name"], categories=weekday_order, ordered=True
)

weekday_sales = weekday_sales.sort_values(by="Day_Name")

fig4 = px.bar(
    weekday_sales,
    x="Day_Name",
    y="Actual",
    title="Average Demand by Weekday",
)

fig4 = apply_dark_theme(fig4)

st.plotly_chart(fig4, use_container_width=True)

# =========================================================
# AI FORECAST INSIGHTS
# =========================================================

st.markdown("---")

st.subheader("🧠 AI Forecast Insights")

highest_day = weekday_sales.sort_values(by="Actual", ascending=False).iloc[0][
    "Day_Name"
]

lowest_day = weekday_sales.sort_values(by="Actual", ascending=True).iloc[0]["Day_Name"]

st.info(f"""
• Forecast model currently operating at {forecast_accuracy}% accuracy

• Average daily demand is {avg_daily_demand:,} units

• Highest demand observed on {highest_day}

• Lowest demand observed on {lowest_day}

• Forecast volatility score: {forecast_variance}
""")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("NeuralRetail AI • Demand Forecasting Intelligence • Amdox Technologies")
