# Day 10 Risk Prediction Model

## Objective

Develop a machine learning model capable of automatically predicting customer risk categories and supporting the insurance policy recommendation system.

---

## Background

The risk classification framework developed on Day 9 successfully categorized customers into Low Risk, Medium Risk, and High Risk groups. The next step was to automate this process using machine learning.

A Random Forest Classifier was selected due to its strong performance, ability to handle complex relationships, and robustness against overfitting.

---

## Model Used

### Random Forest Classifier

The Random Forest Classifier uses an ensemble of decision trees to predict customer risk categories based on demographic, lifestyle, and insurance-related attributes.

---

## Target Classes

| Encoded Value | Risk Category |
| ------------- | ------------- |
| 0             | Low Risk      |
| 1             | Medium Risk   |
| 2             | High Risk     |

---

## Features Used

* age
* sex
* bmi
* children
* smoker
* region

---

## Training Process

1. Loaded the risk classification dataset.
2. Encoded categorical risk labels.
3. Selected input features and target variable.
4. Split data into training and testing datasets.
5. Trained a Random Forest Classifier.
6. Generated predictions on unseen customer records.
7. Evaluated performance using classification metrics.

---

## Model Performance

### Accuracy

**90.30%**

The classifier correctly predicts customer risk categories for approximately 9 out of every 10 customers.

---

## Classification Report

| Risk Class      | Precision | Recall | F1-Score | Support |
| --------------- | --------- | ------ | -------- | ------- |
| Low Risk (0)    | 0.92      | 0.85   | 0.88     | 92      |
| Medium Risk (1) | 0.90      | 0.93   | 0.92     | 88      |
| High Risk (2)   | 0.89      | 0.93   | 0.91     | 88      |

### Overall Performance

| Metric              | Value |
| ------------------- | ----- |
| Accuracy            | 0.90  |
| Macro Average F1    | 0.90  |
| Weighted Average F1 | 0.90  |

---

## Interpretation

* The classifier achieved strong and balanced performance across all risk categories.
* Medium Risk and High Risk customers were identified with particularly high recall.
* Precision values remained consistently high across all classes.
* No major class imbalance issues were observed.
* The model demonstrates strong generalization capability.

---

## Business Impact

The risk prediction model enables:

### Automated Risk Assessment

* Predicts customer risk level instantly.
* Reduces manual evaluation effort.

### Customer Segmentation

* Groups customers into meaningful risk categories.
* Supports personalized service offerings.

### Underwriting Support

* Assists insurance professionals during policy approval.
* Improves consistency in decision-making.

### Policy Recommendation Integration

* Serves as the decision engine for policy recommendation logic.
* Enables automated insurance plan suggestions.

---

## System Workflow

Customer Data Input

↓

Risk Prediction Model

↓

Risk Category Prediction

↓

Policy Recommendation Engine

↓

Recommended Insurance Plan

---

## Key Findings

* Random Forest Classifier achieved 90.30% prediction accuracy.
* Risk categories can be predicted reliably using customer attributes.
* Classification performance is balanced across all customer groups.
* The model successfully automates the risk assessment framework developed previously.
* The system is now capable of generating business-oriented recommendations.

---

## Conclusion

A Random Forest Classifier was successfully developed for customer risk prediction. The model achieved an accuracy of 90.30% and demonstrated balanced performance across Low Risk, Medium Risk, and High Risk customer categories. This model forms the core intelligence layer of the Insurance AI Risk Analysis and Policy Recommendation System and enables automated risk assessment and policy recommendation functionality.
