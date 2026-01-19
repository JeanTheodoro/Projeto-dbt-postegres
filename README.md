# 📘 Projeto DBT + PostgreSQL + OpenWeather (Estudo)

Este projeto utiliza **dbt (data build tool)** para transformação de
dados, **PostgreSQL** como banco de dados (executado via Docker) e a
**API do OpenWeather** para recuperação de dados climáticos.

Os dados são coletados da OpenWeather API, armazenados no PostgreSQL e
transformados utilizando dbt.

------------------------------------------------------------------------

## 🌦 Fonte de Dados --- OpenWeather API

Este projeto consome dados da **OpenWeather API**, utilizando o endpoint
de **Current Weather Data**.

📄 **Documentação oficial da API**:\
https://openweathermap.org/current#parameter

------------------------------------------------------------------------

## 📁 Estrutura Completa do Projeto

    ├── README.md
    ├── docker-compose.yaml
    ├── logs
    │   └── dbt.log
    ├── poetry.lock
    ├── pyproject.toml
    ├── requirements.txt
    └── weather
        ├── README.md
        ├── analyses
        ├── dbt_internal_packages
        ├── dbt_project.yml
        ├── logs
        │   └── dbt.log
        ├── macros
        ├── models
        │   ├── marts
        │   ├── source
        │   └── staging
        ├── scripts
        │   ├── data_pipeline.py
        │   ├── http_request.py
        │   └── connection_database.py
        ├── seeds
        ├── snapshots
        ├── target
        └── tests

------------------------------------------------------------------------

## 🔧 Pré-requisitos

-   Docker
-   Docker Compose
-   Python 3.12.0
-   pip

------------------------------------------------------------------------

## 🧩 Configuração do `.env`

    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=weather
    POSTGRES_HOST=localhost

    OPENWEATHER_API_KEY=

------------------------------------------------------------------------

## 🐳 Subindo o PostgreSQL

    docker-compose up -d
    docker logs -f <container_id>

------------------------------------------------------------------------

## 📦 Dependências Python

Arquivo `requirements.txt`:

    dbt-core>=1.10.0,<2.0.0
    dbt-postgres>=1.10.0,<2.0.0
    psycopg2-binary>=2.9.9,<3.0.0
    requests>=2.32.0,<3.0.0
    python-dotenv>=1.0.0,<2.0.0

Instalação:
    
    python -m venv .venv

    source .venv/bin/activate

    pip install -r requirements.txt

------------------------------------------------------------------------

## ▶️ Executando o Pipeline

    python weather/scripts/data_pipeline.py
    

------------------------------------------------------------------------

## ▶️ Executando o DBT

    dbt run (criar as views)
    dbt test (executar teste)
    dbt docs serve --port 8081 (visualizar a documentação)
------------------------------------------------------------------------

## 🔄 Fluxo de Dados

1.  Python consome a OpenWeather API\
2.  Dados são persistidos no PostgreSQL\
3.  dbt realiza staging, deduplicação e marts\
4.  Dados analíticos prontos para consumo

------------------------------------------------------------------------

