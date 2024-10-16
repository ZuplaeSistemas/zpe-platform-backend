import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context
from app.db.base_class import Base
from app.models import user  # Importe as models aqui

# Lendo as variáveis de ambiente para a URL do banco
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Construindo a URL do banco a partir das variáveis de ambiente
db_url = (
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}/{POSTGRES_DB}"
)

config = context.config

fileConfig(config.config_file_name)

# Metadados das models
target_metadata = Base.metadata


def run_migrations_offline():
    """Executa as migrações no modo offline."""
    context.configure(url=db_url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Executa as migrações no modo online, conectando ao banco de dados."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        url=db_url,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
