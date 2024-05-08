from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getMapStats():
    # Inicialização do navegador
    driver = webdriver.Chrome()

    url = "https://www.hltv.org/stats/teams/map/48/12431/betera?startDate=2024-01-04&endDate=2024-04-04"

    driver.get(url)

    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="CybotCookiebotDialog"]')))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))).click()
    except Exception as e:
        print(f"Erro ao aceitar cookies: {e}")

    # Localize o elemento específico
    elementos = ["body > div.bgPadding > div.widthControl > div:nth-child(2) > div.contentCol > div.stats-section.stats-team.stats-team-map > div:nth-child(6) > div:nth-child(1) > div.stats-rows.standard-box > div:nth-child(9) > span.strong","body > div.bgPadding > div.widthControl > div:nth-child(2) > div.contentCol > div.stats-section.stats-team.stats-team-map > div:nth-child(6) > div:nth-child(1) > div.stats-rows.standard-box > div:nth-child(9) > span.won"]

    for elemento in elementos:
        try:
            element = driver.find_element(By.CSS_SELECTOR, elemento)
            print(element.text)
        except Exception as e:
            print(f"Erro ao encontrar elemento: {e}")
            
    driver.quit()