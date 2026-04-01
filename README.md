# Projeto Turismo Flask

API de turismo desenvolvida com foco em gerenciamento de destinos, hotéis, reservas e passeios.

🚀 Tecnologias Utilizadas
Flask
PostgreSQL
Docker
Pydantic
Alembic (migrations)

⚙️ Como rodar o projeto
1. Clonar o repositório
git clone <url-do-repositorio>
cd projeto-turismo-flask
2. Acessar a pasta do backend
cd backend
3. Subir os containers com Docker
docker compose up -d
4. Instalar as dependências
uv sync
5. Rodar as migrations
uv run alembic upgrade head
6. Iniciar a aplicação
uv run flask --app src/app run

📄 Documentação da API

A documentação interativa (Swagger) estará disponível em:

👉 http://localhost:5000/apidocs