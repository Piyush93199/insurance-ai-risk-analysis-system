# Day 12 Streamlit Dashboard

## Objective

Develop a user-friendly web application for the Insurance AI Risk Analysis and Policy Recommendation System that enables users to enter customer information, predict risk levels, and receive personalized insurance policy recommendations.

---

## Dashboard Overview

The Streamlit dashboard serves as the front-end interface for the machine learning system developed during previous phases of the project.

The application integrates:

- Risk Prediction Model
- Policy Recommendation Engine
- Customer Data Input Interface
- Real-Time Prediction System

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Programming Language | Python |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas |
| Model Storage | Joblib |

---

## System Workflow

Customer Information Input

↓

Risk Prediction Model

↓

Risk Classification

↓

Policy Recommendation Engine

↓

Insurance Plan Suggestion

---

## Features Implemented

### Customer Information Input

The dashboard allows users to enter:

- Age
- Gender
- BMI
- Number of Children
- Smoking Status
- Region

### Risk Prediction

The trained Random Forest Classifier predicts the customer's insurance risk category.

### Policy Recommendation

Based on the predicted risk category, the system recommends an appropriate insurance policy.

### Interactive Dashboard

The application provides instant feedback and displays prediction results in real time.

---

# Dashboard Screenshots

## Dashboard Home Page

![Dashboard Home](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/dashboard_home.png)

**Description**

The home page provides access to the Insurance AI Risk Analysis System and allows users to enter customer details.

---

## Customer Input Form

![Customer Input](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/customer_input.png)

**Description**

Users enter customer demographic and lifestyle information required for risk prediction.

---

## Prediction Result

![Prediction Result](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/prediction_result.png)

**Description**

The system predicts the customer risk level and generates an appropriate policy recommendation.

---

## Sample Prediction

### Customer Profile

| Feature | Value |
|----------|----------|
| Age | 60 |
| Gender | Male |
| BMI | 36 |
| Children | 3 |
| Smoker | Yes |
| Region | Southeast |

### System Output

| Result | Value |
|----------|----------|
| Risk Level | High Risk |
| Recommended Policy | Premium Insurance Plan |

---

## Recommendation Logic

| Risk Level | Recommended Policy |
|------------|-------------------|
| Low Risk | Basic Insurance Plan |
| Medium Risk | Standard Insurance Plan |
| High Risk | Premium Insurance Plan |

---

## Business Benefits

### Automated Risk Assessment

- Reduces manual risk evaluation effort.
- Provides consistent decision-making.

### Personalized Recommendations

- Suggests policies based on customer risk profiles.
- Improves customer experience.

### Underwriting Support

- Assists insurance professionals during policy evaluation.

### Decision Support

- Converts machine learning predictions into actionable business insights.

---

## Project Progress Summary

Completed Components:

- Insurance Domain Research
- Dataset Collection and Analysis
- Exploratory Data Analysis
- Data Preprocessing
- Linear Regression Model
- Decision Tree Model
- Random Forest Model
- Hyperparameter Optimization
- Risk Classification Framework
- Risk Prediction Model
- Policy Recommendation Engine
- Streamlit Dashboard

---

## Current Best Models

### Insurance Charge Prediction

Optimized Random Forest Regressor

Performance:

- MAE: 2441.70
- MSE: 19,519,656.07
- R² Score: 89.38%

### Risk Classification

Random Forest Classifier

Performance:

- Accuracy: 90.30%
- Macro F1 Score: 0.90
- Weighted F1 Score: 0.90

---

## Conclusion

A fully functional Streamlit dashboard was successfully developed and integrated with the Insurance AI Risk Analysis and Policy Recommendation System. The dashboard enables users to enter customer information, predict insurance risk levels, and receive personalized policy recommendations in real time. This implementation transforms the machine learning project into a practical and interactive insurance decision-support application suitable for real-world demonstrations and internship project presentations.