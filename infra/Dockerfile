# Use uma imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY ../app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho
COPY ../app/ .

# Defina a variável de ambiente para a porta
ENV PORT=5000

# Exponha a porta que o Flask usará
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "program.py"]
