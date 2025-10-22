import joblib
import pandas as pd
from .config import MODEL_PATH

def predict_next(df):
    model = joblib.load(MODEL_PATH)
    latest = df.iloc[-1:].drop("Target", axis=1, errors="ignore")
    pred = model.predict(latest)[0]
    movement = "UP 📈" if pred == 1 else "DOWN 📉"
    print(f"Predicted next move: {movement}")
    return movement
