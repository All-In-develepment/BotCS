import requests
import json

resposta = requests.get('https://odds.data.bet/affiliates/218769Lol_CS2/json').json()
jogos_cs = []
jogos_lol = []
eventos = []

for event in resposta['Sport']['eSports']['Events']:
    if event['CategoryID'] == 'esports_counter_strike':
        jogos_cs.append(event)
    if event['CategoryID'] == 'esports_league_of_legends':
        jogos_lol.append(event)
    eventos.append(event)
    