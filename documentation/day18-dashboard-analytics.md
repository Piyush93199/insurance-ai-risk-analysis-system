# Day 18 Dashboard Analytics Documentation

## Objective

The objective of Day 18 was to transform the Insurance AI Risk Analysis and Policy Recommendation System from a prediction-focused application into an analytics-driven dashboard capable of providing business insights and data visualization.

The focus was on presenting meaningful analytical information derived from the insurance dataset to support decision-making and improve dashboard usability.

---

# Overview

After implementing risk prediction, recommendation generation, and result visualization, the next step was to introduce analytical components that provide a broader understanding of customer risk patterns and model performance.

The dashboard was enhanced with visual analytics sections including risk distribution charts, customer segmentation analysis, model performance metrics, and business intelligence insights.

---

# Enhancements Implemented

## 1. Dashboard Analytics Section

A dedicated analytics section was introduced within the Streamlit dashboard.

### Purpose

* Centralize analytical insights.
* Improve dashboard functionality.
* Provide business-oriented information.

### Benefits

* Better data interpretation.
* Improved decision support.
* Professional dashboard appearance.

---

## 2. Risk Distribution Visualization

A risk distribution chart was implemented to visualize customer distribution across risk categories.

### Dataset Statistics

| Risk Level  | Count |
| ----------- | ----- |
| Low Risk    | 446   |
| Medium Risk | 445   |
| High Risk   | 446   |

### Analysis

The dataset demonstrates a nearly balanced distribution across all three risk categories, ensuring fair model training and reducing class imbalance issues.

### Screenshot

![Risk Distribution](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/risk_distribution_chart.png)

---

## 3. Customer Segmentation Analysis

A customer segmentation chart was created using smoker and non-smoker categories.

### Dataset Statistics

| Customer Type | Count |
| ------------- | ----- |
| Non-Smoker    | 1063  |
| Smoker        | 274   |

### Analysis

Non-smokers constitute the majority of customers within the dataset. Smoking behavior remains one of the strongest indicators of insurance risk and significantly influences policy recommendations.

### Screenshot

![Customer Segmentation](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/customer_segmentation_chart.png)

---

## 4. Model Performance Dashboard

A performance dashboard was implemented to display key machine learning metrics.

### Metrics Displayed

| Metric                     | Value  |
| -------------------------- | ------ |
| Classification Accuracy    | 90.30% |
| Optimized Random Forest R² | 89.38% |

### Analysis

The optimized Random Forest model achieved the highest predictive performance among all tested models and was selected for deployment within the dashboard.

### Screenshot

![Model Performance Dashboard](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/model_performance_dashboard.png)

---

## 5. Business Insights Section

A business insights module was added to communicate actionable findings derived from data analysis and model outputs.

### Key Insights

* Smokers represent the majority of high-risk customers.
* Risk classes are nearly equally distributed.
* Random Forest achieved the strongest predictive performance.
* Automated policy recommendation supports insurance decision-making.

### Benefits

* Converts analytical results into business knowledge.
* Supports management-level interpretation.
* Improves dashboard usefulness.

### Screenshot

![Business Insights](https://raw.githubusercontent.com/Piyush93199/insurance-ai-risk-analysis-system/main/screenshots/business_insights.png)

---

# Dashboard Analytics Workflow

Dataset

↓

Risk Analysis

↓

Customer Segmentation

↓

Model Performance Evaluation

↓

Business Insights Generation

↓

Decision Support Dashboard

---

# Analytical Findings

## Risk Distribution

The balanced distribution of risk categories improves model generalization and prevents bias toward any specific class.

---

## Customer Segmentation

Smoking status remains a highly influential risk factor and plays a critical role in customer classification.

---

## Model Performance

Random Forest outperformed all evaluated models and achieved the highest overall predictive accuracy.

---

## Business Intelligence

The dashboard now provides both operational predictions and strategic insights suitable for insurance decision-making.

---

# Screenshots Included

## Risk Distribution Chart

File:

screenshots/risk_distribution_chart.png

---

## Customer Segmentation Chart

File:

screenshots/customer_segmentation_chart.png

---

## Model Performance Dashboard

File:

screenshots/model_performance_dashboard.png

---

## Business Insights Section

File:

screenshots/business_insights.png

---

# Benefits Achieved

## Technical Benefits

* Enhanced dashboard functionality.
* Improved data visualization.
* Better analytical reporting.

## Business Benefits

* Improved decision support.
* Better customer understanding.
* Increased interpretability of results.

## User Experience Benefits

* Easier data interpretation.
* Professional analytics presentation.
* Improved dashboard usability.

---

# Deliverables Completed

✅ Dashboard Analytics Section

✅ Risk Distribution Visualization

✅ Customer Segmentation Analysis

✅ Model Performance Dashboard

✅ Business Insights Section

✅ Analytics Documentation

✅ Dashboard Screenshots

---

# Outcome

The dashboard has evolved from a simple prediction system into a more comprehensive analytics platform capable of delivering machine learning predictions, customer insights, performance metrics, and business intelligence information.

The enhancements significantly improve the project's suitability for internship evaluation, academic presentations, technical demonstrations, and portfolio showcasing.

---

# Status

Day 18 completed successfully.

Analytics dashboard components have been implemented, tested, documented, and integrated into the Insurance AI Risk Analysis and Policy Recommendation System.
