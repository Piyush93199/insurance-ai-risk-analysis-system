# Day 8 Progress Report

## Date

Day 8

## Objective

To optimize the Random Forest model through hyperparameter tuning and identify the best-performing machine learning model for insurance charge prediction.

---

## Activities Performed

* Reviewed the performance of previously developed machine learning models.
* Applied hyperparameter tuning techniques to the Random Forest Regressor.
* Configured advanced model parameters to improve prediction accuracy.
* Trained the optimized Random Forest model on the processed insurance dataset.
* Generated predictions on unseen testing data.
* Evaluated model performance using MAE, MSE, and R² Score.
* Compared optimized model performance with Linear Regression, Decision Tree, and standard Random Forest models.
* Generated visualization of actual versus predicted insurance charges.
* Saved the optimized model for future deployment and integration.

---

## Deliverables Completed

* Optimized Random Forest model developed.
* Hyperparameter tuning completed successfully.
* Performance evaluation completed.
* Comprehensive model comparison prepared.
* Optimized model visualization generated.
* Final candidate model identified.
* Updated project documentation and repository.

---

## Key Findings

### Optimized Random Forest Performance

* Mean Absolute Error (MAE): **2441.70**
* Mean Squared Error (MSE): **19,519,656.07**
* R² Score: **89.38%**

### Performance Improvements

* Achieved the highest R² Score among all developed models.
* Reduced average prediction error compared to previous Random Forest and Decision Tree models.
* Demonstrated improved generalization capability through controlled model complexity.
* Successfully balanced model accuracy and overfitting prevention.

### Model Comparison

| Metric   | Linear Regression | Decision Tree | Random Forest | Optimized Random Forest |
| -------- | ----------------- | ------------- | ------------- | ----------------------- |
| MAE      | 4182.35           | 2593.36       | 2555.93       | **2441.70**             |
| MSE      | 35,493,102.61     | 19,778,189.65 | 21,420,846.46 | **19,519,656.07**       |
| R² Score | 80.68%            | 89.24%        | 88.34%        | **89.38%**              |

---

## Challenges Faced

* Selecting appropriate hyperparameter values without causing overfitting.
* Balancing model complexity and prediction performance.
* Identifying parameter combinations that provide measurable improvements.
* Comparing multiple model versions objectively.

---

## Resolution

* Applied controlled hyperparameter tuning strategies.
* Evaluated model performance using multiple regression metrics.
* Compared optimized and non-optimized models systematically.
* Selected parameters that improved both accuracy and generalization performance.

---

## Learning Outcomes

* Learned practical hyperparameter tuning techniques for ensemble models.
* Understood the impact of model parameters on predictive performance.
* Gained experience in model optimization and validation.
* Improved understanding of bias-variance trade-offs in machine learning.
* Developed skills in selecting the best-performing model based on objective evaluation criteria.

---

## Business Impact

* Improved insurance charge prediction accuracy.
* Enhanced reliability of customer risk assessment.
* Strengthened the foundation for policy recommendation functionality.
* Increased the practical applicability of the system for insurance analytics.

---

## Plan for Day 9

* Develop customer risk categorization methodology.
* Define Low Risk, Medium Risk, and High Risk customer segments.
* Build customer risk scoring logic.
* Create the foundation for the policy recommendation system.
* Begin transitioning from prediction-focused development to decision-support functionality.

---

## Status

Day 8 objectives completed successfully. Hyperparameter tuning improved model performance and established the Optimized Random Forest Regressor as the best-performing model in the project. With an R² Score of 89.38%, the optimized model has been selected as the final prediction engine for the Insurance AI Risk Analysis and Policy Recommendation System.
