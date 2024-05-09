import requests


def CheckResult(match_id):
    try:
        match = requests.get(f'http://191.252.5.229:8080/api/Tips/match/{match_id}').json()
        if match['status']:
            return match
        else:
            return False
    except:
        return False