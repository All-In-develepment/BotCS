import requests
import pandas as pd

pagina = 1
jogos = {}
resultados = []
execultar = True

while execultar:
    jogos = requests.get(f'http://191.252.5.229:8080/api/Tips?pageNumber={pagina}').json()
    pagina += 1
    if len(jogos) == 0:
        execultar = False
    for jogo in jogos:
        resultados.append(jogo)
jogos_df = pd.DataFrame(resultados)

unders_green = {
    '23,5': 0,
    '22,5': 0,
    '21,5': 0,
    '20,5': 0,
    '19,5': 0,
    '18,5': 0,
    '17,5': 0,
}

unders_red = {
    '23,5': 0,
    '22,5': 0,
    '21,5': 0,
    '20,5': 0,
    '19,5': 0,
    '18,5': 0,
    '17,5': 0,
}

for jogo in resultados:
    for key, under in enumerate(jogo['tipMapOdd']):
        if under == '23,5':
            if jogo['tipsMapResult'][key] == '✅':
                unders_green['23,5'] += 1
            else:
                unders_red['23,5'] += 1
        elif under == '22,5':
            if jogo['tipsMapResult'][key] == '✅':
                unders_green['22,5'] += 1
            else:
                unders_red['22,5'] += 1
        elif under == '21,5':
            if jogo['tipsMapResult'][key] == '✅':
                unders_green['21,5'] += 1
            else:
                unders_red['21,5'] += 1
        elif under == '20,5':
            if jogo['tipsMapResult'][key] == '✅':
                unders_green['20,5'] += 1
            else:
                unders_red['20,5'] += 1
        elif under == '19,5':
            if jogo['tipsMapResult'][key] == '✅':
                unders_green['19,5'] += 1
            else:
                unders_red['19,5'] += 1
        elif under == '18,5':
            if jogo['tipsMapResult'][key] == '✅':
                unders_green['18,5'] += 1
            else:
                unders_red['18,5'] += 1
        elif under == '17,5':
            if jogo['tipsMapResult'][key] == '✅':
                unders_green['17,5'] += 1
            else:
                unders_red['17,5'] += 1

# DataFrame com os resultados 
unders_green_df = pd.DataFrame(unders_green.items(), columns=['Under', 'Green'])
unders_red_df = pd.DataFrame(unders_red.items(), columns=['Under', 'Red'])

final_results = unders_green_df.add(unders_red_df, fill_value=0, axis=0)
# Media de acertos
final_results['Total'] = final_results['Green'] + final_results['Red']
final_results['Percentage'] = final_results['Green'] / final_results['Total'] * 100
final_results['Under'] = final_results['Under'].str.split(',')
final_results.to_csv('unders.csv', sep=',')

# Media total de acertos
final_results['Percentage'].mean()