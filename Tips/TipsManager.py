import json
import os
from DataBases.Connection import FindMatchByMatchId, InsertOne, ListSingleMatch

def CreateTips(match_id, match_status, match_date, team_a, team_b, map_1, map_2, map_3, map_4, map_5, entrada_1, entrada_2, entrada_3, entrada_4, entrada_5):
    # Cria um dicionário com a dica
    tip = {
        "match_id": match_id,
        "status": match_status,
        "date": match_date,
        "team_a": team_a,
        "team_b": team_b,
        "map_1": map_1,
        "map_2": map_2,
        "map_3": map_3,
        "map_4": map_4,
        "map_5": map_5,
        "entrada_1": entrada_1,
        "entrada_2": entrada_2,
        "entrada_3": entrada_3,
        "entrada_4": entrada_4,
        "entrada_5": entrada_5
    }
    # Insere a tip no banco de dados
    insert_result, insert_success = InsertOne(tip)
    if insert_success:
        print(f"Dica inserida com sucesso id: {insert_result}")

def VerifyOpenTip(match_id):
    # Busca no banco de dados a dica para o jogo
    print(f"Verificando dica para o jogo {match_id}")
    
    tip = FindMatchByMatchId(int(match_id))
    
    if (tip["tipStatus"] == False):
        print(f"Dica fechada para o jogo {match_id}")
        return False
    else:
        print(f"Dica aberta para o jogo {match_id}")
        return True
    
    