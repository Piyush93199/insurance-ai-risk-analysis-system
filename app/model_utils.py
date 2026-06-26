import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

risk_model = joblib.load(
    BASE_DIR / "models" / "risk_classifier.pkl"
)

risk_labels = {
    0: "High Risk",
    1: "Low Risk",
    2: "Medium Risk"
}

def recommend_policy(risk_level):

    recommendations = {

        "Low Risk":
        """
        Basic Insurance Plan

        • Affordable Premium

        • Essential Coverage

        • Suitable for Low-Risk Customers
        """,

        "Medium Risk":
        """
        Standard Insurance Plan

        • Balanced Coverage

        • Moderate Premium

        • Additional Protection Benefits
        """,

        "High Risk":
        """
        Premium Insurance Plan

        • Comprehensive Coverage

        • Higher Claim Protection

        • Suitable for High-Risk Customers
        """
    }

    return recommendations[risk_level]


def predict_risk(customer_data):

    prediction = risk_model.predict(customer_data)[0]

    risk = risk_labels[prediction]

    recommendation = recommend_policy(risk)

    return risk, recommendation