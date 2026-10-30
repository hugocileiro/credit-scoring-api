"""API FastAPI com lifespan para carregar o modelo na RAM."""
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI

from src.service import PredictorService
from src.routers import router, _state

MODEL_PATH = Path(__file__).resolve().parent.parent / "artifacts" / "model.pkl"

@asynccontextmanager
async def lifespan(app: FastAPI):
    if not MODEL_PATH.exists():
        raise RuntimeError(f"Modelo não encontrado em {MODEL_PATH}")
    # Salva o predictor no dicionário de estado do roteador
    _state["predictor"] = PredictorService(MODEL_PATH)
    yield
    _state.clear()

app = FastAPI(title="Credit Scoring API", lifespan=lifespan)

# Inclui as rotas
app.include_router(router)
