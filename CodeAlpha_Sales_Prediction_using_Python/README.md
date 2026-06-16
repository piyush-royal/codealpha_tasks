# Sales Prediction using Python

## Project Overview

This project predicts product sales based on advertising expenditures across different marketing channels. Using Machine Learning techniques, the model analyzes the impact of TV, Radio, and Newspaper advertising budgets on overall sales performance.

The goal of this project is to help businesses make data-driven marketing decisions and optimize advertising investments for maximum sales growth.

---

## Dataset Information

The dataset contains advertising spending data and corresponding sales figures.

### Features Used

- TV Advertising Budget
- Radio Advertising Budget
- Newspaper Advertising Budget

### Target Variable

- Sales

### Dataset Summary

- Total Records: 200
- Features: 3
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
3. Feature Selection
4. Train-Test Split
5. Model Training
6. Sales Prediction
7. Model Evaluation
8. Advertising Impact Analysis
9. Data Visualization

---

## Model Used

### Linear Regression

Linear Regression was used to establish the relationship between advertising expenditure and sales performance.

---

## Model Performance

| Metric | Value |
|----------|----------|
| MAE | 1.46 |
| R² Score | 0.899 |

The model achieved an **R² Score of approximately 89.9%**, indicating strong predictive capability.

---

## Advertising Impact Analysis

| Advertising Channel | Impact |
|---------------------|---------|
| Radio | Highest |
| TV | Moderate |
| Newspaper | Lowest |

### Coefficients

| Feature | Coefficient |
|----------|------------|
| TV | 0.0447 |
| Radio | 0.1892 |
| Newspaper | 0.0028 |

---

## Key Insights

- Radio advertising has the strongest influence on sales.
- TV advertising positively impacts product sales.
- Newspaper advertising contributes very little compared to other channels.
- Businesses can improve marketing ROI by focusing more on Radio and TV advertising.

---

## Visualization

The project includes a graphical analysis showing the impact of advertising platforms on sales.

**Output File:**

- advertising_impact.png

---

## Project Structure

```text
CodeAlpha_Sales_Prediction/
│
├── advertising.csv
├── sales_prediction.py
├── advertising_impact.png
├── requirements.txt
└── README.md
```

---

## Future Improvements

- Hyperparameter tuning
- Advanced regression models
- Time-series sales forecasting
- Interactive dashboard using Streamlit
- Real-time sales prediction system

---

## Author

Piyush Royal

Data Science & Machine Learning Enthusiast
