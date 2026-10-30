"""Camada de serviço: desacopla a predição do framework web."""
from pathlib import Path
import joblib
import pandas as pd

from src.schemas import CreditFeatures


class PredictorService:
    def __init__(self, model_path: Path):
        self._model = joblib.load(model_path)

    def predict(self, features: CreditFeatures) -> dict:
        df = pd.DataFrame([features.model_dump()])
        prob = float(self._model.predict_proba(df)[0, 1])
        return {"default_probability": prob, "is_default": prob >= 0.5}
