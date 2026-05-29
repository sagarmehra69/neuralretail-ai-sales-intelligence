# 🧠 NeuralRetail AI

Enterprise AI-powered retail intelligence platform built using Machine Learning, Forecasting Models, Customer Analytics, Inventory Intelligence, and Interactive Dashboards.

NeuralRetail AI transforms raw retail transaction data into actionable business intelligence using AI-driven forecasting, churn prediction, inventory optimization, and MLOps monitoring.

---

## 🌐 Live Dashboard
 [![Live App](https://img.shields.io/badge/Live-Dashboard-success?style=for-the-badge&logo=streamlit)](https://neuralretail-ai-sales-intelligence.streamlit.app/)


# 🚀 Key Features

## 📈 Demand Forecasting
- AI-powered sales forecasting using:
  - Prophet
  - XGBoost
- Time-series feature engineering
- Forecast performance comparison
- Actual vs Predicted visualization
- Forecast KPI monitoring

---

## 👥 Customer Intelligence
- Customer churn prediction
- Customer segmentation analytics
- High-risk customer detection
- Churn probability analysis
- Retention intelligence dashboard

---

## 📦 Inventory Intelligence
- Inventory risk analysis
- Reorder point monitoring
- EOQ (Economic Order Quantity) analysis
- Stock optimization insights
- Inventory alert system

---

## ⚙️ MLOps Monitoring
- Model performance tracking
- Forecast model comparison
- Drift monitoring simulation
- AI pipeline health monitoring
- Champion vs challenger model evaluation

---

# 🏗️ System Architecture

<img width="1376" height="768" alt="NuralRetail" src="https://github.com/user-attachments/assets/222fa859-391d-415b-8eb0-5113de87b9dc" />


---

# 🏗️ NeuralRetail AI — System Architecture

```text
                                      ┌──────────────────────────┐
                                      │   Retail Transaction     │
                                      │        Dataset           │
                                      └────────────┬─────────────┘
                                                   │
                                                   ▼
                         ┌─────────────────────────────────────────┐
                         │      Data Cleaning & Preprocessing      │
                         │-----------------------------------------│
                         │ • Missing Value Handling                │
                         │ • Outlier Detection                     │
                         │ • Datetime Processing                   │
                         │ • Feature Standardization               │
                         └────────────┬────────────────────────────┘
                                      │
                                      ▼
                     ┌──────────────────────────────────────────────┐
                     │           Feature Engineering                │
                     │----------------------------------------------│
                     │ • Lag Features                               │
                     │ • Rolling Mean / Std                         │
                     │ • RFM Analysis                               │
                     │ • EOQ Calculations                           │
                     │ • Inventory Risk Features                    │
                     │ • Time-Series Aggregation                    │
                     └────────────┬─────────────────────────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         │                        │                        │
         ▼                        ▼                        ▼

┌─────────────────┐    ┌────────────────────┐    ┌────────────────────┐
│ Demand Forecast │    │ Customer Analytics │    │ Inventory Analytics│
│-----------------│    │--------------------│    │--------------------│
│ Prophet         │    │ Churn Prediction   │    │ EOQ Analysis       │
│ XGBoost         │    │ RFM Segmentation   │    │ Reorder Monitoring │
│ Forecast KPIs   │    │ Risk Scoring       │    │ Risk Scoring       │
└────────┬────────┘    └─────────┬──────────┘    └─────────┬──────────┘
         │                       │                         │
         └───────────────────────┼─────────────────────────┘
                                 │
                                 ▼

               ┌──────────────────────────────────┐
               │      Model Evaluation Layer      │
               │----------------------------------│
               │ • MAPE                           │
               │ • RMSE                           │
               │ • MAE                            │
               │ • F1 Score                       │
               │ • Drift Monitoring               │
               │ • Champion Model Selection       │
               └──────────────┬───────────────────┘
                              │
                              ▼

               ┌──────────────────────────────────┐
               │       Data Export Pipeline       │
               │----------------------------------│
               │ • forecast_results.csv           │
               │ • churn_predictions.csv          │
               │ • inventory_risk.csv             │
               │ • model_metrics.csv              │
               └──────────────┬───────────────────┘
                              │
                              ▼

               ┌──────────────────────────────────┐
               │       Streamlit Dashboard        │
               │----------------------------------│
               │ • Executive Overview             │
               │ • Forecasting Intelligence       │
               │ • Customer Intelligence          │
               │ • Inventory Intelligence         │
               │ • MLOps Monitoring               │
               └──────────────┬───────────────────┘
                              │
                              ▼

               ┌──────────────────────────────────┐
               │        Business Intelligence      │
               │----------------------------------│
               │ • Sales Insights                 │
               │ • Churn Detection                │
               │ • Inventory Optimization         │
               │ • AI Monitoring                  │
               │ • Operational Analytics          │
               └──────────────────────────────────┘

```
```text
═══════════════════════════════════════════════════════════════════════

                        ⚙️ MLOps Monitoring Layer

═══════════════════════════════════════════════════════════════════════

┌──────────────────────┐
│ MLflow Tracking      │
│----------------------│
│ • Experiment Logging │
│ • Model Metrics      │
│ • Artifact Tracking  │
└──────────┬───────────┘
           │
           ▼

┌──────────────────────┐
│ Drift Monitoring     │
│----------------------│
│ • Data Drift         │
│ • KPI Monitoring     │
│ • Performance Drift  │
└──────────┬───────────┘
           │
           ▼

┌──────────────────────┐
│ Deployment Ready     │
│----------------------│
│ • Streamlit UI       │
│ • Multi-page App     │
│ • Modular Loaders    │
│ • Real-time KPIs     │
└──────────────────────┘
```
---

# 📊 Dashboard Modules

## 🧠 Executive Overview
Central command center showing:
- Global KPIs
- Sales trends
- Churn overview
- Inventory risk overview
- AI system status

---

## 📈 Demand Forecasting Dashboard
Includes:
- Actual vs Predicted Sales
- Forecast KPIs
- Trend visualization
- Forecast monitoring

---

## 👥 Customer Intelligence Dashboard
Includes:
- Churn probability distribution
- Customer segmentation
- High-risk customer detection
- Customer analytics

---

## 📦 Inventory Intelligence Dashboard
Includes:
- Inventory risk distribution
- EOQ analysis
- Stock vs reorder point analytics
- Inventory alerts

---

## ⚙️ Model Monitoring Dashboard
Includes:
- Model comparison metrics
- MAPE monitoring
- Drift monitoring
- AI lifecycle tracking
- System health monitoring

---

# 📉 Model Performance

| Model | Performance |
|---|---|
| XGBoost Forecasting | MAPE: 21.45% |
| Prophet Forecasting | MAPE: 30.75% |
| Churn Prediction | F1 Score: 0.999 |
| Inventory Intelligence | Risk Scoring System |

---

# ⚙️ Tech Stack

## Programming & Analytics
- Python
- Pandas
- NumPy

## Machine Learning
- Scikit-learn
- XGBoost
- Prophet

## Visualization
- Plotly
- Matplotlib
- Streamlit

## MLOps & Optimization
- MLflow
- Optuna

## Development Environment
- Jupyter Notebook
- VS Code

---

# 📂 Project Structure

```text
NeuralRetail/
│
├── app/
│   └── dashboard/
│       ├── app.py
│       ├── pages/
│       ├── utils/
│       ├── data/
│       └── assets/
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Demand_Forecasting.ipynb
│   ├── 03_Customer_Intelligence.ipynb
│   ├── 04_Inventory_Intelligence.ipynb
│   └── 05_MLOps_Monitoring.ipynb
│
├── data/
├── models/
├── reports/
├── src/
└── README.md

```

# 🧪 Machine Learning Pipeline

Forecasting Pipeline
Time-series preprocessing
Lag feature generation
Rolling statistics
Forecast model training
Model evaluation
Customer Intelligence Pipeline
RFM feature engineering
Churn classification
Customer segmentation
Risk scoring
Inventory Intelligence Pipeline
EOQ calculation  
Reorder point analysis
Inventory risk scoring
Inventory optimization

---

# 📡 MLOps Capabilities
Model monitoring
Performance tracking
Drift monitoring
Pipeline health monitoring
Metrics visualization
Deployment-ready architecture
---
# 🎯 Business Impact

NeuralRetail AI helps retailers:

Reduce inventory waste
Improve sales forecasting
Detect customer churn early
Optimize inventory operations
Improve operational visibility
Enable AI-driven retail decisions
---

# 🚀 Running the Dashboard

Clone Repository

git clone https://github.com/sagarmehra69/neuralretail-ai-sales-intelligence.git

Install Dependencies

pip install -r requirements.txt
Run Streamlit Dashboard
cd app/dashboard

streamlit run app.py
---
# 🔮 Future Improvements

Real-time streaming pipelines
Kafka integration
LSTM forecasting models
Cloud deployment
Dockerization
CI/CD pipelines
Automated retraining
Real-time drift detection
API integration
Role-based dashboard access

---

# 📌 Project Status

Forecasting Intelligence ✅ Completed
Customer Intelligence ✅ Completed
Inventory Intelligence ✅ Completed
Dashboard Integration ✅ Completed
MLOps Monitoring ✅ Completed
Enterprise Dashboard UI ✅ Completed

---

# 👨‍💻 Author
Sagar Mehra

---
AI & Data Science Enthusiast

Focused on:

Machine Learning
Forecasting Systems
MLOps
Enterprise AI Platforms

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub and support the project.

---

