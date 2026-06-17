# 🧠 NeuralRetail AI Sales Intelligence Platform

An enterprise-style AI-powered retail analytics platform built using **Streamlit, FastAPI, Machine Learning, and Cloud Deployment** for intelligent business forecasting, customer churn prediction, monitoring, and decision support.

---

# 🚀 Live Demo

## 🌐 Streamlit Application

https://neuralretail-ai-sales-intelligence.streamlit.app

## ⚡ FastAPI Backend

https://neuralretail-ai-sales-intelligence.onrender.com/docs

---

# 📌 Project Overview

NeuralRetail AI is a production-style retail intelligence system designed to help businesses analyze customer behavior, forecast sales trends, identify churn risks, and monitor AI model performance in real time.

This project combines:

* Business Intelligence
* Machine Learning
* Cloud APIs
* Authentication Systems
* MLOps Concepts
* Enterprise Dashboard Design

The system simulates how modern retail analytics platforms operate in real enterprise environments.

---

# 🏗️ System Architecture

```text
User
   ↓
Streamlit Frontend Dashboard
   ↓
Authentication & RBAC Layer
   ↓
FastAPI Backend APIs
   ↓
Machine Learning Models
   ├── XGBoost Churn Prediction
   ├── Prophet Forecasting
   └── Analytics Engine
   ↓
Monitoring & Reporting Layer
   ↓
Cloud Deployment (Render + Streamlit Cloud)
```

---

# ✨ Key Features

## 📊 Business Intelligence Dashboard

* Executive KPI Monitoring
* Revenue & Sales Analysis
* Customer Segmentation
* Risk-Based Filtering
* Interactive Visualizations

---

## 🤖 AI & Machine Learning

### 🔥 Churn Prediction

* Real-time churn prediction using XGBoost
* Live API-based inference
* Probability-based risk scoring
* Feature engineering during inference

### 📈 Sales Forecasting

* Prophet-based future sales forecasting
* Trend analysis
* Seasonal pattern prediction

---

## ⚡ FastAPI Backend

* Production-style ML API serving
* RESTful prediction endpoints
* Swagger API documentation
* Modular backend architecture

---

## 🔐 Authentication & RBAC

* Login system
* Session management
* Protected routes
* Role-Based Access Control (RBAC)
* Admin & Viewer roles

---

## 📄 Export & Reporting

* Excel report generation
* Professional PDF reports
* Executive analytics summaries

---

## 📡 Monitoring Dashboard

* API health tracking
* Model monitoring
* Simulated AI drift monitoring
* Prediction statistics
* System health metrics

---

# 🧠 Machine Learning Models

| Model                   | Purpose                          |
| ----------------------- | -------------------------------- |
| XGBoost                 | Customer Churn Prediction        |
| Prophet                 | Sales Forecasting                |
| Pandas Analytics Engine | Business Insights & KPI Analysis |

---

# 🛠️ Tech Stack

## Frontend

* Streamlit
* Plotly
* HTML/CSS

## Backend

* FastAPI
* Uvicorn

## Machine Learning

* XGBoost
* Prophet
* Scikit-learn
* Pandas
* NumPy

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sagarmehra69/neuralretail-ai-sales-intelligence.git
cd neuralretail-ai-sales-intelligence
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

## 🚀 Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000/docs
```

---

## 🌐 Run Streamlit Frontend

```bash
streamlit run app.py
```
---

# 🔐 Demo Credentials

## 👑 Admin

```text
Username: admin
Password: admin123
```

## 👤 Viewer

```text
Username: viewer
Password: viewer123
```
---

# 🎯 Business Use Cases

* Customer retention analytics
* Retail sales forecasting
* Churn risk management
* Executive reporting
* AI-powered business intelligence

---

# 📸 Project Highlights

✅ Production-style ML architecture
✅ Cloud deployment
✅ FastAPI integration
✅ Real-time inference
✅ Authentication & RBAC
✅ Monitoring dashboard
✅ Export system
✅ Enterprise UI/UX

# ⭐ Final Note

NeuralRetail AI is designed to simulate a modern enterprise retail intelligence ecosystem by combining machine learning, cloud deployment, monitoring, authentication, and real-time analytics into a single integrated platform.

This project demonstrates not only machine learning capability, but also practical AI system architecture and deployment engineering.
