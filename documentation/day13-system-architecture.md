# Day 13 System Architecture and Workflow Documentation

## Objective

To document the architecture, workflow, and deployment process of the Insurance AI Risk Analysis and Policy Recommendation System.

---

# Project Overview

The Insurance AI Risk Analysis and Policy Recommendation System is an AI-powered decision support platform designed to assist insurance providers in assessing customer risk levels and recommending appropriate insurance plans.

The system combines machine learning, risk classification, business rules, and an interactive dashboard to automate insurance decision-making.

---

# System Architecture

## Architecture Diagram

![System Architecture](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/diagrams/system_architecture.png)

---

## Architecture Components

### 1. Customer Data Input

The system accepts customer information including:

* Age
* Gender
* BMI
* Number of Children
* Smoking Status
* Region

This information serves as input for the machine learning model.

---

### 2. Streamlit Dashboard

The dashboard acts as the user interface layer.

Functions:

* Collect customer information
* Display prediction results
* Display policy recommendations
* Provide real-time interaction

---

### 3. Risk Prediction Model

Model Used:

**Random Forest Classifier**

Responsibilities:

* Analyze customer features
* Predict insurance risk category
* Generate classification output

Performance:

* Accuracy: 90.30%

---

### 4. Risk Classification Layer

Customers are classified into:

#### Low Risk

* Lower expected claims
* Lower overall risk exposure

#### Medium Risk

* Moderate risk indicators
* Balanced customer profile

#### High Risk

* Elevated risk factors
* Higher expected insurance costs

---

### 5. Policy Recommendation Engine

The recommendation engine maps risk levels to insurance plans.

| Risk Level  | Recommended Policy      |
| ----------- | ----------------------- |
| Low Risk    | Basic Insurance Plan    |
| Medium Risk | Standard Insurance Plan |
| High Risk   | Premium Insurance Plan  |

---

### 6. Insurance Policy Output

The system provides:

* Customer Risk Level
* Recommended Insurance Policy

This serves as the final decision-support output.

---

# Project Workflow

## Workflow Diagram

![Project Workflow](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/diagrams/project_workflow.png)

---

## Workflow Description

### Dataset Collection

* Insurance dataset acquisition
* Feature understanding
* Business problem analysis

### Exploratory Data Analysis (EDA)

* Statistical analysis
* Data visualization
* Pattern identification
* Feature understanding

### Data Preprocessing

* Data cleaning
* Feature encoding
* Data preparation
* Model-ready dataset creation

### Model Training

Models evaluated:

* Linear Regression
* Decision Tree
* Random Forest

### Hyperparameter Optimization

Performed:

* Parameter tuning
* Model evaluation
* Performance improvement

### Risk Classification

Customers classified into:

* Low Risk
* Medium Risk
* High Risk

### Policy Recommendation Engine

Risk categories are mapped to suitable insurance plans through business rules.

### Streamlit Dashboard

Final deployment layer providing real-time customer analysis and policy recommendation.

---

# Technology Stack

## Programming Language

* Python

## Data Analysis

* Pandas

## Machine Learning

* Scikit-Learn

## Models

* Linear Regression
* Decision Tree
* Random Forest
* Optimized Random Forest

## Model Persistence

* Joblib

## Dashboard Framework

* Streamlit

---

# Model Performance Summary

## Insurance Charge Prediction

### Optimized Random Forest Regressor

| Metric   | Value         |
| -------- | ------------- |
| MAE      | 2441.70       |
| MSE      | 19,519,656.07 |
| R² Score | 89.38%        |

---

## Risk Classification

### Random Forest Classifier

| Metric            | Value  |
| ----------------- | ------ |
| Accuracy          | 90.30% |
| Macro F1 Score    | 0.90   |
| Weighted F1 Score | 0.90   |

---

# Deployment Process

## Step 1: Clone Repository

```bash
git clone https://github.com/Piyush93199/insurance-ai-risk-analysis-system.git
cd insurance-ai-risk-analysis-system
```

## Step 2: Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install pandas scikit-learn streamlit joblib
```

## Step 4: Launch Application

```bash
streamlit run app/app.py
```

## Step 5: Access Dashboard

Open:

```text
http://localhost:8501
```

---

# Project Deliverables

Completed Components:

* Insurance Domain Research
* Dataset Collection
* Exploratory Data Analysis
* Data Preprocessing
* Machine Learning Models
* Hyperparameter Optimization
* Risk Classification System
* Policy Recommendation Engine
* Streamlit Dashboard
* System Architecture Documentation
* Workflow Documentation
* Deployment Guide

---

# Conclusion

The Insurance AI Risk Analysis and Policy Recommendation System successfully integrates machine learning, risk assessment, and business decision logic into a unified platform. The system can analyze customer information, classify insurance risk levels, recommend suitable insurance policies, and provide real-time interaction through a Streamlit dashboard. The project demonstrates a complete end-to-end machine learning workflow from data collection to deployment and serves as a practical AI-powered insurance decision-support solution.
