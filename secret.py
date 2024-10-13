import secrets

# Gera uma chave de 32 caracteres aleatórios
fixed_token = secrets.token_urlsafe(32)

print(fixed_token)
