# Usar uma imagem base oficial do Python
FROM python:3.12-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo de requisitos e instalar as dependências
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry && poetry install --no-dev

# Copiar o restante do código
COPY . .

# Expor a porta 80
EXPOSE 80

# Comando para rodar a aplicação
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
