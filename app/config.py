import os

from dotenv import load_dotenv

# Carregar o arquivo .env
load_dotenv()

# Carregar o token do .env
FIXED_TOKEN = os.getenv("FIXED_TOKEN")
