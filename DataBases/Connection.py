from pymongo import MongoClient
from bson.objectid import ObjectId

def CreateConnection():
    try:
        uri = "mongodb://botcs:allIn2022@194.35.120.140?retryWrites=true&writeConcern=majority"
        client = MongoClient(uri)
        db = client["cs"]
        collection = db["cs_bot"]
        return collection, True

    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None, False

def ListMultipleMatchs():
    collection, success = CreateConnection()
    if success:
        try:
            documents = collection.find()
            return list(documents), True
        except Exception as e:
            print(f"Erro ao listar documentos: {e}")
            return [], False
    else:
        print("Erro ao Conectar com banco de dados")
        return [], False
    
def ListSingleMatch(match_id):
    collection, success = CreateConnection()
    if success:
        try:
            documents = collection.find_one({"_id": ObjectId(match_id)})
            return documents, True
        except Exception as e:
            print(f"Erro ao listar documentos: {e}")
            return [], False
    else:
        print("Erro ao Conectar com banco de dados")
        return [], False

def FindMatchByMatchId(match_id):
    collection, success = CreateConnection()
    if success:
        try:
            documents = collection.find({"match_id": match_id})
            return documents, True
        except Exception as e:
            print(f"Erro ao listar documentos: {e}")
            return [], False
    else:
        print("Erro ao Conectar com banco de dados")
        return [], False

def InsertOne(data):
    collection, success = CreateConnection()
    if success:
        try:
            result = collection.insert_one(data)
            return result.inserted_id, True
        except Exception as e:
            print(f"Erro ao inserir documento: {e}")
            return None, False
    else:
        print("Erro ao Conectar com banco de dados")
        return None, False

def DeleteOne(document_id):
    collection, success = CreateConnection()
    if success:
        try:
            result = collection.delete_one({'_id': ObjectId(document_id)})
            return result.deleted_count, True
        except Exception as e:
            print(f"Erro ao deletar documento: {e}")
            return None, False
    else:
        print("Erro ao Conectar com banco de dados")
        return None, False
    
def EditOne(document_id, new_values):
    collection, success = CreateConnection()
    if success:
        try:
            result = collection.update_one({'_id': ObjectId(document_id)}, {'$set': new_values})
            return result.modified_count, True
        except Exception as e:
            print(f"Erro ao editar documento: {e}")
            return None, False
    else:
        print("Erro ao Conectar com banco de dados")
        return None, False

def InsertOrUpdateGame(game_data):
    collection, success = CreateConnection()
    if success:
        try:
            match_id = game_data['match_id']
            existing_game = collection.find_one({"match_id": match_id})
            if existing_game:
                print(f"Jogo com o match_id {match_id} já existe no banco de dados. Ignorando inserção.")
            else:
                result = collection.insert_one(game_data)
                print(f"Jogo inserido com sucesso com o ID: {result.inserted_id}")
            return True
        except Exception as e:
            print(f"Erro ao inserir ou atualizar jogo: {e}")
            return False
    else:
        print("Erro ao Conectar com banco de dados")
        return False
