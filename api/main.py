# =========================================================
# FASTAPI IMPORTS
# =========================================================

from fastapi import FastAPI
from pydantic import BaseModel

import joblib
import numpy as np

# =========================================================
# CREATE APP
# =========================================================

app = FastAPI(
    title="NeuralRetail AI API",
    version="1.0"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load(
    r"D:\NuralRetail\output\models\churn_model.pkl"
)

# =========================================================
# INPUT SCHEMA
# =========================================================

class CustomerData(BaseModel):

    Recency: float
    Frequency: float
    Monetary: float
    AvgMonetaryPerPurchase: float

# =========================================================
# ROOT ROUTE
# =========================================================

@app.get("/")

def home():

    return {
        "message": "NeuralRetail AI API Running"
    }

# =========================================================
# CHURN PREDICTION
# =========================================================

@app.post("/predict/churn")

def predict_churn(data: CustomerData):

    features = np.array([[
        data.Recency,
        data.Frequency,
        data.Monetary,
        data.AvgMonetaryPerPurchase
    ]])

    probability = model.predict_proba(
        features
    )[0][1]

    prediction = int(probability > 0.5)

    return {

        "churn_probability": float(probability),

        "prediction": prediction
    }