import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from .config import DATA_PATH, MODEL_PATH

def train_model():
    print("🧠 Training model...")
    df = pd.read_csv(DATA_PATH)
    df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
    
    features = ["Open", "High", "Low", "Close", "Volume", "SMA_10", "SMA_50", "RSI"]
    df = df.dropna()
    
    X = df[features]
    y = df["Target"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    
    print(f"✅ Model trained with accuracy: {acc:.2f}")

    # ✅ Auto-create models folder if missing
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    
    joblib.dump(model, MODEL_PATH)
    print(f"💾 Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
