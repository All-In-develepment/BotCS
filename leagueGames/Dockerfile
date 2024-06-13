# Use a imagem base do Python
FROM python:3.12-alpine

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instalar dependências do sistema
RUN apk update && \
    apk add --no-cache tzdata

ENV TZ=America/Sao_Paulo
# Instalando as dependências da aplicação
RUN pip install -r requirements.txt

# Copiando todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

# EXPOSE 8000

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["python", "-u", "index.py"]