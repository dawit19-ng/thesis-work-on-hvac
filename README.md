# HVAC Chiller Energy Consumption Forecasting

A comprehensive time-series forecasting project for predicting **Chiller Energy Consumption (kWh)** in a building HVAC system using deep learning and traditional ML models.

## Project Overview

This repository implements and compares multiple models for forecasting chiller energy consumption from HVAC sensor data:

- Deep Learning Models:
  - LSTM
  - BiLSTM
  - GRU
  - Custom SSM/Mamba-inspired model (State Space Model hybrid)
- Ensemble (average of all deep learning predictions)
- Baselines:
  - Random Forest
  - XGBoost

The pipeline includes:

- Temporal feature engineering (lags, rolling statistics, hour/day features)
- Min-Max scaling
- Sequence creation for recurrent models
- Training with early stopping and learning rate scheduling
- Comprehensive evaluation (RMSE, MAE, R², MAPE, Accuracy ≈ 100 - MAPE)

## 📊 Dataset

This project uses a publicly available HVAC dataset from Kaggle:

- [Kaggle HVAC Dataset](https://www.kaggle.com/dataset-link)  
- Download the dataset and save it in the root directory as `hvac_dataset.csv`.

The dataset should contain at least the following columns:

- `Local Time (Timezone : GMT+8h)` → timestamp
- `Chiller Energy Consumption (kWh)` → target
- Supporting features:
  - `Cooling Water Temperature (C)`
  - `Humidity (%)`
  - `Building Load (RT)`
  - `Chilled Water Rate (L/sec)`
  - `Outside Temperature (F)`
  - `Dew Point (F)`
  - `Wind Speed (mph)`
  - `Pressure (in)`

## ⚙️ Requirements

The project requires the following Python packages:

1. pandas  
2. numpy  
3. torch  
4. scikit-learn  
5. xgboost  
6. matplotlib  
7. seaborn  
8. scipy  

You can install them using:

```bash
pip install -r requirements.txt
