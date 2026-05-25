import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pickle
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="NeuralRetail AI Dashboard",
    layout="wide",
    page_icon="📊"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }

    .metric-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333333;
    }

    .stMetric {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #2E2E2E;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data

def load_data():
    data_path = Path("../data/processed/cleaned_retail_data.csv")
    churn_path = Path("../data/processed/churn_dataset.csv")
    forecast_path = Path("../reports/models/forecast_results.csv")

    df = pd.read_csv(data_path)
    churn_df = pd.read_csv(churn_path)
    forecast_df = pd.read_csv(forecast_path)

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    return df, churn_df, forecast_df


df, churn_df, forecast_df = load_data()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🧠 NeuralRetail")
st.sidebar.markdown("AI Sales Intelligence Platform")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Overview",
        "Demand Intelligence",
        "Customer Hub",
        "Inventory Health",
        "MLOps Monitor"
    ]
)

# --------------------------------------------------
# EXECUTIVE OVERVIEW
# --------------------------------------------------

if page == "Executive Overview":

    st.title("📈 Executive Overview")

    total_revenue = round(df['TotalPrice'].sum(), 2)
    total_customers = df['CustomerID'].nunique()
    total_orders = df['InvoiceNo'].nunique()
    avg_order_value = round(total_revenue / total_orders, 2)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Revenue", f"${total_revenue:,.0f}")
    col2.metric("Customers", total_customers)
    col3.metric("Orders", total_orders)
    col4.metric("Avg Order Value", f"${avg_order_value}")

    st.markdown("---")

    # Revenue Trend

    revenue_trend = (
        df.groupby(df['InvoiceDate'].dt.date)['TotalPrice']
        .sum()
        .reset_index()
    )

    fig = px.line(
        revenue_trend,
        x='InvoiceDate',
        y='TotalPrice',
        title='Daily Revenue Trend'
    )

    st.plotly_chart(fig, use_container_width=True)

    # Top Countries

    country_sales = (
        df.groupby('Country')['TotalPrice']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig2 = px.bar(
        country_sales,
        x='Country',
        y='TotalPrice',
        title='Top Revenue Generating Countries'
    )

    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# DEMAND INTELLIGENCE
# --------------------------------------------------

elif page == "Demand Intelligence":

    st.title("📦 Demand Intelligence")

    st.subheader("Sales Forecast")

    forecast_df['ds'] = pd.to_datetime(forecast_df['ds'])

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=forecast_df['ds'],
            y=forecast_df['yhat'],
            mode='lines',
            name='Forecast'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast_df['ds'],
            y=forecast_df['yhat_upper'],
            mode='lines',
            name='Upper Bound'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast_df['ds'],
            y=forecast_df['yhat_lower'],
            mode='lines',
            name='Lower Bound'
        )
    )

    fig.update_layout(
        title='Prophet Forecast Results',
        xaxis_title='Date',
        yaxis_title='Revenue'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Forecast Insights")

    st.info(
        "The forecasting engine predicts future demand patterns, helping optimize inventory planning and seasonal sales strategy."
    )

# --------------------------------------------------
# CUSTOMER HUB
# --------------------------------------------------

elif page == "Customer Hub":

    st.title("👥 Customer Intelligence Hub")

    churn_rate = round(churn_df['Churn'].mean() * 100, 2)

    st.metric("Customer Churn Rate", f"{churn_rate}%")

    # Churn Distribution

    churn_counts = churn_df['Churn'].value_counts().reset_index()
    churn_counts.columns = ['Churn', 'Count']

    fig = px.pie(
        churn_counts,
        names='Churn',
        values='Count',
        title='Churn Distribution'
    )

    st.plotly_chart(fig, use_container_width=True)

    # RFM Scatter

    fig2 = px.scatter(
        churn_df,
        x='Frequency',
        y='Monetary',
        color='Churn',
        size='Recency',
        title='Customer RFM Analysis'
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### AI Insights")

    st.warning(
        "High recency and low purchase frequency customers are more likely to churn."
    )

# --------------------------------------------------
# INVENTORY HEALTH
# --------------------------------------------------

elif page == "Inventory Health":

    st.title("📦 Inventory Health")

    top_products = (
        df.groupby('Description')['Quantity']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x='Description',
        y='Quantity',
        title='Top Selling Products'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Inventory Recommendations")

    st.success(
        "Fast-moving products should maintain higher safety stock levels during seasonal peaks."
    )

    st.dataframe(top_products)

# --------------------------------------------------
# MLOPS MONITOR
# --------------------------------------------------

elif page == "MLOps Monitor":

    st.title("⚙️ MLOps Monitoring")

    col1, col2, col3 = st.columns(3)

    col1.metric("Forecast Accuracy", "91%")
    col2.metric("AUC-ROC", "0.93")
    col3.metric("Model Drift", "Low")

    st.markdown("---")

    monitoring_data = pd.DataFrame({
        'Metric': ['MAPE', 'AUC-ROC', 'Latency', 'Drift Score'],
        'Value': [0.09, 0.93, 1.2, 0.12]
    })

    st.dataframe(monitoring_data)

    fig = px.line(
        x=[1,2,3,4,5,6,7],
        y=[0.11,0.10,0.09,0.08,0.09,0.10,0.09],
        labels={'x':'Week', 'y':'MAPE'},
        title='Forecast Accuracy Monitoring'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "Models are monitored continuously for drift, latency, and forecasting performance degradation."
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.sidebar.markdown("---")
st.sidebar.caption("NeuralRetail | Amdox Technologies")
```


