# Day 3 EDA Findings

## Objective

To explore the dataset, understand feature distributions, identify patterns, and extract insights relevant to insurance risk assessment and policy recommendation.

---

## Age Analysis

![Age Distribution](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/age_distribution.png)

### Observations

* Customer ages are distributed across a broad range.
* Most records belong to the working-age population.
* Age appears to have a meaningful influence on insurance costs.
* Older customers are likely to have higher risk profiles compared to younger customers.

---

## BMI Analysis

![BMI Distribution](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/bmi_distribution.png)

### Observations

* Most BMI values fall within the normal to overweight range.
* A few extreme BMI values are present, indicating potential outliers.
* Higher BMI may be associated with increased health risks and insurance expenses.

---

## Insurance Charges Analysis

![Charges Distribution](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/charges_distribution.png)

### Observations

* Insurance charges are not normally distributed.
* Most customers incur relatively low to moderate charges.
* A small group of customers generates significantly higher insurance costs.
* The presence of high-cost outliers indicates strong influence from certain risk factors.

---

## Smoking Status Analysis

![Smoker Analysis](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/smoker_analysis.png)

### Observations

* Smokers incur substantially higher insurance charges than non-smokers.
* Smoking status is one of the strongest indicators of customer risk.
* This feature is expected to have high predictive importance during model training.

---

## Gender Analysis

![Gender Analysis](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/gender_analysis.png)

### Observations

* Insurance charges for males and females are relatively similar.
* Gender does not appear to independently drive insurance costs.
* Other factors such as smoking status, age, and BMI have greater influence.

---

## Key Insights

* Smoking status is the strongest predictor of insurance charges.
* Age contributes significantly to customer risk assessment.
* BMI can be used as a health-related risk indicator.
* Insurance charges contain several high-cost cases that should be considered during model development.
* Risk prediction models should prioritize smoking status, age, and BMI as important features.

---

## Conclusion

Exploratory Data Analysis identified several meaningful relationships within the dataset. Smoking status emerged as the most influential factor affecting insurance charges, followed by age and BMI. These findings will guide feature engineering and machine learning model development in the next phase of the project.
