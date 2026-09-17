import pandas as pd

NUM_COLS = [
    'Age',
    'Weight',
    'Height',
    'BMI',
    'Systolic_BP',
    'Diastolic_BP',
    'Pulse_Pressure',
    'Heart_Rate',
    'Blood_Sugar_Fasting',
    'Cholesterol_Total'
]

ORD_COLS = [
    'Diet',
    'Stress_Level',
    'Physical_Activity'
]

NOM_COLS = [
    'Gender',
    'Smoking',
    'Alcohol_Intake'
]

def preprocess_input(df, ordinal_encoder, scaler, columns):
    df = df.copy()
    df[ORD_COLS] = ordinal_encoder.transform(df[ORD_COLS])
    df = pd.get_dummies(df, columns=NOM_COLS, drop_first=True)
    df = df.reindex(columns=columns, fill_value=0)
    df[NUM_COLS] = scaler.transform(df[NUM_COLS])
    return df