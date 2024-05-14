# Use a imagem base do Python
FROM python:3.12-bookworm

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Definir a variável TERM
ENV TERM=xterm

# Copiando todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]
