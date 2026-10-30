💳 Credit Scoring API

<p align="center">
**API RESTful para análise e previsão de risco de crédito utilizando Machine Learning.**
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn&logoColor=white" />
<img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow" />
</p>

📌 Sobre o Projeto

O Credit Scoring API é um projeto que implementa uma API RESTful para disponibilizar um modelo preditivo de Machine Learning voltado à análise de risco de crédito.

O sistema recebe informações financeiras básicas de um cliente, como renda, dívida e idade, e retorna a probabilidade de inadimplência.

O objetivo é demonstrar como modelos de Machine Learning podem ser integrados a aplicações backend, permitindo automatizar parte do processo de avaliação de risco e auxiliar na tomada de decisão para concessão de crédito.

🧠 Desenvolvimento do Modelo

O modelo foi desenvolvido do zero para este projeto, utilizando uma abordagem de pipeline próprio (Opção B).

Para o treinamento, foi criada uma base de dados sintética simulando informações financeiras e demográficas de clientes.

Pipeline de Machine Learning

O processo de desenvolvimento utiliza:

Geração de dados: criação de uma base sintética contendo renda, dívida e idade.
Pré-processamento: normalização dos dados utilizando StandardScaler.
Treinamento: utilização do algoritmo RandomForestClassifier.
Avaliação: análise do desempenho por meio de métricas de classificação.
Serialização: armazenamento do modelo treinado utilizando Joblib.
📊 Métricas de Desempenho

Resultados informados para o conjunto de teste:

Métrica	Resultado
Acurácia (Accuracy)	~98%
F1-Score	~97%
ROC-AUC	~99%
Observação: os resultados foram obtidos com dados sintéticos e representam o desempenho no conjunto de teste utilizado. Eles não garantem a mesma performance em dados reais.
🛠️ Tecnologias Utilizadas
Tecnologia	Finalidade
Python 3.14	Linguagem de programação
FastAPI	Desenvolvimento da API REST
Uvicorn	Servidor ASGI
Pydantic	Validação dos dados de entrada
Scikit-Learn	Treinamento e implementação do modelo
Pandas	Manipulação de dados
NumPy	Operações numéricas
Joblib	Serialização do modelo
StandardScaler	Normalização dos dados
RandomForestClassifier	Algoritmo de classificação
📂 Estrutura do Projeto
text
credit-scoring-api/
│
├── artifacts/
│   └── model.pkl
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── train.py
│
├── .venv/
│
├── requirements.txt
├── README.md
└── .gitignore

A estrutura acima representa a organização esperada com base nos arquivos e caminhos informados. Ajuste os nomes caso sua estrutura real seja diferente.
⚙️ Como Executar o Projeto

Siga o passo a passo para configurar o ambiente e executar a API localmente.

1. Clone o repositório
bash
git clone https://github.com/hugocileiro/credit-scoring-api.git

cd credit-scoring-api

2. Crie e ative o ambiente virtual

O ambiente virtual permite isolar as dependências do projeto.

Windows (PowerShell):

powershell
python -m venv .venv

.\.venv\Scripts\Activate.ps1


Linux / macOS:

bash
python3 -m venv .venv

source .venv/bin/activate

3. Instale as dependências

Com o ambiente virtual ativado, execute:

bash
pip install -r requirements.txt

4. Treine o modelo de Machine Learning

Execute o comando:

bash
python -m src.train


Esse processo será responsável por:

Gerar a base de dados sintética.
Treinar o modelo de classificação.
Avaliar o desempenho utilizando métricas.
Serializar o modelo treinado.
Gerar o arquivo model.pkl dentro da pasta artifacts/.
5. Inicie a API

Após o treinamento do modelo, inicie o servidor FastAPI:

bash
uvicorn src.main:app --reload


Se tudo estiver configurado corretamente, a API estará disponível em:

🌐 http://127.0.0.1:8000

📖 Documentação da API

O FastAPI disponibiliza documentação interativa para facilitar a visualização e os testes dos endpoints.

Documentação	Endereço
Swagger UI	http://127.0.0.1:8000/docs
ReDoc	http://127.0.0.1:8000/redoc

Através dessas interfaces, é possível visualizar os endpoints disponíveis, consultar os parâmetros esperados e realizar requisições diretamente pelo navegador.

🎯 Objetivos do Projeto

Este projeto foi desenvolvido com o objetivo de aplicar e demonstrar conhecimentos em:

Desenvolvimento de APIs RESTful com FastAPI.
Integração de modelos de Machine Learning com aplicações backend.
Construção de pipelines de treinamento e pré-processamento.
Validação de dados com Pydantic.
Avaliação de modelos de classificação.
Serialização e carregamento de modelos treinados.
Organização e estruturação de projetos Python.
👨‍💻 Autor

Hugo Cileiro

GitHub: @hugocileiro

Repositório: Credit Scoring API

<p align="center">
Desenvolvido com 🐍 Python e 🤖 Machine Learning.
</p>