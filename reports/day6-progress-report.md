# Day 6 Progress Report

## Date

Day 6

## Objective

To develop and evaluate a Decision Tree Regressor model for insurance charge prediction and compare its performance with the previously developed Linear Regression model.

---

## Activities Performed

* Loaded the processed insurance dataset.
* Prepared input features and target variable.
* Split the dataset into training and testing sets.
* Trained a Decision Tree Regressor model.
* Generated predictions on test data.
* Evaluated model performance using regression metrics.
* Compared results with the Linear Regression baseline model.
* Generated visualization for actual versus predicted values.
* Saved the trained model for future use.

---

## Deliverables Completed

* Decision Tree Regressor model developed.
* Model evaluation completed.
* Actual vs Predicted visualization generated.
* Model comparison analysis performed.
* Trained model saved in the project repository.
* Documentation updated with findings and observations.

---

## Key Findings

* Decision Tree achieved an R² Score of **89.24%**.
* Mean Absolute Error (MAE) was reduced to **2593.36**.
* Mean Squared Error (MSE) decreased to **19,778,189.65**.
* Decision Tree significantly outperformed the Linear Regression model.
* Non-linear relationships within customer data were captured more effectively.

### Model Comparison

| Metric   | Linear Regression | Decision Tree |
| -------- | ----------------- | ------------- |
| MAE      | 4182.35           | 2593.36       |
| MSE      | 35,493,102.61     | 19,778,189.65 |
| R² Score | 80.68%            | 89.24%        |

---

## Challenges Faced

* Selecting suitable Decision Tree parameters to balance accuracy and complexity.
* Preventing excessive model growth that could lead to overfitting.
* Evaluating performance improvements against the baseline model.

---

## Resolution

* Applied controlled tree depth during training.
* Used regression evaluation metrics for objective comparison.
* Analyzed prediction outputs and visualization results to assess model effectiveness.

---

## Learning Outcomes

* Learned how Decision Tree Regression models work.
* Understood the advantages of non-linear machine learning algorithms.
* Gained experience in model evaluation and performance comparison.
* Improved understanding of insurance charge prediction using machine learning.

---

## Plan for Day 7

* Develop a Random Forest Regressor model.
* Compare performance across multiple algorithms.
* Analyze feature importance.
* Identify the most suitable model for the final system.

---

## Status

Day 6 objectives completed successfully. The Decision Tree Regressor achieved an R² score of 89.24%, outperforming the Linear Regression baseline and becoming the best-performing model developed so far.
