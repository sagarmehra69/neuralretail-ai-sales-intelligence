from fastapi import FastAPI
import pandas as pd

from api.schemas import ChurnRequest, ChurnResponse
from api.model_loader import churn_model

app = FastAPI(
    title="NeuralRetail API",
    description="AI Sales Intelligence Backend API",
    version="1.0",
)


# =========================================================
# HEALTH CHECK
# =========================================================
@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "NeuralRetail API is running"}


# =========================================================
# CHURN PREDICTION ENDPOINT
# =========================================================
@app.post("/predict/churn", response_model=ChurnResponse)
def predict_churn(data: ChurnRequest):

    # =====================================================
    # FEATURE ENGINEERING
    # =====================================================

    avg_monetary = data.Monetary / max(data.Frequency, 1)

    customer_value_score = (
        (data.Frequency * data.Monetary)
        / max(data.Recency, 1)
    )

    # =====================================================
    # INPUT DATAFRAME
    # =====================================================

    input_df = pd.DataFrame([{
        "Recency": data.Recency,
        "Frequency": data.Frequency,
        "Monetary": data.Monetary,
        "AvgMonetaryPerPurchase": avg_monetary,
        "CustomerValueScore": customer_value_score
    }])

    # DEBUG
    print(input_df.columns)

    # =====================================================
    # PREDICTION
    # =====================================================

    prediction = churn_model.predict(input_df)[0]

    probability = churn_model.predict_proba(input_df)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": round(float(probability), 4)
    }