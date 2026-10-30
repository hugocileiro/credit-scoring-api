"""Schemas Pydantic com validação estrita."""
from pydantic import BaseModel, Field, ConfigDict


class CreditFeatures(BaseModel):
    model_config = ConfigDict(extra="forbid")

    renda: float = Field(..., gt=0, description="Renda mensal (R$)")
    divida: float = Field(..., ge=0, description="Dívida total (R$)")
    idade: int = Field(..., ge=18, le=120, description="Idade em anos")


class PredictionResponse(BaseModel):
    default_probability: float
    is_default: bool
    model_version: str = "1.0.0"
