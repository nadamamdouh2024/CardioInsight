import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="CardioInsight",
    page_icon="🫀",
    layout="wide"
)

st.title("🫀 CardioInsight")
st.write("Heart Disease Risk Assessment")
st.divider()

st.header("👤 Patient Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=1.0,
        max_value=120.0,
        value=50.0
    )

with col2:
    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=200.0,
        value=70.0
    )

with col3:
    height = st.number_input(
        "Height (cm)",
        min_value=50.0,
        max_value=250.0,
        value=170.0
    )

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col2:
    smoking = st.selectbox(
        "Smoking",
        ["Never", "Former", "Current"]
    )

st.divider()

st.header("🏥 Medical History")

col1, col2, col3 = st.columns(3)

with col1:
    hypertension = st.selectbox(
        "Hypertension",
        ["No", "Yes"]
    )

with col2:
    diabetes = st.selectbox(
        "Diabetes",
        ["No", "Yes"]
    )

with col3:
    hyperlipidemia = st.selectbox(
        "Hyperlipidemia",
        ["No", "Yes"]
    )

col1, col2 = st.columns(2)

with col1:
    family_history = st.selectbox(
        "Family History",
        ["No", "Yes"]
    )

with col2:
    previous_heart_attack = st.selectbox(
        "Previous Heart Attack",
        ["No", "Yes"]
    )

st.divider()

st.header("🩺 Clinical Measurements")

col1, col2, col3 = st.columns(3)

with col1:
    systolic_bp = st.number_input(
        "Systolic BP",
        min_value=50,
        max_value=250,
        value=120
    )

with col2:
    diastolic_bp = st.number_input(
        "Diastolic BP",
        min_value=30,
        max_value=150,
        value=80
    )

with col3:
    heart_rate = st.number_input(
        "Heart Rate",
        min_value=30,
        max_value=220,
        value=75
    )

col1, col2 = st.columns(2)

with col1:
    blood_sugar = st.number_input(
        "Fasting Blood Sugar",
        min_value=30,
        max_value=500,
        value=100
    )

with col2:
    cholesterol = st.number_input(
        "Total Cholesterol",
        min_value=50,
        max_value=500,
        value=200
    )

st.divider()

st.header("🍎 Lifestyle")

col1, col2, col3 = st.columns(3)

with col1:
    physical_activity = st.selectbox(
        "Physical Activity",
        ["Sedentary", "Moderate", "Active"]
    )

with col2:
    diet = st.selectbox(
        "Diet",
        ["Unhealthy", "Average", "Healthy"]
    )

with col3:
    stress_level = st.selectbox(
        "Stress Level",
        [ "Low", "Medium", "High"]
    )

alcohol = st.selectbox(
    "Alcohol Intake",
    ["None", "Low", "Moderate", "High"]
)

st.divider()

if st.button("🔍 Predict", use_container_width=True):
    if diastolic_bp >= systolic_bp:
        st.error("Diastolic BP must be lower than Systolic BP.")
    else:
        data = {
            "Age": age,
            "Weight": weight,
            "Height": height,
            "Physical_Activity": physical_activity,
            "Diet": diet,
            "Stress_Level": stress_level,
            "Hypertension": 1 if hypertension == "Yes" else 0,
            "Diabetes": 1 if diabetes == "Yes" else 0,
            "Hyperlipidemia": 1 if hyperlipidemia == "Yes" else 0,
            "Family_History": 1 if family_history == "Yes" else 0,
            "Previous_Heart_Attack": 1 if previous_heart_attack == "Yes" else 0,
            "Systolic_BP": systolic_bp,
            "Diastolic_BP": diastolic_bp,
            "Heart_Rate": heart_rate,
            "Blood_Sugar_Fasting": blood_sugar,
            "Cholesterol_Total": cholesterol,
            "Gender": gender,
            "Smoking": smoking,
            "Alcohol_Intake": alcohol
        }

        try:
            response = requests.post(
                API_URL,
                json=data,
                timeout=10
            )

            if response.status_code == 200:
                result = response.json()

                st.divider()
                st.header("📊 Prediction Result")

                if result["prediction"] == 1:
                    st.error("🔴 Predicted Class: Heart Disease")
                else:
                    st.success("🟢 Predicted Class: No Heart Disease")

                st.metric(
                    "Probability of Heart Disease",
                    f"{result['probability']:.2%}"
                )

                st.info(
                    "This is an AI model prediction and should not be considered a medical diagnosis."
                )
            else:
                st.error(f"API Error: {response.status_code}")

        except requests.exceptions.RequestException:
            st.error("Unable to connect to the prediction API. Please make sure FastAPI is running.")