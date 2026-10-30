# Credit Scoring API

**Resumo do Projeto:** 
este projeto implementa uma API RESTful para disponibilizar um modelo preditivo de Machine Learning de análise de risco de crédito. O sistema recebe dados financeiros básicos de um cliente e retorna a probabilidade dele se tornar inadimplente, auxiliando na tomada de decisão automatizada de concessão de crédito.

**Origem do Modelo:** 
opção B (Pipeline próprio). O modelo foi desenvolvido do zero para este projeto, simulando uma base de dados sintética de clientes (renda, dívida e idade) para treinar um pipeline de `RandomForestClassifier` com `StandardScaler`. Métricas alcançadas no conjunto de teste: Acurácia ~98%, F1-Score ~97%, ROC-AUC ~99%.

## 🛠️ Tecnologias Utilizadas

- **Python 3.14** (Ambiente Virtual `venv`)
- **FastAPI** (Framework web ASGI)
- **Uvicorn** (Servidor de aplicação)
- **Pydantic** (Validação estrita de dados)
- **Scikit-Learn** (Treinamento do modelo de ML)
- **Pandas & NumPy** (Manipulação de dados)
- **Joblib** (Serialização do modelo)

## ⚙️ Como Executar o Projeto

siga os passos abaixo para recriar o ambiente e rodar a API na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/hugocileiro/credit-scoring-api.git
   cd credit-scoring-api
