import ast
import json
import requests


def getAllGames(url_matchs):
    
    try:
        resposta = requests.get(url_matchs).json()
        # print(resposta)
    except Exception as e:
        print("Erro ao conectar com a API")
        resposta = e
    
    return resposta

def filterNextGames(list_games, url_matchs):
    max_match = 10
    count_now = 0
    next_matchs = []
    for match in list_games:
        new_url = url_matchs + f"/{match['id']}"
        next_matchs.append(new_url)
        count_now += 1
        if count_now >= max_match:
            break

    return next_matchs

def getMatchInfo(urls):
    next_matchs_info = []
    for url in urls:
        try:
            teste = requests.get(url)
            if(teste.status_code != 200):
                break
            next_matchs_info.append(teste.json())
            
        except Exception as e:
            print("Erro ao conectar com a API")
            print(e)
            break
    
    return next_matchs_info

def getMatchByMatchId(match_id):
    try:
        match = requests.get(f'http://191.252.5.225:5000/get-matches-statistics/{match_id}').json()
        return match
    except:
        return False

def strutuctInfo(info):
    new_dict_string = {}
    
    try:
        new_dict_string.update({
            "new_uri": f"{info['newUri']}"
        })
    except:
        new_dict_string.update({
            "new_uri": ""
        })
    
    try:
        new_dict_string.update({
            "has_map": f"{info['hasMap']}"
        })
    except:
        new_dict_string.update({
            "has_map": False
        })
    
    try:
        new_dict_string.update({
            "match_id": f"{info['id']}"
        })
    except:
        new_dict_string.update({
            "match_id": ""
        })
    
    try:
        new_dict_string.update({
            "team1_rank": f"{info['team1']['rank']}"
        })
    except:
        new_dict_string.update({
            "team1_rank": ""
        })
    
    try:
        new_dict_string.update({
            "team2_rank": f"{info['team2']['rank']}"
        })
    except:
        new_dict_string.update({
            "team2_rank": ""
        })
    
    try:
        new_dict_string.update({
            "team1_name": f"{info['team1']['name']}"
        })
    except:
        new_dict_string.update({
            "team1_name": ""
        })
    
    try:
        new_dict_string.update({
            "team2_name": f"{info['team2']['name']}"
        })
    except:
        new_dict_string.update({
            "team2_name": ""
        })
    try:
        new_dict_string.update({
            "match_date": f"{info['date']}"
        })
    except:
        new_dict_string.update({
            "match_date": ""
        })

    return new_dict_string

def getMapsBO3(match_id, url):
    url_local = f"http://127.0.0.1:8000/machAnalytic/{match_id}/{url}"
    response = requests.get(url_local)
    
    return response.json()

def getMapsBO1(match_id, url):
    url_local = f"http://127.0.0.1:8000/machAnalyticBo1/{match_id}/{url}"
    response = requests.get(url_local)
    
    return response.json()

def getMapsBO5(match_id, url):
    url_local = f"http://127.0.0.1:8000/machAnalyticBo5/{match_id}/{url}"
    response = requests.get(url_local)
    
    return response.json()