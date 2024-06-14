import pandas as pd
from pymongo import MongoClient
import requests
import os
from dotenv import load_dotenv
import hashlib

def get_data_from_csv(url):
    response = requests.get(url)
    open('/tmp/diferencas.csv', 'wb').write(response.content)
    df = pd.read_csv('/tmp/diferencas.csv')
    return df

def compute_hash(row):
    # Substitua com os nomes das colunas relevantes para o hash
    relevant_data = row[['gameid', 'league', 'date', 'playername', 'playerid', 'teamname', 'teamid', 'champion','gamelength', 'ckpm', 'dpm']]
    hash_str = ''.join(relevant_data.astype(str).values)
    return hashlib.md5(hash_str.encode()).hexdigest()

def update_database():
    # Carregar dotenv
    env_path = os.path.join(os.path.dirname(os.path.dirname('index.py')), '.env')
    load_dotenv(dotenv_path=env_path)

    # Carregar variaveis
    mongo_uri = os.getenv('MONGO_URI')
    mongo_name = os.getenv('MONGO_NAME')
    mongo_collection = os.getenv('MONGO_COLLECTION')

    # Conectar ao MongoDB
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=20000)
    db = client[mongo_name]
    collection = db[mongo_collection]

    # URL do Google Drive para download direto
    file_id = '1IjIEhLc9n8eLKeY-yh_YigKVWbhgGBsN'
    download_url = f'https://drive.google.com/uc?export=download&id={file_id}'

    # Carregar o CSV em um DataFrame pandas
    df = get_data_from_csv(download_url)

    # Adicionar uma coluna de hash para identificar registros únicos
    df['hash'] = df.apply(compute_hash, axis=1)

    # Identificar hashes já presentes no banco de dados
    existing_hashes = set(collection.distinct('hash'))

    # Filtrar novos registros
    new_records = df[~df['hash'].isin(existing_hashes)]

    # Converter o DataFrame filtrado em uma lista de dicionários
    data = new_records.to_dict(orient='records')

    # Inserir novos registros na coleção MongoDB
    if data:
        collection.insert_many(data)
        print(f'Inseridos {len(data)} novos registros na tabela {collection.name} do banco de dados {db.name}.')
    else:
        print('Nenhum novo registro para inserir.')

    client.close()

if __name__ == "__main__":
    update_database()