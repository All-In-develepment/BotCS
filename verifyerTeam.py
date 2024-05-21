def FavoriteTeam(team_a_name, team_b_name, team_a_rank, team_b_rank, range):
    if (team_a_rank < team_b_rank):
        print(f"Time Favorito é o time a: {team_a_name}")
        if((team_b_rank - team_a_rank) >= range):
            return 'T1'
        else:
            print(f"Diferença entre times menos que {range}")
            return False

    elif (team_b_rank < team_a_rank):
        print(f"Time Favorito é o time B: {team_b_name}")
        if((team_a_rank - team_b_rank) >= range):
            return 'T2'
        else:
            print(f"Diferença entre times menos que {range}")
            return False
    else:
        return False

def AvgWinPeerLoos(avg_map):
    print (avg_map)
    if ((avg_map >= 7) and (avg_map < 8)):
        return "23,5"
    elif((avg_map >= 6) and (avg_map < 7)):
        return "22,5"
    elif((avg_map >= 5) and (avg_map < 6)):
        return "21,5"
    elif((avg_map >= 4) and (avg_map < 5)):
        return "20,5"
    elif((avg_map >= 3) and (avg_map < 4)):
        return "19,5"
    elif((avg_map >= 2) and (avg_map < 3)):
        return "18,5"
    else:
        return 'Não entrar'
