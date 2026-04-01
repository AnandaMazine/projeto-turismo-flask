import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# 1. CONFIGURAÇÃO DE CAMINHOS (PATH)
# Define a pasta raiz do backend (onde está o alembic.ini)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Adiciona a pasta 'src' ao sistema para o Python achar database.py e models.py
sys.path.insert(0, os.path.join(BASE_DIR, 'src'))

load_dotenv()

# 2. INICIALIZAÇÃO DO CONFIG
config = context.config

# 3. CONFIGURAÇÃO DE LOGS
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 4. IMPORTAÇÃO DOS SEUS MODELS (TURISMO)
try:
    import database
    import models
    # O MetaData avisa ao Alembic quais tabelas existem no seu código
    target_metadata = database.db.metadata
except ImportError as e:
    print(f"❌ Erro de importação no Alembic: {e}")
    print(f"DEBUG: Tentando buscar em: {os.path.join(BASE_DIR, 'src')}")
    target_metadata = None

# 5. CONFIGURAÇÃO DA URL DO BANCO
database_url = os.getenv('DATABASE_URL')
if database_url:
    # Correção automática para o driver do SQLAlchemy
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    config.set_main_option('sqlalchemy.url', database_url)

def run_migrations_offline() -> None:
    """Modo Offline: Gera o script SQL sem conectar ao banco."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Modo Online: Conecta ao banco e aplica as mudanças."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()