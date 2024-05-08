from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getAllNextGames():
    # Abrir pagina web
    driver = webdriver.Chrome()
    driver.get('https://www.hltv.org/matches')

    # Fecha a janela de cookies
    try :
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="CybotCookiebotDialog"]')))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))).click()
    except Exception as e:
        print(f"Erro ao aceitar cookies: {e}")

    # Encontrar elemento pelo seletor CSS
    element = driver.find_element(By.CSS_SELECTOR, 'body > div.bgPadding > div.widthControl > div:nth-child(2) > div.contentCol > div.newMatches > div.standardPageGrid > div > div.upcomingMatchesWrapper > div > div.upcomingMatchesAll')
    
    objeto_total = []
    for div in element.find_elements(By.CSS_SELECTOR, 'div.upcomingMatch'):
        link = div.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        horario_jogo = div.find_element(By.CSS_SELECTOR, 'div.matchInfo > div.matchTime').text
        metch_meta = div.find_element(By.CSS_SELECTOR, 'div.matchInfo > div.matchMeta').text
        try:
            team_1 = div.find_element(By.CSS_SELECTOR, 'div.matchTeams.text-ellipsis > div.matchTeam.team1').text
        except:
            team_1 = 'N/A'
            
        try:
            team_2 = div.find_element(By.CSS_SELECTOR, 'div.matchTeams.text-ellipsis > div.matchTeam.team2').text
        except:
            team_2 = 'N/A'
        # print(team_2)
        objeto = {
            'link': link,
            'horario_jogo': horario_jogo,
            'metch_meta': metch_meta,
            'team_1': team_1,
            'team_2': team_2,
        }
        objeto_total.append(objeto)

    # imprimir objeto formatação json
    driver.quit()
    
    return objeto_total