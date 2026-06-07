# Day 6 Decision Tree Regressor

## Objective

Develop and evaluate a Decision Tree Regressor for insurance charge prediction and compare its performance with the baseline Linear Regression model.

## Model Used

Decision Tree Regressor

## Features Used

* age
* sex
* bmi
* children
* smoker
* region

## Target Variable

* charges

## Training Process

* Loaded the processed insurance dataset.
* Selected relevant input features and target variable.
* Split the dataset into training and testing sets.
* Trained a Decision Tree Regressor model.
* Generated predictions on unseen test data.
* Evaluated model performance using regression metrics.

## Evaluation Metrics

### Mean Absolute Error (MAE)

**2593.36**

The model's predictions differ from actual insurance charges by approximately 2593 units on average.

### Mean Squared Error (MSE)

**19,778,189.65**

The Decision Tree model significantly reduced prediction error compared to the baseline model.

### R² Score

**0.8924 (89.24%)**

The model explains approximately 89.24% of the variation in insurance charges, demonstrating strong predictive performance.

## Model Visualization

![Decision Tree: Actual vs Predicted](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/decision_tree_actual_vs_predicted.png)

*Figure 1: Comparison between actual insurance charges and Decision Tree predictions.*

### Interpretation

* The scatter plot demonstrates a strong relationship between actual and predicted insurance charges.
* Most prediction points align closely with the actual values, indicating improved accuracy.
* The model captures complex patterns in customer insurance costs more effectively than Linear Regression.
* Some prediction deviations remain for extreme insurance charge values.
* The visualization supports the achieved R² score of 89.24%, indicating strong predictive performance.

## Model Comparison

| Metric   | Linear Regression | Decision Tree |
| -------- | ----------------- | ------------- |
| MAE      | 4182.35           | 2593.36       |
| MSE      | 35,493,102.61     | 19,778,189.65 |
| R² Score | 0.8068            | 0.8924        |

### Comparison Analysis

* Decision Tree outperformed Linear Regression across all evaluation metrics.
* The model achieved higher prediction accuracy and lower error rates.
* Decision Tree successfully captured complex relationships within the dataset.
* The improvement indicates that insurance charge prediction benefits from non-linear modeling techniques.

## Observations

* Smoking status remains a highly influential feature.
* Decision Tree handled variations in customer profiles more effectively.
* Prediction accuracy improved significantly compared to the baseline model.

## Conclusion

The Decision Tree Regressor achieved an R² score of 89.24%, outperforming the Linear Regression model. Based on current results, Decision Tree is the best-performing model developed so far and serves as a strong candidate for the final recommendation system.
