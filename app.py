import time
import os
from datetime import datetime
from Games import getAllGames, filterNextGames, getMapsBO1, getMapsBO3, getMapsBO5, getMatchInfo, strutuctInfo
from Messages.messagens import SendMessage
from Tips.TipsManager import CreateTips, VerifyOpenTip
from verifyerTeam import AvgWinPeerLoos, FavoriteTeam
from DataBases.Connection import ListMultipleMatchs, ListSingleMatch, InsertOne, DeleteOne, EditOne, CreateConnection, FindMatchByMatchId, InsertOrUpdateGame



# Definindo um conjunto para armazenar IDs de partidas enviadas
partidas_enviadas = set()

url_matchs = "http://191.252.5.225:5000/get-matches-statistics"

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # Busca todos os jogos
    all_games = getAllGames(url_matchs)
    
    try:
        # verifica se o retorno está correto
        if all_games != "Erro ao conectar com a API" or all_games['statusCode'] != 500:
            
            # Filtra os próximos 10 jogos
            next_games = filterNextGames(all_games, url_matchs)
            print("next_games")
            
            match_info = getMatchInfo(next_games)
            print(len(match_info))
            
            # Percorre todos os jogos retornados
            for match in match_info:
                # Cria uma estrutura com as informações do jogo
                new_structure = strutuctInfo(match)
                
                # Verifica se tem mapa já definido na partida
                if str(new_structure['has_map']) == "True":
                    
                    # Consulta no banco para ver se há uma tip em aberto
                    tip_is_open = VerifyOpenTip(match['id'])
                    
                    # Se a tip não estiver aberta e se o ID da partida ainda não foi enviado
                    if not tip_is_open and match['id'] not in partidas_enviadas:
                        # Busca as informações de acordo com o tipo de jogo
                        if match["format"]["type"] == "bo3":
                            informacoes = getMapsBO3(new_structure['match_id'], new_structure['new_uri'])
                        elif match["format"]["type"] == "bo5":
                            informacoes = getMapsBO5(new_structure['match_id'], new_structure['new_uri'])
                        else:
                            informacoes = getMapsBO1(new_structure['match_id'], new_structure['new_uri'])

                        # Define o time favorito
                        favorite_team = FavoriteTeam(match['team1']['name'], match['team2']['name'], match['team1']['rank'], match['team2']['rank'], 25)

                        # Formatação de data de forma legível
                        date_timestemp = datetime.fromtimestamp(match['date']/1000)

                        # Verifica se o time favorito é o time 1 ou 2
                        if favorite_team == 'T1':
                            favorite_team = match['team1']['name']
                            # tenta converter o valor para float, caso não consiga, atribui 0
                            try:
                                first_map_avg = float(informacoes['status_tima_a_first_map'])
                            except:
                                first_map_avg = 0

                            try:
                                second_map_avg = float(informacoes['status_tima_a_second_map'])
                            except:
                                second_map_avg = 0

                            try:
                                third_map_avg = float(informacoes['status_tima_a_third_map'])
                            except:
                                third_map_avg = 0

                            # Monta a dica de acordo com a média de vitórias
                            first_map_tip = AvgWinPeerLoos(first_map_avg)
                            second_map_tip = AvgWinPeerLoos(second_map_avg)
                            third_map_tip = AvgWinPeerLoos(third_map_avg)

                            # Abre o arquivo de mensagem e formata a mensagem
                            with open('Messages/entrada_message.txt', 'r', encoding='utf-8') as file:
                                entrada = file.read().format(
                                    time_a=match['team1']['name'],
                                    time_b=match['team2']['name'],
                                    match_date=date_timestemp.strftime('%d/%m/%Y'),
                                    match_time=date_timestemp.strftime('%H:%M'),
                                    favorite_team=favorite_team,
                                    map_1=informacoes['firt_map_element'],
                                    map_2=informacoes['second_map_element'],
                                    map_3=informacoes['third_map_element'],
                                    entrada_1=f'UNDER {first_map_tip}',
                                    entrada_2=f'UNDER {second_map_tip}',
                                    entrada_3=f'UNDER {third_map_tip}'
                                )

                            # Envia a mensagem
                            SendMessage(entrada)

                            # Insere a dica no banco de dados
                            InsertOrUpdateGame({
                                'match_id': match['id'],
                                'status': True,
                                'date': date_timestemp.strftime('%d/%m/%Y %H:%M'),
                                'team_a': match['team1']['name'],
                                'team_b': match['team2']['name'],
                                'map_1': informacoes['firt_map_element'],
                                'map_2': informacoes['second_map_element'],
                                'map_3': informacoes['third_map_element'],
                                'map_4': 'N/A',
                                'map_5': 'N/A',
                                'entrada_1': f'UNDER {first_map_tip}',
                                'entrada_2': f'UNDER {second_map_tip}',
                                'entrada_3': f'UNDER {third_map_tip}',
                                'entrada_4': 'N/A',
                                'entrada_5': 'N/A'
                            })

                            # Adiciona o ID da partida ao conjunto de partidas enviadas
                            partidas_enviadas.add(match['id'])

                        elif favorite_team == 'T2':
                            favorite_team = match['team2']['name']
                            try:
                                first_map_avg = float(informacoes['status_tima_b_first_map'])
                            except:
                                first_map_avg = 0
                            try:
                                second_map_avg = float(informacoes['status_tima_b_second_map'])
                            except:
                                second_map_avg = 0
                            try:
                                third_map_avg = float(informacoes['status_tima_b_third_map'])
                            except:
                                third_map_avg = 0

                            first_map_tip = AvgWinPeerLoos(first_map_avg)
                            second_map_tip = AvgWinPeerLoos(second_map_avg)
                            third_map_tip = AvgWinPeerLoos(third_map_avg)
                            with open('Messages/entrada_message.txt', 'r', encoding='utf-8') as file:
                                entrada = file.read().format(
                                    time_a=match['team1']['name'],
                                    time_b=match['team2']['name'],
                                    match_date=date_timestemp.strftime('%d/%m/%Y'),
                                    match_time=date_timestemp.strftime('%H:%M'),
                                    favorite_team=favorite_team,
                                    map_1=informacoes['firt_map_element'],
                                    map_2=informacoes['second_map_element'],
                                    map_3=informacoes['third_map_element'],
                                    entrada_1=f'UNDER {first_map_tip}',
                                    entrada_2=f'UNDER {second_map_tip}',
                                    entrada_3=f'UNDER {third_map_tip}'
                                )
                            SendMessage(entrada)
                            InsertOrUpdateGame({
                                'match_id': match['id'],
                                'status': True,
                                'date': date_timestemp.strftime('%d/%m/%Y %H:%M'),
                                'team_a': match['team1']['name'],
                                'team_b': match['team2']['name'],
                                'map_1': informacoes['firt_map_element'],
                                'map_2': informacoes['second_map_element'],
                                'map_3': informacoes['third_map_element'],
                                'map_4': 'N/A',
                                'map_5': 'N/A',
                                'entrada_1': f'UNDER {first_map_tip}',
                                'entrada_2': f'UNDER {second_map_tip}',
                                'entrada_3': f'UNDER {third_map_tip}',
                                'entrada_4': 'N/A',
                                'entrada_5': 'N/A'
                            })

                            # Adiciona o ID da partida ao conjunto de partidas enviadas
                            partidas_enviadas.add(match['id'])
                        else:
                            print("Não atende aos requisitos")

                else:
                    print("Partida sem mapa\n--------------------------")
    except Exception as e:
        print(e)
    
    time.sleep(10)
