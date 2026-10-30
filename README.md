# Credit Scoring API

API de inferência de credit scoring com FastAPI, pipeline scikit-learn
serializado e carregado na RAM via lifespan.

## Estrutura

- src/train.py - treina e serializa o modelo em artifacts/model.pkl
- src/schemas.py - validação estrita com Pydantic v2
- src/service.py - camada de serviço desacoplada
- src/main.py - app FastAPI com /health e /predict

## Como rodar

    pip install -r requirements.txt
    python -m src.train
    uvicorn src.main:app --reload

## Endpoints

- GET /health - status do serviço e do modelo
- POST /predict - probabilidade de inadimplência
