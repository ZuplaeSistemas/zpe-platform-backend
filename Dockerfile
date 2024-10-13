# Usando uma imagem base oficial do Python
FROM python:3.12-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos de dependências
COPY pyproject.toml poetry.lock /app/

# Instalando o Poetry
RUN pip install poetry

# Instalando as dependências de produção
RUN poetry install --no-root --without dev

# Copiar o arquivo .env
COPY .env /app/

# Copiando o restante do código para o diretório de trabalho
COPY . /app/

# Expondo a porta
EXPOSE 8000

# Comando de execução
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
