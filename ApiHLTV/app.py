from flask import Flask, jsonify
from getAllNextGames import getAllNextGames
from getMapStats import getMapStats
from getPreLiveInformation import getPreLiveInformation
from getPreliveBo1 import getPreLiveBo1

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'API Rodando'})

@app.route('/mapStats', methods=['GET'])
def map_stats():
    return jsonify(getMapStats())

@app.route('/allMatches', methods=['GET'])
def all_matches():
    return jsonify(getAllNextGames())

@app.route('/machAnalytic/<matchid>/<suplie>', methods=['GET'])
def analytics(matchid, suplie):
    return jsonify(getPreLiveInformation(matchid, suplie))

@app.route('/machAnalyticBo1/<matchid>/<suplie>', methods=['GET'])
def analytics_bo1(matchid, suplie):
    return jsonify(getPreLiveBo1(matchid, suplie))

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')