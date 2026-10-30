# Credit Scoring API

**Resumo do Projeto:** 
Este projeto implementa uma API RESTful para disponibilizar um modelo preditivo de Machine Learning de análise de risco de crédito. O sistema recebe dados financeiros básicos de um cliente e retorna a probabilidade dele se tornar inadimplente, auxiliando na tomada de decisão automatizada de concessão de crédito.

**Origem do Modelo:** 
Opção B (Pipeline próprio). O modelo foi desenvolvido do zero para este projeto, simulando uma base de dados sintética de clientes (renda, dívida e idade) para treinar um pipeline de `RandomForestClassifier` com `StandardScaler`. Métricas alcançadas no conjunto de teste: Acurácia ~98%, F1-Score ~97%, ROC-AUC ~99%.

## 🛠️ Tecnologias Utilizadas

- **Python 3.14** (Ambiente Virtual `venv`)
- **FastAPI** (Framework web ASGI)
- **Uvicorn** (Servidor de aplicação)
- **Pydantic** (Validação estrita de dados)
- **Scikit-Learn** (Treinamento do modelo de ML)
- **Pandas & NumPy** (Manipulação de dados)
- **Joblib** (Serialização do modelo)

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente e executar a API de Credit Scoring localmente.

1. Clone o repositório

Abra o terminal e execute:

bash
git clone https://github.com/hugocileiro/credit-scoring-api.git
cd credit-scoring-api

2. Crie e ative o ambiente virtual

Crie um ambiente virtual para isolar as dependências do projeto.

Windows (PowerShell):

powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1


Linux / macOS:

bash
python3 -m venv .venv
source .venv/bin/activate

3. Instale as dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias:

bash
pip install -r requirements.txt

4. Treine e serialize o modelo (Fase 1)

Execute o comando abaixo para iniciar o treinamento do modelo de Machine Learning:

bash
python -m src.train


Esse processo irá:

Treinar o modelo de Credit Scoring.
Exibir as métricas de desempenho no terminal.
Serializar o modelo treinado.
Gerar o arquivo model.pkl dentro da pasta artifacts/.
5. Inicie o servidor da API

Após o treinamento do modelo, execute:

bash
uvicorn src.main:app --reload


A API estará disponível localmente no endereço:

http://127.0.0.1:8000

Documentação interativa

O FastAPI disponibiliza uma documentação interativa que permite testar os endpoints diretamente pelo navegador.

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc


Pronto! Com essas etapas, o ambiente estará configurado, o modelo treinado e a API em execução localmente.