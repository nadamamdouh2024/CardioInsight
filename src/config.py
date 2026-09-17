from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "Data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = BASE_DIR / "models"

RAW_DATA_PATH = RAW_DATA_DIR / "synthetic_heart_disease_dataset.csv"
PROCESSED_DATA_PATH = PROCESSED_DATA_DIR / "synthetic_heart_disease_cleaned.csv"

MODEL_PATH = MODELS_DIR / "best_model.pkl"