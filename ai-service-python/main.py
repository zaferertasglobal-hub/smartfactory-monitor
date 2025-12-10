from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.ensemble import IsolationForest
import pandas as pd

app = FastAPI(title="SmartFactory AI Anomaly Detection", version="1.0")

# Modeli bir kere eğit
data = pd.DataFrame({
    "temperature": np.random.normal(50, 10, 1000),
    "vibration": np.random.normal(5, 1, 1000),
    "pressure": np.random.normal(100, 15, 1000)
})
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(data)

class SensorData(BaseModel):
    temperature: float
    vibration: float
    pressure: float

@app.get("/api/ai/health")
def health():
    return {"status": "UP", "service": "AI Anomaly Detection", "model": "IsolationForest"}

@app.post("/api/ai/predict")
def predict(data: SensorData):
    X = np.array([[data.temperature, data.vibration, data.pressure]])
    prediction = model.predict(X)[0]
    score = model.decision_function(X)[0]
    
    return {
        "anomaly": prediction == -1,
        "score": float(score),
        "message": "MACHINE FAILURE RISK!" if prediction == -1 else "Normal operation"
    }

@app.get("/")
def root():
    return {"message": "SmartFactory AI Service Running!"}