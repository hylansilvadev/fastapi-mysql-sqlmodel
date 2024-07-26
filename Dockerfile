# Use a imagem base do Python
FROM python:3.12-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie todos os arquivos para o diretório de trabalho
COPY . .

# Instale pipx e poetry, e crie um link simbólico para poetry
RUN apt-get update && apt-get install -y pipx && pipx ensurepath && pipx install poetry && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Instale as dependências usando poetry
RUN poetry install

# Exponha a porta que a aplicação irá rodar
EXPOSE 8000

# Comando para rodar a aplicação FastAPI e aplicar migrações
CMD ["sh", "-c", "poetry run alembic upgrade head && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000"]
