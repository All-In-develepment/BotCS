import pandas as pd
from pymongo import MongoClient
import requests
import os
from dotenv import load_dotenv
import hashlib

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

  # Baixar o CSV diretamente do link
  response = requests.get(download_url)
  open('/tmp/league_games.csv', 'wb').write(response.content)

  # Carregar o CSV em um DataFrame pandas
  df = pd.read_csv('/tmp/league_games.csv', index_col=0)

  # Adicionar uma coluna de hash para identificar registros únicos
  df['hash'] = df.apply(lambda row: hashlib.md5(str(row.values).encode()).hexdigest(), axis=1)

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