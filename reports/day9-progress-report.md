# Day 9 Progress Report

## Date

Day 9

## Objective

To develop a customer risk classification framework and establish the foundation for an intelligent insurance policy recommendation system.

---

## Activities Performed

* Created customer risk categories using insurance charge-based segmentation.
* Classified customers into Low Risk, Medium Risk, and High Risk groups.
* Analyzed risk distribution across the dataset.
* Studied the relationship between customer age and risk level.
* Investigated the impact of smoking status on risk classification.
* Developed initial policy recommendation logic.
* Generated supporting visualizations for risk analysis.
* Prepared a risk-classified dataset for future development.

---

## Deliverables Completed

* Customer risk classification framework developed.
* Risk distribution analysis completed.
* Age-based risk analysis completed.
* Smoking vs Risk analysis completed.
* Policy recommendation logic implemented.
* Risk classification dataset generated.
* Documentation and findings recorded.

---

## Risk Distribution

| Risk Level  | Customers |
| ----------- | --------- |
| Low Risk    | 446       |
| Medium Risk | 445       |
| High Risk   | 446       |

### Observation

* Customer distribution is balanced across all three risk categories.
* The classification framework successfully segmented customers into meaningful groups.
* Balanced classes will support future machine learning classification tasks.

---

## Key Findings

### Age-Based Analysis

| Risk Level  | Average Age |
| ----------- | ----------- |
| Low Risk    | 26.52 Years |
| Medium Risk | 47.96 Years |
| High Risk   | 43.21 Years |

**Insights**

* Low-risk customers are considerably younger.
* Medium and High-risk customers tend to be older.
* Age contributes significantly to insurance risk assessment.

### Smoking vs Risk Analysis

| Smoker Status | Low Risk | Medium Risk | High Risk |
| ------------- | -------- | ----------- | --------- |
| Non-Smoker    | 446      | 445         | 172       |
| Smoker        | 0        | 0           | 274       |

**Insights**

* All smokers were classified into the High Risk category.
* No smokers appeared in Low Risk or Medium Risk groups.
* Smoking status remains the strongest customer risk indicator.
* Findings align with previous machine learning feature importance results.

---

## Policy Recommendation Framework

### Low Risk

Recommended Policy:

* Basic Insurance Plan

### Medium Risk

Recommended Policy:

* Standard Insurance Plan

### High Risk

Recommended Policy:

* Premium Insurance Plan

---

## Challenges Faced

* Defining meaningful risk categories from continuous insurance charge values.
* Translating predictive outputs into actionable business recommendations.
* Ensuring balanced customer segmentation.

---

## Resolution

* Applied quantile-based segmentation to create balanced risk groups.
* Developed a rule-based recommendation framework.
* Validated risk categories using customer characteristics and risk indicators.

---

## Learning Outcomes

* Learned practical customer segmentation techniques.
* Understood the importance of risk classification in insurance analytics.
* Gained experience in transforming predictive insights into business decisions.
* Developed foundational recommendation system logic.
* Improved understanding of customer risk assessment methodologies.

---

## Business Impact

* Enables customer risk profiling.
* Supports personalized insurance recommendations.
* Assists underwriting and premium decision-making.
* Improves customer segmentation and risk management.
* Provides the foundation for an intelligent insurance recommendation engine.

---

## Plan for Day 10

* Build a machine learning risk classification model.
* Predict customer risk category automatically.
* Evaluate classification performance.
* Improve recommendation logic using model outputs.
* Move toward a complete end-to-end Insurance AI Risk Analysis and Policy Recommendation System.

---

## Status

Day 9 objectives completed successfully. A balanced customer risk classification framework was developed, and a policy recommendation system was established. Analysis confirmed that smoking status is the strongest risk indicator, while age also plays a significant role in customer risk assessment. The project has successfully transitioned from pure prediction modeling to business-oriented decision support functionality.
