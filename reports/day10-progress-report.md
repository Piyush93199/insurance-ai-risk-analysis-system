# Day 10 Progress Report

## Date

Day 10

## Objective

To develop and evaluate a machine learning model capable of automatically predicting customer risk categories.

---

## Activities Performed

* Loaded the risk classification dataset.
* Encoded customer risk labels.
* Prepared training and testing datasets.
* Trained a Random Forest Classifier.
* Generated risk predictions on unseen customer records.
* Evaluated classification accuracy.
* Analyzed precision, recall, and F1-scores.
* Studied model performance across all risk categories.
* Prepared the model for integration with the recommendation system.

---

## Deliverables Completed

* Risk prediction model developed.
* Classification accuracy evaluation completed.
* Classification report generated.
* Automated customer risk prediction workflow established.
* Trained classifier saved in the repository.
* Documentation updated with model findings.

---

## Key Findings

### Model Performance

* Accuracy: **90.30%**
* Macro Average F1-Score: **0.90**
* Weighted Average F1-Score: **0.90**

### Class-wise Performance

| Risk Class  | Precision | Recall | F1-Score |
| ----------- | --------- | ------ | -------- |
| Low Risk    | 0.92      | 0.85   | 0.88     |
| Medium Risk | 0.90      | 0.93   | 0.92     |
| High Risk   | 0.89      | 0.93   | 0.91     |

### Insights

* The model achieved strong classification performance.
* Risk prediction is reliable across all customer categories.
* Medium Risk and High Risk customers were identified with particularly high recall.
* The classifier successfully automates customer risk assessment.

---

## Challenges Faced

* Converting business-defined risk categories into machine learning targets.
* Evaluating classification performance across multiple customer groups.
* Ensuring balanced prediction quality across all classes.

---

## Resolution

* Applied label encoding for risk categories.
* Used Random Forest Classifier for robust classification.
* Evaluated model performance using multiple classification metrics.

---

## Learning Outcomes

* Learned practical classification modeling techniques.
* Understood precision, recall, and F1-score evaluation metrics.
* Gained experience in customer risk prediction systems.
* Improved understanding of business-oriented machine learning applications.
* Developed an automated customer risk assessment solution.

---

## Plan for Day 11

* Develop integrated policy recommendation engine.
* Connect risk prediction outputs with insurance plan recommendations.
* Create end-to-end prediction workflow.
* Build customer recommendation interface logic.
* Move toward a complete Insurance AI Risk Analysis and Policy Recommendation System.

---

## Status

Day 10 objectives completed successfully. A Random Forest Classifier was developed and achieved 90.30% accuracy in predicting customer risk categories. The project now includes predictive analytics, risk classification, and automated risk prediction capabilities, forming the foundation of a complete insurance decision-support system.
