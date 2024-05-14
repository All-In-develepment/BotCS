# Use a imagem base do Python
FROM python:3.12-bookworm

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

EXPOSE 8000

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]
