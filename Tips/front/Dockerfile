# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update

RUN apt-get install -y \
    build-essential curl software-properties-common \
    git \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Sao_Paulo

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/front

EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD ["streamlit", "run", "index.py", "--server.port=8501", "--server.address=0.0.0.0"]