from Games import getMatchByMatchId
from Messages.messagens import SendMessage


def CheckResult(tip):
    point = 0
    bets_result = []
    match = getMatchByMatchId(tip["tipMatchId"])
    print(match)
    for entrada in tip["tipMapOdd"]:
        try:
            entrada_float = entrada.replace(",", ".")
            entrada_float = float(entrada_float)
            print(entrada_float)
        except:
            print("Não tem entrada para esse mapa")
            entrada_float = "Não tem entrada para esse mapa"
            
        if ("winnerTeam" in match):
            maps_rouds = match["maps"][point]["result"]["team1TotalRounds"] + match["maps"][point]["result"]["team2TotalRounds"]
        
        if entrada_float != "Não tem entrada para esse mapa":
            if maps_rouds < entrada_float:
                print("Ganhou")
                bets_result[point] = "✅"
                SendMessage("Ganhou")
            else:
                bets_result[point] = "❌"
                print("Perdeu")
            point += 1