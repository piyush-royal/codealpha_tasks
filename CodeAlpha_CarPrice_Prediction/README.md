# Car Price Prediction using Machine Learning

## Project Overview

This project predicts the selling price of used cars using Machine Learning techniques. The model analyzes various factors such as vehicle age, present price, fuel type, transmission type, ownership history, and kilometers driven to estimate the resale value of a car.

The objective of this project is to demonstrate the practical application of regression algorithms in solving real-world price prediction problems.

---

## Dataset Information

The dataset contains information about different cars and their selling prices.

### Features Used

- Year
- Present_Price
- Driven_kms
- Fuel_Type
- Selling_type
- Transmission
- Owner

### Target Variable

- Selling_Price

### Dataset Summary

- Total Records: 301
- Features: 7
- Missing Values: 0

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Label Encoding
5. Train-Test Split
6. Model Training
7. Prediction
8. Model Evaluation
9. Feature Importance Analysis

---

## Model Used

### Random Forest Regressor

Random Forest Regressor was used to predict car selling prices based on the available features.

---

## Model Performance

| Metric | Value |
|----------|----------|
| MAE | 0.614 |
| RMSE | 0.916 |
| R² Score | 0.964 |

The model achieved an accuracy score (R²) of approximately **96.4%**, indicating strong predictive performance.

---

## Feature Importance

The model identified the following factors as the most influential:

1. Present Price
2. Year
3. Driven Kilometers
4. Transmission Type
5. Fuel Type

---

## Key Insights

- Present Price is the strongest predictor of a car's selling price.
- Newer vehicles generally have higher resale values.
- Cars with lower mileage tend to have better market prices.
- Fuel type and transmission also influence resale value.

---

## Project Structure

```text
CodeAlpha_CarPrice_Prediction/
│
├── car-data.csv
├── car_price_prediction.py
├── feature_importance.png
├── requirements.txt
└── README.md
```

## Future Improvements

- Hyperparameter tuning
- Deployment using Streamlit
- Comparison with other regression models
- Real-time car price prediction interface

---

## Author

Piyush Royal

Data Science & Machine Learning Enthusiast
