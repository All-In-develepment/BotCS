import json
import requests


def ListMultipleMatchs():
    try:
        result = requests.get("http://191.252.5.229:8080/api/Tips")
        return result
        
    except Exception as e:
        return json({'error': f'Erro ao obter os dados, {e}'}), 500
    
def ListSingleMatch(match_id):
    try:
        result = requests.get(f"http://191.252.5.229:8080/api/Tips/{match_id}")
        return result
        
    except Exception as e:
        return json({'error': f'Erro ao obter os dados, {e}'}), 500


def InsertOne(data):
    
    try:
        result = requests.post("http://191.252.5.229:8080/api/Tips", json = data)
        return result

    except Exception as e:
        return json({'error': f'Erro ao obter os dados, {e}'}), 500
    
    
def FindMatchByMatchId(match_id):
    try:
        result = requests.get(f"http://191.252.5.229:8080/api/Tips/match/{match_id}")
        print(result.status_code)
        if (result.status_code == 200):
            print("Cheguei até aqui")
            return result.json()
        elif (result.status_code == 404):
            result = {"tipStatus": False}
            return result
        else:
            result = {"tipStatus": True}
            return result
        
    except Exception as e:
        return json({'error': f'Erro ao obter os dados, {e}'}), 500
    
def GetOpenTips():
    try:
        match = requests.get(f'http://191.252.5.229:8080/api/Tips/status').json()
        return match
    except:
        return False
    
def UpdateTip(match_id):
    try:
        match = requests.put(f'http://191.252.5.229:8080/api/Tips/{match_id}').json()
        return match
    except:
        return False