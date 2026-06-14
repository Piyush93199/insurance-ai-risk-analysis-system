# Day 12 Progress Report

## Date

Day 12

## Objective

To develop a user-facing web application for the Insurance AI Risk Analysis and Policy Recommendation System and integrate all previously developed machine learning components into a single interactive platform.

---

## Activities Performed

* Designed and developed a Streamlit-based web application.
* Created an interactive customer information input form.
* Integrated the Risk Prediction Model with the dashboard.
* Connected the Policy Recommendation Engine to prediction outputs.
* Implemented real-time customer risk analysis.
* Tested the application using multiple customer profiles.
* Verified risk prediction and policy recommendation consistency.
* Generated dashboard screenshots and documentation.

---

## Deliverables Completed

* Streamlit web application.
* Interactive customer input interface.
* Integrated Risk Prediction Model.
* Integrated Policy Recommendation Engine.
* Real-time prediction workflow.
* Dashboard documentation.
* User demonstration screenshots.

---

## Dashboard Features

### Customer Data Input

The application accepts:

* Age
* Gender
* BMI
* Number of Children
* Smoking Status
* Region

### Risk Prediction

The Random Forest Classifier predicts customer risk categories:

* Low Risk
* Medium Risk
* High Risk

### Policy Recommendation

Based on predicted risk levels, the system recommends:

| Risk Level  | Recommended Policy      |
| ----------- | ----------------------- |
| Low Risk    | Basic Insurance Plan    |
| Medium Risk | Standard Insurance Plan |
| High Risk   | Premium Insurance Plan  |

### Real-Time Analysis

The dashboard provides instant risk assessment and policy recommendations.

---

## System Testing

### Test Case 1

| Feature | Value |
| ------- | ----- |
| Age     | 25    |
| BMI     | 22    |
| Smoker  | No    |

**Prediction**

* Risk Level: Low Risk
* Recommended Policy: Basic Insurance Plan

---

### Test Case 2

| Feature | Value |
| ------- | ----- |
| Age     | 45    |
| BMI     | 30    |
| Smoker  | Yes   |

**Prediction**

* Risk Level: High Risk
* Recommended Policy: Premium Insurance Plan

---

### Test Case 3

| Feature | Value |
| ------- | ----- |
| Age     | 60    |
| BMI     | 36    |
| Smoker  | Yes   |

**Prediction**

* Risk Level: High Risk
* Recommended Policy: Premium Insurance Plan

---

## Key Findings

### Risk Prediction Performance

Random Forest Classifier

* Accuracy: 90.30%
* Macro F1 Score: 0.90
* Weighted F1 Score: 0.90

### Insurance Charge Prediction Performance

Optimized Random Forest Regressor

* MAE: 2441.70
* MSE: 19,519,656.07
* R² Score: 89.38%

### Business Insights

* Smoking status remains the strongest risk indicator.
* Age significantly influences insurance risk.
* High-risk customers generally require enhanced coverage.
* Automated recommendations improve decision-making efficiency.

---

## Challenges Faced

### Streamlit Deployment Setup

* Configuring the Python virtual environment.
* Installing required packages correctly.

### Model Integration

* Connecting machine learning models with the dashboard interface.
* Handling model loading and prediction workflows.

### Label Encoding Consistency

* Ensuring correct mapping between encoded labels and risk categories.
* Correcting policy recommendation logic after identifying encoding mismatches.

---

## Resolution

* Successfully configured the virtual environment.
* Integrated trained models using Joblib.
* Fixed label encoding and recommendation mapping issues.
* Validated outputs using multiple customer test cases.

---

## Learning Outcomes

* Learned Streamlit application development.
* Gained experience integrating machine learning models into web applications.
* Improved understanding of deployment workflows.
* Learned practical implementation of AI-powered decision-support systems.
* Developed a complete end-to-end machine learning application.

---

## Project Status

### Completed Modules

* Insurance Domain Research
* Dataset Collection
* Exploratory Data Analysis
* Data Preprocessing
* Linear Regression Model
* Decision Tree Model
* Random Forest Model
* Hyperparameter Optimization
* Risk Classification Framework
* Risk Prediction Model
* Policy Recommendation Engine
* Streamlit Dashboard

### Overall Progress

Core project functionality is fully operational.

The system can:

1. Accept customer information.
2. Predict customer risk level.
3. Recommend an insurance policy.
4. Display results through a web interface.

---

## Plan for Day 13

* Improve dashboard UI and user experience.
* Create system architecture diagram.
* Design project workflow diagram.
* Prepare project presentation slides.
* Create deployment documentation.
* Prepare final internship project demonstration.

---

## Status

Day 12 objectives completed successfully. The Insurance AI Risk Analysis and Policy Recommendation System has been transformed into a fully functional web application. The project now includes machine learning-based risk prediction, automated policy recommendation, and an interactive dashboard, making it suitable for demonstrations, presentations, and real-world insurance decision-support scenarios.
