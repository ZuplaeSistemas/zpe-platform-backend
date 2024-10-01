# Usar a imagem base do Python 3.12
FROM python:3.12-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o pyproject.toml e poetry.lock
COPY pyproject.toml poetry.lock /app/

# Instalar as dependências com Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

# Copiar o restante do código
COPY . /app

# Expor a porta para a aplicação
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
