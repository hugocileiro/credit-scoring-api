"""API FastAPI com lifespan para carregar o modelo na RAM."""
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException

from src.schemas import CreditFeatures, PredictionResponse
from src.service import PredictorService

MODEL_PATH = Path(__file__).resolve().parent.parent / "artifacts" / "model.pkl"
_state: dict = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not MODEL_PATH.exists():
        raise RuntimeError(f"Modelo não encontrado em {MODEL_PATH}")
    _state["predictor"] = PredictorService(MODEL_PATH)
    yield
    _state.clear()


app = FastAPI(title="Credit Scoring API", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": "predictor" in _state}


@app.post("/predict", response_model=PredictionResponse)
def predict(payload: CreditFeatures):
    predictor = _state.get("predictor")
    if predictor is None:
        raise HTTPException(status_code=503, detail="Modelo não carregado")
    try:
        result = predictor.predict(payload)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Erro na predição: {exc}")
    return PredictionResponse(**result)

# rotas: /health e /predict implementadas com tratamento de erros
