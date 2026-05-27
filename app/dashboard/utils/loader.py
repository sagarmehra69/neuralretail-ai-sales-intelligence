# =========================================================
# Centralized Data Loader
# =========================================================

import pandas as pd
import streamlit as st

# =========================================================
# FORECAST DATA
# =========================================================


@st.cache_data
def load_forecast_data():

    df = pd.read_csv(r"D:\NuralRetail\app\dashboard\data\forecast_results.csv")

    return df


# =========================================================
# CHURN DATA
# =========================================================


@st.cache_data
def load_churn_data():

    df = pd.read_csv(r"D:\NuralRetail\app\dashboard\data\churn_predictions.csv")

    return df


# =========================================================
# INVENTORY DATA
# =========================================================


@st.cache_data
def load_inventory_data():

    df = pd.read_csv(r"D:\NuralRetail\app\dashboard\data\inventory_risk.csv")

    return df


# =========================================================
# MODEL METRICS
# =========================================================


@st.cache_data
def load_model_metrics():

    df = pd.read_csv(r"D:\NuralRetail\app\dashboard\data\model_metrics.csv")

    return df

