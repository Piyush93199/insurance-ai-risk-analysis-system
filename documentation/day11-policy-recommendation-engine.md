# Day 11 Policy Recommendation Engine

## Objective

Develop an integrated policy recommendation engine that combines customer risk prediction with personalized insurance policy recommendations.

---

## System Overview

The policy recommendation engine integrates the previously developed Risk Prediction Model with a rule-based recommendation framework.

The complete workflow is:

Customer Data
↓
Risk Prediction Model
↓
Risk Category Prediction
↓
Policy Recommendation
↓
Insurance Plan Suggestion

---

## Components Used

### Risk Prediction Model

- Random Forest Classifier
- Accuracy: 90.30%

### Risk Categories

- Low Risk
- Medium Risk
- High Risk

### Recommended Policies

| Risk Level | Recommended Policy |
|------------|-------------------|
| Low Risk | Basic Insurance Plan |
| Medium Risk | Standard Insurance Plan |
| High Risk | Premium Insurance Plan |

---

## Recommendation Logic

The system predicts the customer's risk level and automatically assigns a suitable insurance policy.

### Low Risk Customers

Characteristics:

- Lower insurance costs
- Lower risk exposure
- Younger and healthier profiles

Recommendation:

Basic Insurance Plan

### Medium Risk Customers

Characteristics:

- Moderate insurance costs
- Average risk exposure

Recommendation:

Standard Insurance Plan

### High Risk Customers

Characteristics:

- Higher insurance costs
- Smoking or health-related risk factors
- Greater financial exposure

Recommendation:

Premium Insurance Plan

---

## Sample Customer Prediction

### Customer Profile

- Age: 45
- BMI: 31.5
- Children: 2
- Smoker: Yes

### System Output

Customer Risk Level: High Risk

Recommended Policy: Premium Insurance Plan

---

## Recommendation Engine Testing

| Age | Smoker | BMI | Risk Level | Recommended Policy |
|------|---------|------|------------|-------------------|
| 25 | No | 22 | Low Risk | Basic Insurance Plan |
| 45 | Yes | 30 | High Risk | Premium Insurance Plan |
| 60 | Yes | 36 | High Risk | Premium Insurance Plan |

### Observations

- Low-risk customers receive basic plans.
- High-risk customers receive premium plans.
- Smoking status significantly influences recommendations.
- Recommendations are consistent with risk prediction outputs.

---

## Business Impact

The recommendation engine enables:

- Automated insurance recommendations.
- Personalized customer experiences.
- Improved underwriting support.
- Faster decision-making.
- Data-driven insurance planning.

---

## Key Findings

- Risk prediction and recommendation systems were successfully integrated.
- Recommendations are generated automatically.
- The workflow supports real-world insurance decision-making.
- The system transforms machine learning predictions into actionable business recommendations.

---

## Conclusion

An integrated policy recommendation engine was successfully developed. The system combines customer risk prediction with policy recommendation logic to generate personalized insurance suggestions. This marks the completion of the core Insurance AI Risk Analysis and Policy Recommendation System functionality.