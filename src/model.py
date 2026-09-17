import joblib
from src.config import MODEL_PATH

def load_model():
    bundle = joblib.load(MODEL_PATH)
    return bundle

def predict(bundle, data):
    model = bundle['model']
    return model.predict(data)

def predict_probability(bundle, data):
    model = bundle['model']
    return model.predict_proba(data)