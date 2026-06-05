import streamlit as st
import requests

from utils.theme import load_css

load_css()

st.set_page_config(page_title="Live Churn Prediction", page_icon="⚠️", layout="wide")

st.title("⚠️ Live Churn Prediction")

st.markdown("""
Real-time customer churn prediction powered by FastAPI and XGBoost.
""")

# =========================================================
# USER INPUTS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    recency = st.number_input("Recency", min_value=0.0, value=20.0)

with col2:
    frequency = st.number_input("Frequency", min_value=1.0, value=5.0)

with col3:
    monetary = st.number_input("Monetary", min_value=0.0, value=400.0)

# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button("Predict Churn Risk"):
    payload = {"Recency": recency, "Frequency": frequency, "Monetary": monetary}

    try:
        response = requests.post(
            "https://neuralretail-ai-sales-intelligence.onrender.com/predict/churn",
            json=payload,
        )

        result = response.json()

        prediction = result["churn_prediction"]
        probability = result["churn_probability"]

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error(f"⚠️ High Churn Risk ({probability:.2%})")
        else:
            st.success(f"✅ Low Churn Risk ({probability:.2%})")

        st.progress(float(probability))

        st.metric("Churn Probability", f"{probability:.2%}")

    except Exception as e:
        st.error(f"API Connection Error: {e}")
