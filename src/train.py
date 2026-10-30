"""Pipeline de treinamento e serialização do modelo."""
from pathlib import Path
import joblib
import numpy as np
import pandas as pd

from src.model import build_model

ARTIFACTS_DIR = Path(__file__).resolve().parent.parent / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "model.pkl"


def _synthetic_data(n: int = 1000, seed: int = 42):
    rng = np.random.default_rng(seed)
    renda = rng.normal(5000, 2000, n).clip(500, 20000)
    divida = rng.normal(1500, 800, n).clip(0, 10000)
    idade = rng.integers(18, 75, n)
    y = ((divida / renda) > 0.4).astype(int)
    X = pd.DataFrame({"renda": renda, "divida": divida, "idade": idade})
    return X, y


def train_and_save() -> Path:
    X, y = _synthetic_data()
    pipeline = build_model()
    pipeline.fit(X, y)
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Modelo treinado e salvo em {MODEL_PATH}")
    return MODEL_PATH


if __name__ == "__main__":
    train_and_save()
