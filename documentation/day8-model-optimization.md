# Day 8 Model Optimization

## Objective

To optimize the Random Forest model through hyperparameter tuning and improve the predictive performance of the Insurance AI Risk Analysis and Policy Recommendation System.

---

## Background

After evaluating Linear Regression, Decision Tree Regressor, and Random Forest Regressor models, further optimization was required to improve prediction accuracy and identify the most suitable model for deployment.

Hyperparameter tuning was performed on the Random Forest model to reduce prediction errors and enhance overall model performance.

---

## Optimization Strategy

The following optimization techniques were applied:

* Increased the number of decision trees.
* Controlled maximum tree depth.
* Adjusted node splitting requirements.
* Introduced minimum leaf size constraints.
* Reduced overfitting while improving generalization performance.

### Optimized Parameters

| Parameter         | Value |
| ----------------- | ----- |
| n_estimators      | 300   |
| max_depth         | 10    |
| min_samples_split | 5     |
| min_samples_leaf  | 2     |
| random_state      | 42    |

---

## Training Process

The following steps were performed:

1. Loaded the processed insurance dataset.
2. Selected input features and target variable.
3. Split the dataset into training and testing datasets.
4. Applied optimized Random Forest configuration.
5. Trained the model using training data.
6. Generated predictions on testing data.
7. Evaluated model performance using regression metrics.
8. Compared optimized results with all previously developed models.

---

## Evaluation Metrics

### Mean Absolute Error (MAE)

**2441.70**

The optimized model predicts insurance charges with an average error of approximately 2442 units.

### Mean Squared Error (MSE)

**19,519,656.07**

The optimized model achieved the lowest prediction error among all developed models.

### R² Score

**89.38%**

The optimized model explains approximately 89.38% of the variation in insurance charges and achieved the highest predictive performance in the project.

---

## Model Visualization

![Optimized Random Forest](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/optimized_random_forest.png)

*Figure 1: Actual vs Predicted insurance charges using the optimized Random Forest model.*

### Interpretation

* Predicted values closely align with actual insurance charges.
* The model captures both simple and complex relationships within the dataset.
* Prediction consistency improved after hyperparameter tuning.
* The optimized model demonstrates strong generalization capability.

---

## Performance Comparison

| Metric   | Linear Regression | Decision Tree | Random Forest | Optimized Random Forest |
| -------- | ----------------- | ------------- | ------------- | ----------------------- |
| MAE      | 4182.35           | 2593.36       | 2555.93       | **2441.70**             |
| MSE      | 35,493,102.61     | 19,778,189.65 | 21,420,846.46 | **19,519,656.07**       |
| R² Score | 80.68%            | 89.24%        | 88.34%        | **89.38%**              |

---

## Improvement Analysis

### Compared to Linear Regression

* MAE reduced by approximately 41.6%.
* MSE reduced by approximately 45%.
* R² Score improved from 80.68% to 89.38%.

### Compared to Initial Random Forest

* MAE improved from 2555.93 to 2441.70.
* MSE improved from 21,420,846.46 to 19,519,656.07.
* R² Score improved from 88.34% to 89.38%.

### Compared to Decision Tree

* Achieved higher R² Score.
* Reduced overall prediction error.
* Demonstrated better model stability and generalization.

---

## Key Findings

* Hyperparameter tuning successfully improved model performance.
* Optimized Random Forest achieved the highest R² Score among all developed models.
* Prediction errors were reduced significantly compared to baseline models.
* Ensemble learning proved highly effective for insurance charge prediction.
* The optimized model provides a strong foundation for risk assessment and policy recommendation tasks.

---

## Business Relevance

The optimized model can assist insurance organizations in:

* Estimating customer insurance charges.
* Identifying high-risk customers.
* Supporting premium calculation decisions.
* Improving underwriting efficiency.
* Enabling data-driven policy recommendations.

---

## Final Model Selection

Based on evaluation results, the **Optimized Random Forest Regressor** has been selected as the final prediction model for the Insurance AI Risk Analysis and Policy Recommendation System.

### Selected Model Performance

* MAE: **2441.70**
* MSE: **19,519,656.07**
* R² Score: **89.38%**

---

## Conclusion

Random Forest hyperparameter tuning successfully improved predictive performance and established the Optimized Random Forest Regressor as the best-performing model developed during the project. The model achieved the highest accuracy, lowest prediction error, and strongest overall performance among all evaluated algorithms. It has been selected as the final candidate model and will serve as the core prediction engine for subsequent risk analysis and policy recommendation modules.
