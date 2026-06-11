# Day 9 Risk Classification System

## Objective

Develop a customer risk classification framework and establish the foundation for an intelligent insurance policy recommendation system.

---

## Background

The optimized Random Forest model successfully predicts insurance charges with high accuracy. However, insurance organizations require actionable business insights rather than numerical predictions alone.

To address this requirement, a customer risk classification system was developed to categorize customers into distinct risk groups and provide corresponding insurance policy recommendations.

---

## Risk Classification Framework

Customers were segmented into three risk categories based on insurance charge distribution using quantile-based classification.

### Risk Categories

#### Low Risk

Customers with relatively lower insurance charges and lower overall risk exposure.

#### Medium Risk

Customers with moderate insurance charges and average risk profiles.

#### High Risk

Customers with higher insurance charges and increased risk exposure.

---

## Classification Methodology

The insurance charge variable was divided into three equally distributed segments using quantile-based categorization.

### Risk Assignment Logic

* Lower charge segment → Low Risk
* Middle charge segment → Medium Risk
* Higher charge segment → High Risk

This approach ensures balanced risk distribution across customer groups.

---

## Risk Distribution Analysis

| Risk Level  | Customer Count |
| ----------- | -------------- |
| Low Risk    | 446            |
| Medium Risk | 445            |
| High Risk   | 446            |

### Observations

* Customer distribution is balanced across all risk categories.
* Each risk group contains approximately one-third of the dataset.
* Balanced segmentation improves future classification model development.
* The framework successfully separates customers into meaningful business groups.

---

## Risk Distribution Visualization

![Risk Distribution](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/risk_distribution.png)

*Figure 1: Distribution of customers across risk categories.*

---

## Age-Based Risk Analysis

| Risk Level  | Average Age |
| ----------- | ----------- |
| Low Risk    | 26.52 Years |
| Medium Risk | 47.96 Years |
| High Risk   | 43.21 Years |

### Interpretation

* Low-risk customers are significantly younger than other groups.
* Medium-risk customers have the highest average age.
* High-risk customers also maintain relatively high average ages.
* Age contributes meaningfully to insurance risk assessment.
* Younger customers generally exhibit lower insurance expenses and reduced risk exposure.

---

## Smoking vs Risk Analysis

| Smoker Status | Low Risk | Medium Risk | High Risk |
| ------------- | -------- | ----------- | --------- |
| Non-Smoker    | 446      | 445         | 172       |
| Smoker        | 0        | 0           | 274       |

### Interpretation

* All smokers were classified into the High Risk category.
* No smokers appeared in Low Risk or Medium Risk groups.
* Smoking status remains the strongest customer risk indicator.
* Results validate earlier machine learning findings and feature importance analysis.

---

## Key Findings

### Customer Risk Drivers

#### Smoking Status

* Most influential risk factor.
* Strongly associated with higher insurance charges.
* Primary determinant of customer risk level.

#### Age

* Significant contributor to risk classification.
* Older customers generally exhibit higher risk levels.

#### Health Indicators

* BMI contributes substantially to insurance charge prediction.
* Supports health-based risk assessment.

---

## Policy Recommendation Framework

The risk classification system was integrated with a basic recommendation engine.

### Low Risk Customers

**Recommended Policy:** Basic Insurance Plan

Characteristics:

* Lower insurance costs
* Lower risk exposure
* Younger customer profiles
* Standard coverage requirements

---

### Medium Risk Customers

**Recommended Policy:** Standard Insurance Plan

Characteristics:

* Moderate insurance expenses
* Balanced risk profile
* Average protection requirements
* Extended coverage options

---

### High Risk Customers

**Recommended Policy:** Premium Insurance Plan

Characteristics:

* Higher insurance costs
* Increased health or lifestyle risks
* Greater financial exposure
* Enhanced coverage requirements

---

## Recommendation Logic

The recommendation system follows the following rule set:

| Risk Level  | Recommended Policy      |
| ----------- | ----------------------- |
| Low Risk    | Basic Insurance Plan    |
| Medium Risk | Standard Insurance Plan |
| High Risk   | Premium Insurance Plan  |

---

## Business Impact

The risk classification framework provides several practical benefits:

### Customer Segmentation

* Groups customers based on risk exposure.
* Enables targeted business strategies.

### Personalized Recommendations

* Supports individualized policy suggestions.
* Improves customer experience.

### Underwriting Support

* Assists insurance professionals in risk evaluation.
* Enhances decision-making efficiency.

### Risk Management

* Improves identification of high-risk customers.
* Supports premium planning and policy structuring.

---

## System Architecture Progress

Completed Components:

* Insurance Domain Research
* Dataset Collection and Analysis
* Exploratory Data Analysis
* Data Preprocessing
* Linear Regression Model
* Decision Tree Model
* Random Forest Model
* Optimized Random Forest Model
* Risk Classification System
* Policy Recommendation Framework

Current Best Model:

**Optimized Random Forest Regressor**

Performance:

* MAE: 2441.70
* MSE: 19,519,656.07
* R² Score: 89.38%

---

## Conclusion

A customer risk classification framework was successfully developed and integrated into the Insurance AI Risk Analysis and Policy Recommendation System. Customers were segmented into Low Risk, Medium Risk, and High Risk categories using charge-based quantile classification. Analysis confirmed that smoking status is the strongest determinant of customer risk, while age and health-related factors also contribute significantly. The addition of risk categorization and policy recommendation logic transforms the project from a predictive analytics model into a practical insurance decision-support system capable of delivering meaningful business insights and personalized policy recommendations.
