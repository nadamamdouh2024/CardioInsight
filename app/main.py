from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from src.model import load_model, predict, predict_probability
from src.preprocessing import preprocess_input

app = FastAPI(
    title="CardioInsight API",
    description="Heart Disease Prediction API",
    version="1.0.0"
)

bundle = load_model()

class PatientData(BaseModel):
    Age: float
    Weight: float
    Height: float
    Physical_Activity: str
    Diet: str
    Stress_Level: str
    Hypertension: int
    Diabetes: int
    Hyperlipidemia: int
    Family_History: int
    Previous_Heart_Attack: int
    Systolic_BP: int
    Diastolic_BP: int
    Heart_Rate: int
    Blood_Sugar_Fasting: int
    Cholesterol_Total: int
    Gender: str
    Smoking: str
    Alcohol_Intake: str

@app.post("/predict")
def predict_heart_disease(patient: PatientData):
    data = pd.DataFrame([patient.model_dump()])
    data["BMI"] = (
        data["Weight"] / ((data["Height"] / 100) ** 2)
    ).round(1)
    data["Pulse_Pressure"] = (
        data["Systolic_BP"] - data["Diastolic_BP"]
    )
    processed_data = preprocess_input(
        data,
        bundle["ordinal_encoder"],
        bundle["scaler"],
        bundle["columns"]
    )
    prediction = predict(bundle, processed_data)
    probability = predict_probability(bundle, processed_data)

    return {
        "prediction": int(prediction[0]),
        "probability": float(probability[0][1])
    }

