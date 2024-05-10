from DataBases.Connection import UpdateTip
from Games import getMatchByMatchId
from Messages.messagens import EditMessage, SendMessage


def CheckResult(tip):
    point = 0
    bets_result = [0] * 3
    match = getMatchByMatchId(tip["tipMatchId"])
    # print(match)
    for entrada in tip["tipMapOdd"]:
        print(f"Point atual: {point}")
        try:
            entrada_float = entrada.replace(",", ".")
            entrada_float = float(entrada_float)
            print(entrada_float)
        except:
            print("Não tem entrada para esse mapa")
            entrada_float = "Não tem entrada para esse mapa"
            
        if ("winnerTeam" in match):
            print(match)
            try:
                maps_rouds = match["maps"][point]["result"]["team1TotalRounds"] + match["maps"][point]["result"]["team2TotalRounds"]
            except:
                maps_rouds = 0
            print(f"Total de Rounds: {maps_rouds}")
        
        if entrada_float != "Não tem entrada para esse mapa":
            if maps_rouds < entrada_float:
                print("Ganhou")
                bets_result[point] = "✅"
            else:
                bets_result[point] = "❌"
                print("Perdeu")
        else:
            bets_result[point] = ""
        
        point += 1
    
    with open('./Messages/resultado_message.txt', 'r', encoding='utf-8') as file:
        all_results = file.read().format(
            time_a=tip['teamA'],
            time_b=tip['teamB'],
            match_date=tip['tipDate'].split('T')[0],
            match_time=tip['tipDate'].split('T')[1],
            favorite_team=tip['favoriteTeam'],
            map_1=tip["tipMaps"][0],
            map_2=tip["tipMaps"][1],
            map_3=tip["tipMaps"][2],
            entrada_1=f'UNDER {tip["tipMapOdd"][0]}',
            entrada_2=f'UNDER {tip["tipMapOdd"][1]}',
            entrada_3=f'UNDER {tip["tipMapOdd"][2]}',
            resultado_1=bets_result[0],
            resultado_2=bets_result[1],
            resultado_3=bets_result[2]
        )
    
    print(all_results)
    try:
        EditMessage(tip["tipMessageId"], all_results)
    except Exception as e:
        print(e)
        
    update_result = UpdateTip(tip["tipMatchId"], bets_result)
    print(update_result)