# Day 7 Progress Report

## Date

Day 7

## Objective

To develop and evaluate a Random Forest Regressor model for insurance charge prediction and compare its performance with previously developed machine learning models.

---

## Activities Performed

* Loaded the processed insurance dataset.
* Prepared input features and target variable for model training.
* Split the dataset into training and testing datasets.
* Trained a Random Forest Regressor model using ensemble learning techniques.
* Generated predictions on unseen test data.
* Evaluated model performance using MAE, MSE, and R² Score.
* Compared Random Forest performance with Linear Regression and Decision Tree models.
* Conducted feature importance analysis.
* Generated Actual vs Predicted visualization.
* Saved the trained model for future deployment and evaluation.

---

## Deliverables Completed

* Random Forest Regressor model developed.
* Model evaluation completed.
* Feature importance analysis performed.
* Model comparison report prepared.
* Actual vs Predicted visualization generated.
* Trained model saved in the repository.
* Documentation updated with findings and observations.

---

## Key Findings

### Model Performance

* Mean Absolute Error (MAE): **2555.93**
* Mean Squared Error (MSE): **21,420,846.46**
* R² Score: **88.34%**

### Feature Importance Findings

* Smoking status was identified as the most influential feature with an importance score of approximately **60%**.
* BMI emerged as the second most important predictor.
* Age contributed significantly to insurance charge prediction.
* Children, region, and gender had comparatively lower impact on model predictions.
* Feature importance results closely aligned with earlier EDA observations.

### Model Comparison

| Metric   | Linear Regression | Decision Tree     | Random Forest |
| -------- | ----------------- | ----------------- | ------------- |
| MAE      | 4182.35           | 2593.36           | **2555.93**   |
| MSE      | 35,493,102.61     | **19,778,189.65** | 21,420,846.46 |
| R² Score | 80.68%            | **89.24%**        | 88.34%        |

### Comparative Analysis

* Random Forest significantly outperformed the Linear Regression baseline model.
* Random Forest achieved the lowest Mean Absolute Error among all developed models.
* Decision Tree achieved the highest R² Score and lowest Mean Squared Error.
* Both tree-based models demonstrated superior performance compared to Linear Regression.
* Ensemble learning effectively captured complex patterns within customer insurance data.

---

## Challenges Faced

* Understanding the impact of ensemble learning on model performance.
* Selecting suitable Random Forest parameters.
* Interpreting feature importance scores.
* Comparing multiple machine learning models objectively.

---

## Resolution

* Applied standard Random Forest configuration for initial experimentation.
* Evaluated performance using multiple regression metrics.
* Conducted feature importance analysis to understand model behavior.
* Compared results across all developed models using a common evaluation framework.

---

## Learning Outcomes

* Learned the fundamentals of ensemble learning techniques.
* Understood how Random Forest combines multiple decision trees for prediction.
* Gained experience in feature importance analysis.
* Improved skills in model comparison and performance evaluation.
* Developed a deeper understanding of predictive modeling for insurance analytics.

---

## Plan for Day 8

* Perform hyperparameter tuning of the Random Forest model.
* Optimize model performance through parameter experimentation.
* Compare tuned and untuned model results.
* Select the final candidate model for deployment.
* Prepare the project for the model optimization phase.

---

## Status

Day 7 objectives completed successfully. The Random Forest Regressor achieved an R² score of 88.34% and delivered the lowest Mean Absolute Error among all tested models. Feature importance analysis confirmed that smoking status, BMI, and age are the primary drivers of insurance charges. While Random Forest demonstrated strong predictive performance, the Decision Tree Regressor remains the best-performing model overall based on R² Score and Mean Squared Error.
