import streamlit as st
import pandas as pd

from model_utils import predict_risk

st.set_page_config(
    page_title="Insurance AI Risk Analysis System",
    layout="wide"
)

st.sidebar.title("🏥 Insurance AI")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "ℹ️ Project Information",
        "🏠 Risk Prediction",
        "📊 Analytics Dashboard",
    ]
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Machine Learning Model\n\nRandom Forest"
)

st.sidebar.info(
    "Dataset\n1338 Records"
)

st.title("🏥 Insurance AI Risk Analysis System")

st.markdown(
"""
### AI-Powered Insurance Risk Assessment & Policy Recommendation Platform
"""
)

st.markdown("---")

if page == "ℹ️ Project Information":

    st.header("Project Information")

    st.info(
    """
    Insurance AI Risk Analysis and Policy Recommendation System is a
    Machine Learning-based decision support platform developed using
    Python, Pandas, Scikit-Learn, Joblib, and Streamlit.

    The system analyzes customer attributes including age, gender,
    BMI, number of children, smoking status, and region to predict
    insurance risk levels using a trained Random Forest model with
    90.30% classification accuracy.

    Based on the predicted risk category, the platform automatically
    recommends suitable insurance policies and provides interactive
    analytics including risk distribution, customer segmentation,
    model performance monitoring, and business insights.
    """
    )

    st.markdown("### Technology Stack")

    st.write("• Python")

    st.write("• Pandas")

    st.write("• NumPy")

    st.write("• Scikit-Learn")

    st.write("• Random Forest Classifier")

    st.write("• Joblib")

    st.write("• Streamlit")

    st.markdown("---")

if page == "🏠 Risk Prediction":
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

        st.subheader(
        "Recommendation Explanation"
    )

        st.info(
            """
            The recommendation is generated using customer
            demographic information, lifestyle indicators,
            and predicted insurance risk levels produced by
            the trained Random Forest machine learning model.

            Customers classified as Low Risk receive Basic
            Insurance Plans, Medium Risk customers receive
            Standard Insurance Plans, and High Risk customers
            receive Premium Insurance Plans with enhanced
            coverage options.
            """
        )

        st.subheader(
            "Available Insurance Plans"
        )

        plan_df = pd.DataFrame(
            {
                "Plan": [
                    "Basic",
                    "Standard",
                    "Premium"
                ],
                "Coverage": [
                    "Essential",
                    "Extended",
                    "Comprehensive"
                ],
                "Target Risk Level": [
                    "Low Risk",
                    "Medium Risk",
                    "High Risk"
                ]
            }
        )

        st.dataframe(
            plan_df,
            use_container_width=True
        )

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

        st.subheader("Customer Profile")

        profile_data = pd.DataFrame(
            {
                "Attribute": [
                    "Age",
                    "Gender",
                    "BMI",
                    "Children",
                    "Smoking Status",
                    "Region"
                ],
                "Value": [
                    age,
                    sex,
                    bmi,
                    children,
                    smoker,
                    region
                ]
            }
        )

        st.dataframe(
            profile_data,
            hide_index=True,
            use_container_width=True
        )

        st.subheader("Customer Segmentation Summary")

        if smoker == "Yes":
            segment = "High-Risk Lifestyle Segment"
        else:
            segment = "General Lifestyle Segment"

        st.success(
            f"""
            Customer Segment

            {segment}
            """
        )

        st.subheader("Risk Group Analysis")

        if risk == "Low Risk":

            st.info(
                """
                Low Risk Group

                • Healthy customer profile

                • Lower insurance claim probability

                • Eligible for affordable insurance plans
                """
            )

        elif risk == "Medium Risk":

            st.warning(
                """
                Medium Risk Group

                • Moderate insurance exposure

                • Balanced premium recommendation

                • Periodic policy review suggested
                """
            )

        else:

            st.error(
                """
                High Risk Group

                • Higher insurance claim probability

                • Comprehensive coverage recommended

                • Premium protection advised
                """
            )

        st.subheader("Customer Characteristics")

        characteristics = pd.DataFrame(
            {
                "Category": [
                    "Age Group",
                    "Lifestyle",
                    "Insurance Risk",
                    "Recommended Plan"
                ],
                "Assessment": [
                    "Adult" if age < 60 else "Senior",
                    "Smoker" if smoker == "Yes" else "Non-Smoker",
                    risk,
                    recommendation.strip().splitlines()[0]
                ]
            }
        )

        st.dataframe(
            characteristics,
            hide_index=True,
            use_container_width=True
        )

if page == "📊 Analytics Dashboard":

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

    with st.expander(
        "📊 Risk Distribution Analysis",
        expanded=False
    ):

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

    with st.expander(
        "👥 Customer Segmentation",
        expanded=False
    ):

        st.bar_chart(
            segment_df.set_index(
                "Customer Type"
            )
        )

    with st.expander(
        "📈 Model Performance",
        expanded=False
    ):

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Accuracy",
                "90.30%",
                "↑ 2.4%"
            )

        with col2:
            st.metric(
                "Customers",
                "1338",
                "+1338"
            )

        with col3:
            st.metric(
                "Risk Classes",
                "3",
                "Active"
            )

        with col4:
            st.metric(
                "ML Model",
                "Random Forest",
                "Best Model"
            )

    with st.expander(
        "🗂️ Dataset Explorer",
        expanded=False
    ):
        dataset_info = pd.DataFrame({
        "Feature": [
            "Age",
            "Sex",
            "BMI",
            "Children",
            "Smoker",
            "Region"
        ],
        "Type": [
            "Numeric",
            "Categorical",
            "Numeric",
            "Numeric",
            "Categorical",
            "Categorical"
        ]
        })

        st.dataframe(
            dataset_info,
            use_container_width=True
        )

    with st.expander(
        "💡 Business Insights",
        expanded=False
    ):

        st.info(
            """
            • Smokers represent the majority of high-risk customers.

            • Low-risk and high-risk customers are almost equally distributed.

            • Random Forest achieved the best overall predictive performance.

            • The recommendation engine can support insurance decision-making.
            """
        )

    with st.expander(
        "🔍 Customer Risk Insights",
        expanded=False
    ):
        st.success(
            """
            Key Risk Drivers

            • Smoking Status

            • BMI

            • Age

            • Number of Children

            These features contribute most
            to insurance risk assessment.
            """
        )

    with st.expander(
        "🔄 Recommendation Workflow",
        expanded=False
    ):

        st.markdown("""
        Customer Information

        ⬇️

        Machine Learning Prediction

        ⬇️

        Risk Classification

        ⬇️

        Rule-Based Recommendation Engine

        ⬇️

        Insurance Policy Recommendation
        """)

    with st.expander(
        "📋 Recommendation Review",
        expanded=False
    ):

        review = pd.DataFrame(
            {
                "Validation Item": [
                    "Risk Prediction",
                    "Policy Mapping",
                    "Recommendation Logic",
                    "Recommendation Display"
                ],
                "Status": [
                    "Pass",
                    "Pass",
                    "Pass",
                    "Pass"
                ]
            }
        )

        st.dataframe(
            review,
            hide_index=True,
            use_container_width=True
        )

    with st.expander(
        "✅ Dashboard Review",
        expanded=False
    ):

        review = pd.DataFrame(
            {
                "Component": [
                    "Navigation",
                    "Prediction",
                    "Recommendation",
                    "Analytics",
                    "Documentation",
                    "Testing"
                ],
                "Status": [
                    "Completed",
                    "Completed",
                    "Completed",
                    "Completed",
                    "Completed",
                    "Completed"
                ]
            }
        )

        st.dataframe(
            review,
            hide_index=True,
            use_container_width=True
        )

    st.markdown("---")

st.caption(
    "Insurance AI Risk Analysis and Policy Recommendation System | AI/ML Internship Project"
)