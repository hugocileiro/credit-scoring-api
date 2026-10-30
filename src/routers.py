"""Roteadores da API."""
from fastapi import APIRouter, HTTPException
from src.schemas import CreditFeatures, PredictionResponse

router = APIRouter()
_state: dict = {}

@router.get("/health")
def health():
    return {"status": "ok", "model_loaded": "predictor" in _state}

@router.post("/predict", response_model=PredictionResponse)
def predict(payload: CreditFeatures):
    predictor = _state.get("predictor")
    if predictor is None:
        raise HTTPException(status_code=503, detail="Modelo não carregado")
    try:
        result = predictor.predict(payload)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Erro na predição: {exc}")
    return PredictionResponse(**result)