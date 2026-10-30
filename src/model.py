"""Definição do modelo de credit scoring (pipeline sklearn)."""
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


def build_model() -> Pipeline:
    """Retorna um pipeline padronizado: scaler + random forest."""
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "clf",
                RandomForestClassifier(
                    n_estimators=200,
                    max_depth=6,
                    random_state=42,
                ),
            ),
        ]
    )
