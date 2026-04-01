# Projeto Turismo Flask

API de turismo desenvolvida com foco em gerenciamento de destinos, hotéis, reservas e passeios.

🚀 Tecnologias Utilizadas
- Flask
- Flasgger
- PostgreSQL
- Docker
- Pydantic
- Alembic (migrations)

## Repositório
https://github.com/AnandaMazine/projeto-turismo-flask

## Como rodar o projeto
1. Clone o repositório:

git clone https://github.com/AnandaMazine/projeto-turismo-flask.git
cd projeto-turismo-flask

2. Suba o banco de dados com Docker:
docker compose up -d

3. Acesse o backend:
cd apps/backend

4. Instale/atualize as dependências:
uv sync

5. Execute as migrations:
uv run alembic upgrade head

6. Inicie a aplicação Flask:
uv run flask --app src.app run


## Variáveis de ambiente
O backend carrega as configurações do arquivo `apps/backend/.env`.
Por padrão ele usa:
DATABASE_URL=postgresql://devuser:devpassword@localhost:5433/turismo_db

## Documentação da API
A documentação interativa (Swagger) estará disponível em:

👉 http://localhost:5000/apidocs