import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model paths
CHURN_MODEL_PATH = os.path.join(
    BASE_DIR,
    "output",
    "models",
    "xgboost_churn_model.pkl"
)

FEATURE_PATH = os.path.join(
    BASE_DIR,
    "output",
    "models",
    "churn_features.pkl"
)

# Load models once during startup
churn_model = joblib.load(CHURN_MODEL_PATH)
churn_features = joblib.load(FEATURE_PATH)