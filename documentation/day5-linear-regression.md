# Day 5 Linear Regression Model

## Objective

Develop and evaluate a baseline machine learning model for insurance charge prediction.

## Model Used

Linear Regression

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
* Trained a Linear Regression model using the training data.
* Generated predictions on the testing dataset.
* Evaluated model performance using regression metrics.

## Evaluation Metrics

### Mean Absolute Error (MAE)

**4182.35**

The model's predictions differ from actual insurance charges by approximately 4182 units on average.

### Mean Squared Error (MSE)

**35,493,102.61**

This metric indicates the average squared prediction error and highlights the impact of larger prediction deviations.

### R² Score

**0.8068 (80.68%)**

The model explains approximately 80.68% of the variation in insurance charges, indicating strong predictive performance for a baseline model.

## Model Visualization

![Actual vs Predicted Charges](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/actual_vs_predicted.png)

*Figure 1: Comparison between actual insurance charges and model predictions.*

### Interpretation

- The scatter plot demonstrates a strong positive relationship between actual and predicted insurance charges.
- Most prediction points closely follow the overall trend of the actual values.
- The model performs well for the majority of customers in the dataset.
- Some prediction deviations are visible for higher insurance charge values.
- The visualization supports the model's R² score of 80.68%, indicating good predictive performance.

## Observations

* The model achieved a strong R² score above 0.80.
* Smoking status, age, and BMI appear to contribute significantly to prediction accuracy.
* The model performs well as an initial benchmark for future comparisons.
* Further improvements may be achieved using advanced machine learning algorithms.

## Conclusion

A Linear Regression model was successfully developed and evaluated for insurance charge prediction. The model achieved an R² score of 80.68%, making it a strong baseline model for subsequent experimentation and performance comparison.
