import requests
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'API Rodando'})

@app.route('/tips', methods=['GET'])
def getTips():
    pagina = 1
    jogos = {}
    resultados = []
    execute = True
    
    while execute:
        jogos = requests.get(f'http://191.252.5.229:8080/api/Tips?pageNumber={pagina}').json()
        pagina += 1
        if len(jogos) == 0:
            execute = False
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
        if (jogo['tipStatus'] == False):
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
    final_results['Percentage'] = round(final_results['Green'] / final_results['Total'] * 100, 2)
    final_results['Percentage'] = final_results['Percentage'].fillna(0)
    final_results['Under'] =  final_results['Under'].str.slice(0,4)
    final_results.to_csv('unders.csv', sep=',')
    final_results['Percentage'].mean()
    # Media total de acertos
    result = final_results.to_dict(orient='records')
    return jsonify(result)
    
if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=True)


