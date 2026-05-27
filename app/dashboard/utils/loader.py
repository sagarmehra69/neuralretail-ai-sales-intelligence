import pandas as pd
import streamlit as st
from pathlib import Path

# =========================================================
# BASE DATA PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

# =========================================================
# FORECAST DATA
# =========================================================


@st.cache_data
def load_forecast_data():

    return pd.read_csv(DATA_DIR / "forecast_results.csv")


# =========================================================
# CHURN DATA
# =========================================================


@st.cache_data
def load_churn_data():

    return pd.read_csv(DATA_DIR / "churn_predictions.csv")


# =========================================================
# INVENTORY DATA
# =========================================================


@st.cache_data
def load_inventory_data():

    return pd.read_csv(DATA_DIR / "inventory_risk.csv")


# =========================================================
# MODEL METRICS
# =========================================================


@st.cache_data
def load_model_metrics():

    return pd.read_csv(DATA_DIR / "model_metrics.csv")
