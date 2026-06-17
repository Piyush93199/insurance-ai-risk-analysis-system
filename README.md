# Insurance AI Risk Analysis and Policy Recommendation System

## Overview

The Insurance AI Risk Analysis and Policy Recommendation System is an end-to-end machine learning application designed to assess customer insurance risk levels and recommend suitable insurance plans.

The system combines data analysis, predictive modeling, risk classification, recommendation logic, and a Streamlit-based web dashboard to provide an AI-powered insurance decision support solution.

This project was developed as part of an AI/ML internship focused on applying machine learning techniques to real-world business problems in the insurance domain.

---

## Project Objectives

* Analyze insurance customer data.
* Identify factors affecting insurance costs and risk.
* Predict customer risk levels using machine learning.
* Classify customers into risk categories.
* Recommend suitable insurance policies.
* Provide real-time risk assessment through a web application.

---

## System Architecture

![System Architecture](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/diagrams/system_architecture.png)

---

## Project Workflow

![Project Workflow](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/diagrams/project_workflow.png)

---

## Dataset Overview

| Attribute    | Value                      |
| ------------ | -------------------------- |
| Records      | 1338                       |
| Features     | 7                          |
| Dataset Type | Insurance Customer Dataset |

### Features

* Age
* Gender
* BMI
* Children
* Smoker
* Region
* Charges

---

## Exploratory Data Analysis Findings

### Key Insights

* Smoking status is the strongest factor affecting insurance charges.
* Customer age significantly impacts insurance costs.
* Higher BMI values contribute to increased risk.
* Insurance charges show a positively skewed distribution.
* Gender has relatively limited influence on insurance costs.

---

## Machine Learning Models

### Insurance Charge Prediction

| Model                   | R² Score |
| ----------------------- | -------- |
| Linear Regression       | 80.68%   |
| Decision Tree           | 89.24%   |
| Random Forest           | 88.34%   |
| Optimized Random Forest | 89.38%   |

### Best Model

**Optimized Random Forest Regressor**

Performance Metrics:

* MAE: 2441.70
* MSE: 19,519,656.07
* R² Score: 89.38%

---

## Risk Classification System

The system classifies customers into three categories:

### Low Risk

* Lower expected claims
* Lower insurance costs
* Healthier customer profile

### Medium Risk

* Moderate risk exposure
* Balanced customer profile

### High Risk

* Higher expected claims
* Increased insurance risk
* Greater financial exposure

### Classification Performance

| Metric            | Value  |
| ----------------- | ------ |
| Accuracy          | 90.30% |
| Macro F1 Score    | 0.90   |
| Weighted F1 Score | 0.90   |

---

## Policy Recommendation Engine

| Risk Level  | Recommended Policy      |
| ----------- | ----------------------- |
| Low Risk    | Basic Insurance Plan    |
| Medium Risk | Standard Insurance Plan |
| High Risk   | Premium Insurance Plan  |

The recommendation engine automatically maps predicted customer risk levels to suitable insurance plans.

---

## Streamlit Dashboard

### Features

* Customer Data Input
* Risk Prediction
* Risk Classification
* Policy Recommendation
* Real-Time Analysis

### Dashboard Home

![Dashboard Home](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/dashboard_home.png)

### Customer Input Form

![Customer Input Form](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/customer_input.png)

### Prediction Result

![Prediction Result](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/prediction_result.png)

---

## Technology Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn

### Visualization

* Matplotlib

### Dashboard

* Streamlit

### Model Persistence

* Joblib

### Development Tools

* Git
* GitHub
* VS Code
* Jupyter Notebook

---

## Project Structure

```text
insurance-ai-project/
├── app/
├── dataset/
├── models/
├── notebooks/
├── documentation/
├── reports/
├── diagrams/
├── screenshots/
├── presentations/
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Piyush93199/insurance-ai-risk-analysis-system.git
cd insurance-ai-risk-analysis-system
```

### Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install pandas numpy scikit-learn streamlit joblib matplotlib
```

### Run Application

```bash
streamlit run app/app.py
```

### Access Dashboard

Open:

```text
http://localhost:8501
```

---

## Project Deliverables

* Insurance Risk Prediction Model
* Risk Classification System
* Policy Recommendation Engine
* Streamlit Dashboard
* System Architecture Documentation
* Workflow Documentation
* Deployment Guide
* Final Validation Report

---

## Results Summary

### Insurance Charge Prediction

* Best Model: Optimized Random Forest Regressor
* R² Score: 89.38%
* MAE: 2441.70

### Risk Classification

* Accuracy: 90.30%
* Macro F1 Score: 0.90
* Weighted F1 Score: 0.90

### Business Outcome

The system successfully predicts customer risk levels and generates personalized insurance policy recommendations through an interactive dashboard, providing a practical AI-powered insurance decision support solution.

---

## Author

**Piyush Chaubey**

Bachelor of Computer Applications (Artificial Intelligence & Machine Learning)

University of Petroleum and Energy Studies (UPES)

GitHub: https://github.com/Piyush93199

---

## License

This project is licensed under the MIT License.
