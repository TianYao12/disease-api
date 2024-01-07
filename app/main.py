from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    symptoms: List[int]


class PredictionOut(BaseModel):
    disease: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    disease = predict_pipeline(payload.symptoms)
    return {"disease": disease}
