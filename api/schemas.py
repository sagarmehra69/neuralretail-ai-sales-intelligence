from pydantic import BaseModel


class ChurnRequest(BaseModel):
    Recency: float
    Frequency: float
    Monetary: float


class ChurnResponse(BaseModel):
    churn_prediction: int
    churn_probability: float