import streamlit as st
import pandas as pd

from model_utils import predict_risk

st.set_page_config(
    page_title="Insurance AI Risk Analysis System",
    layout="centered"
)

st.title("🏥 Insurance AI Risk Analysis System")

st.markdown(
"""
This system predicts customer insurance risk levels and recommends
appropriate insurance plans using Machine Learning.
"""
)

st.write(
    "Predict customer risk levels and receive policy recommendations."
)

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

if st.button("Analyze Customer"):

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

    risk, recommendation = predict_risk(customer)

    if risk == "Low Risk":
        st.success("🟢 Low Risk Customer")

    elif risk == "Medium Risk":
        st.warning("🟡 Medium Risk Customer")

    else:
        st.error("🔴 High Risk Customer")

    st.success(
        f"Risk Level: {risk}"
    )

    st.info(
        f"Recommended Policy: {recommendation}"
    )
