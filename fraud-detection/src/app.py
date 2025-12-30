from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
import json
from typing import List, Dict, Any

# Initialize FastAPI
app = FastAPI(
    title="Fraud Detection API",
    description="API for detecting fraudulent transactions",
    version="1.0.0"
)
# Load the model
MODEL_DIR = Path("models")
model_path = MODEL_DIR / "fraud_detection_xgboost_20251230_163756.pkl"
metadata_path = MODEL_DIR / "model_metadata_20251230_163756.json"

# To this:
MODEL_DIR = Path(r"C:\Users\My Device\Desktop\Week-5_KAIM\fraud-detection\models")
model_path = MODEL_DIR / "fraud_detection_xgboost_20251230_163756.pkl"
metadata_path = MODEL_DIR / "model_metadata_20251230_163756.json"
try:
    model = joblib.load(model_path)
    with open(metadata_path) as f:
        metadata = json.load(f)
    print("✅ Model and metadata loaded successfully")
except Exception as e:
    print(f"❌ Error loading model: {str(e)}")
    raise

# Define request/response models
class Transaction(BaseModel):
    features: List[float]
    
class PredictionResult(BaseModel):
    is_fraud: bool
    fraud_probability: float
    threshold: float

# Health check endpoint
@app.get("/")
def read_root():
    return {
        "status": "healthy",
        "model": "XGBoost Classifier",
        "version": "1.0.0"
    }

# Single prediction endpoint
@app.post("/predict", response_model=PredictionResult)
def predict(transaction: Transaction):
    try:
        # Convert to 2D array
        features = np.array(transaction.features).reshape(1, -1)
        
        # Get prediction probabilities
        proba = model.predict_proba(features)[0]
        fraud_prob = proba[1]  # Probability of class 1 (fraud)
        
        # Get threshold from metadata
        threshold = metadata.get('threshold_95_precision', 0.5)
        
        return {
            "is_fraud": bool(fraud_prob >= threshold),
            "fraud_probability": float(fraud_prob),
            "threshold": float(threshold)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Batch prediction endpoint
@app.post("/predict_batch")
def predict_batch(transactions: List[Transaction]):
    try:
        # Convert to 2D array
        features = np.array([t.features for t in transactions])
        
        # Get prediction probabilities
        probas = model.predict_proba(features)
        fraud_probs = probas[:, 1]  # Probabilities of class 1 (fraud)
        
        # Get threshold from metadata
        threshold = metadata.get('threshold_95_precision', 0.5)
        
        # Prepare results
        results = []
        for i, prob in enumerate(fraud_probs):
            results.append({
                "transaction_id": i,
                "is_fraud": bool(prob >= threshold),
                "fraud_probability": float(prob),
                "threshold": float(threshold)
            })
        
        return {"predictions": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Model info endpoint
@app.get("/model_info")
def get_model_info():
    return {
        "model_type": "XGBoost",
        "training_date": metadata.get("training_date"),
        "features": metadata.get("features"),
        "metrics": metadata.get("test_metrics", {})
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)