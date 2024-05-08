import json
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
from flask import Flask, jsonify


def ListMultipleMatchs():
    try:
        result = requests.get("http://191.252.5.229:8080/api/Tips")
        return result
        
    except Exception as e:
        return jsonify({'error': f'Erro ao obter os dados, {e}'}), 500
    
def ListSingleMatch(match_id):
    try:
        result = requests.get(f"http://191.252.5.229:8080/api/Tips/{match_id}")
        return result
        
    except Exception as e:
        return jsonify({'error': f'Erro ao obter os dados, {e}'}), 500


def InsertOne(data):
    
    try:
        result = requests.post("http://191.252.5.229:8080/api/Tips", json = data)
        return result

    except Exception as e:
        return jsonify({'error': f'Erro ao obter os dados, {e}'}), 500
    
    
def FindMatchByMatchId(match_id):
    try:
        result = requests.get(f"http://191.252.5.229:8080/api/Tips/match/{match_id}")
        if (result.status_code == 200):
            return result.json()
        else:
            return jsonify({'error': f'Erro ao obter os dados, {e}'}), 500
        
    except Exception as e:
        return jsonify({'error': f'Erro ao obter os dados, {e}'}), 500

# def DeleteOne(document_id):
#     collection, success = CreateConnection()
#     if success:
#         try:
#             result = collection.delete_one({'_id': ObjectId(document_id)})
#             return result.deleted_count, True
#         except Exception as e:
#             print(f"Erro ao deletar documento: {e}")
#             return None, False
#     else:
#         print("Erro ao Conectar com banco de dados")
#         return None, False
    
# def EditOne(document_id, new_values):
#     collection, success = CreateConnection()
#     if success:
#         try:
#             result = collection.update_one({'_id': ObjectId(document_id)}, {'$set': new_values})
#             return result.modified_count, True
#         except Exception as e:
#             print(f"Erro ao editar documento: {e}")
#             return None, False
#     else:
#         print("Erro ao Conectar com banco de dados")
#         return None, False

# def InsertOrUpdateGame(game_data):
#     collection, success = CreateConnection()
#     if success:
#         try:
#             match_id = game_data['match_id']
#             existing_game = collection.find_one({"match_id": match_id})
#             if existing_game:
#                 print(f"Jogo com o match_id {match_id} já existe no banco de dados. Ignorando inserção.")
#             else:
#                 result = collection.insert_one(game_data)
#                 print(f"Jogo inserido com sucesso com o ID: {result.inserted_id}")
#             return True
#         except Exception as e:
#             print(f"Erro ao inserir ou atualizar jogo: {e}")
#             return False
#     else:
#         print("Erro ao Conectar com banco de dados")
#         return False
