import streamlit as st
import pandas as pd

from model_utils import predict_risk

st.set_page_config(
    page_title="Insurance AI Risk Analysis System",
    layout="wide"
)

st.sidebar.title("Navigation")

st.sidebar.markdown(
"""
### Insurance AI System

- Risk Prediction
- Policy Recommendation
- Customer Analysis
"""
)

st.title("🏥 Insurance AI Risk Analysis System")

st.markdown(
"""
### AI-Powered Insurance Risk Assessment & Policy Recommendation Platform
"""
)

st.markdown("---")

st.subheader("Project Information")

st.info(
    """
    This AI-powered system analyzes customer information,
    predicts insurance risk levels, and recommends
    suitable insurance policies using Machine Learning.
    """
)

st.write(
    "Predict customer risk levels and receive policy recommendations."
)

st.subheader("Customer Information")

left_col, right_col = st.columns(2)

with left_col:

    age = st.slider(
    "Age",
    18,
    100,
    30
    )

    sex = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0
    )

with right_col:

    children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
    )

    smoker = st.selectbox(
    "Smoker",
    ["No", "Yes"]
    )

    region = st.selectbox(
        "Region",
        [
            "Northeast",
            "Northwest",
            "Southeast",
            "Southwest"
        ]
    )

if st.button("🔍 Analyze Customer", use_container_width=True):

    customer = pd.DataFrame({

        "age": [age],

        "sex": [
            1 if sex == "Male" else 0
        ],

        "bmi": [bmi],

        "children": [children],

        "smoker": [
            1 if smoker == "Yes" else 0
        ],

        "region": [
            {
                "northeast": 0,
                "northwest": 1,
                "southeast": 2,
                "southwest": 3
            }[
                region.lower()
            ]
        ]
    })

    st.subheader("Prediction Results")

    risk, recommendation = predict_risk(customer)

    st.balloons()

    st.success(
        "Analysis Completed Successfully"
    )

    if risk == "Low Risk":

        st.success(
            f"🟢 Risk Level: {risk}"
        )

    elif risk == "Medium Risk":

        st.warning(
            f"🟡 Risk Level: {risk}"
        )

    else:

        st.error(
            f"🔴 Risk Level: {risk}"
        )

    st.markdown("### Recommended Insurance Plan")

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:10px;
            background-color:#0000001A;
            border-left:6px solid #2563EB;
        ">
            <h4>{recommendation}</h4>
            <p>
            Policy recommendation generated using
            customer risk assessment and machine
            learning analysis.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("Customer Analysis Summary")

    st.write(f"Age: {age}")
    st.write(f"BMI: {bmi}")
    st.write(f"Children: {children}")
    st.write(f"Smoking Status: {smoker}")
    st.write(f"Region: {region}")

    st.markdown("---")

    st.subheader("Risk Interpretation")

    if risk == "Low Risk":

        st.info(
            """
            Customer shows low insurance risk.
            Suitable for standard insurance plans.
            """
        )

    elif risk == "Medium Risk":

        st.warning(
            """
            Customer shows moderate risk factors.
            Enhanced policy coverage is recommended.
            """
        )

    else:

        st.error(
            """
            Customer exhibits high risk characteristics.
            Premium insurance plans are recommended.
            """
        )

    st.markdown("---")

    st.header("📊 Dashboard Analytics")

    risk_distribution = {
    "Low Risk": 446,
    "Medium Risk": 445,
    "High Risk": 446
    }

    risk_df = pd.DataFrame(
        {
            "Risk Level": risk_distribution.keys(),
            "Customers": risk_distribution.values()
        }
    )

    st.subheader("Risk Distribution")

    st.bar_chart(
        risk_df.set_index("Risk Level")
    )

    segment_df = pd.DataFrame(
        {
            "Customer Type": [
                "Non-Smoker",
                "Smoker"
            ],
            "Count": [
                1063,
                274
            ]
        }
    )

    st.subheader("Customer Segmentation")

    st.bar_chart(
        segment_df.set_index(
            "Customer Type"
        )
    )

st.subheader("Model Performance")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Classification Accuracy",
        "90.30%"
    )

with col2:

    st.metric(
        "Optimized Random Forest R²",
        "89.38%"
    )

with col3:
    st.metric(
        "Dataset Records",
        "1338"
    )

st.subheader(
    "Business Insights"
)

st.info(
    """
    • Smokers represent the majority of high-risk customers.

    • Low-risk and high-risk customers are almost equally distributed.

    • Random Forest achieved the best overall predictive performance.

    • The recommendation engine can support insurance decision-making.
    """
)

st.caption(
    "Insurance AI Risk Analysis and Policy Recommendation System | AI/ML Internship Project"
)