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

## Pré-requisitos
- Docker
- Python 3.14+
- `uv` instalado (Hatch/UV environment manager)

## Como rodar o projeto
1. Clone o repositório:
   ```bash
git clone https://github.com/AnandaMazine/projeto-turismo-flask.git
cd projeto-turismo-flask
```
2. Suba o banco de dados com Docker:
   ```bash
docker compose up -d
```
3. Acesse o backend:
   ```bash
cd apps/backend
```
4. Instale/atualize as dependências:
   ```bash
uv sync
```
5. Execute as migrations:
   ```bash
uv run alembic upgrade head
```
6. Inicie a aplicação Flask:
   ```bash
uv run flask --app src.app run
```

## Variáveis de ambiente
O backend carrega as configurações do arquivo `apps/backend/.env`.
Por padrão ele usa:
```env
DATABASE_URL=postgresql://devuser:devpassword@localhost:5432/turismo_db
```

## Documentação da API
A documentação interativa (Swagger) estará disponível em:

👉 http://localhost:5000/apidocs

## Observações
- O endpoint Swagger só estará disponível enquanto a aplicação estiver em execução.
- Caso precise parar os containers Docker:
  ```bash
docker compose down
```
