# Usar a imagem oficial do Python
FROM python:3.12-slim

# Configurar diretório de trabalho
WORKDIR /app

# Instalar Poetry
RUN pip install poetry

# Copiar os arquivos do projeto
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

# Copiar o restante do código
COPY . .

# Comando para rodar a aplicação
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
