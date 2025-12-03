from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Ames House Price Prediction API")

# Load trained model
model = joblib.load("model.pkl")

# Input schema with 10 features
class HouseFeatures(BaseModel):
    LotArea: float
    OverallQual: int
    OverallCond: int
    YearBuilt: int
    YearRemodAdd: int
    MasVnrArea: float
    BsmtFinSF1: float
    TotalBsmtSF: float
    GrLivArea: float
    GarageCars: int

# Home route
@app.get("/")
def home():
    return {"message": "Ames Housing API is working!"}

# Predict route
@app.post("/predict")
def predict(features: HouseFeatures):
    data = features.model_dump()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"prediction": float(prediction)}

