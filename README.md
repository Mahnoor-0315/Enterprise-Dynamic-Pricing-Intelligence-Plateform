# Enterprise-Dynamic-Pricing-Intelligence-Plateform
A machine-learning prototype for dynamic pricing that predicts demand and recommends smarter prices using market, inventory, promotion, and seasonality data.


# Enterprise Dynamic Pricing Intelligence Platform

This project implements a lightweight end-to-end dynamic pricing prototype for the EEF case study.

## What is included
- Synthetic data generation for e-commerce sales events
- Feature engineering for demand and pricing signals
- A regression model for demand forecasting
- An explainability export for feature importance
- A FastAPI service with recommendation and training endpoints
- A simple HTML dashboard for quick price simulation

## Project structure
- src/data_generation.py: synthetic dataset generation and loading
- src/feature_engineering.py: feature transformation utilities
- src/modeling.py: demand model training and evaluation
- src/pricing_pipeline.py: pricing recommendation logic
- src/api.py: FastAPI application
- notebooks/01_eda.ipynb: EDA notebook placeholder

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run the API
```bash
uvicorn src.api:app --reload
```

## Sample training
```bash
python -c "from src.modeling import train_demand_model; print(train_demand_model())"
```


This repository is intended as a demonstration prototype for data-driven pricing strategy. It is not a production-grade pricing system and should be extended with real business data, stronger validation, and deployment safeguards before use in a live environment.

