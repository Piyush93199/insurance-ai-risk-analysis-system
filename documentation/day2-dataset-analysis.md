# Day 2 Dataset Analysis

## Dataset Information

**Dataset Name:** Medical Cost Insurance Dataset

**Source:** Public Insurance Dataset

## Dataset Overview

The dataset contains customer demographic, lifestyle, and insurance-related information that can be used for risk assessment and predictive analytics. It includes both numerical and categorical features commonly used in insurance decision-making.

## Features

| Feature  | Description          |
| -------- | -------------------- |
| age      | Age of customer      |
| sex      | Gender of customer   |
| bmi      | Body Mass Index      |
| children | Number of dependents |
| smoker   | Smoking status       |
| region   | Residential region   |
| charges  | Insurance charges    |

## Dataset Statistics

### Number of Records

1338 customer records

### Number of Features

7 features

### Missing Values

No missing values were detected in the dataset. All records were complete and suitable for analysis without requiring missing value treatment.

### Data Types

- Numerical Features:
  - age
  - bmi
  - children
  - charges

- Categorical Features:
  - sex
  - smoker
  - region

## Initial Observations

* Dataset contains both numerical and categorical variables.
* Insurance charges appear to be the target variable.
* Smoking status is expected to significantly impact insurance costs.
* Dataset is suitable for predictive modeling and customer risk assessment.

## Relevance to Project

The dataset supports the primary objectives of the project:

* Customer risk analysis
* Insurance cost prediction
* Customer segmentation
* Insurance recommendation system development

## Next Steps

* Perform Exploratory Data Analysis (EDA)
* Analyze feature distributions
* Identify feature relationships
* Detect outliers
* Prepare data for machine learning models
