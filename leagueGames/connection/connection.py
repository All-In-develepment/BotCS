from flask import Flask, request, jsonify
from bson.json_util import dumps
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# Configuração do MongoDB
# Carregar dotenv
env_path = os.path.join(os.path.dirname(os.path.dirname('index.py')), '.env')
print(os.path.join(os.path.dirname(os.path.dirname('index.py'))))
load_dotenv(dotenv_path=env_path)

# Carregar variaveis
mongo_uri = os.getenv('MONGO_URI')
print(mongo_uri)
mongo_name = os.getenv('MONGO_NAME')
mongo_collection = os.getenv('MONGO_COLLECTION')

# Conectar ao MongoDB
client = MongoClient(mongo_uri, serverSelectionTimeoutMS=20000)
db = client[mongo_name]
collection = db[mongo_collection]

@app.route('/users', methods=['GET'])
def get_users():
    users = collection.find()
    return dumps(users)

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({'message': 'User added successfully'}), 201

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = collection.find_one({'_id': ObjectId(id)})
    return dumps(user)

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'User updated successfully'})

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')