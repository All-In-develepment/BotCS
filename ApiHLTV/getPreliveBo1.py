from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getPreLiveBo1(idMatch, urlSuplie):
    driver = webdriver.Chrome()
    
    url = f"https://www.hltv.org/betting/analytics/{idMatch}/{urlSuplie}"
    
    json_return = {}
    
    driver.get(url)
    try :
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="CybotCookiebotDialog"]')))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))).click()
    except Exception as e:
        print(f"Erro ao aceitar cookies: {e}")
    
    # Localize o elemento específico
    elementos= {
        "firt_map_element": "#handicap > div.analytics-handicap-map-wrapper.g-grid > div:nth-child(1) > div > div.analytics-handicap-map-data-container > div.analytics-handicap-map-data-bottom > div.analytics-handicap-map-data-table-container > table > tbody > tr:nth-child(1) > td.analytics-handicap-map-data-mapname > div",
        "status_tima_a_first_map": "#handicap > div.analytics-handicap-map-wrapper.g-grid > div:nth-child(1) > div > div.analytics-handicap-map-data-container > div.analytics-handicap-map-data-bottom > div.analytics-handicap-map-data-table-container > table > tbody > tr:nth-child(1) > td:nth-child(2)",
        "status_tima_b_first_map": "#handicap > div.analytics-handicap-map-wrapper.g-grid > div:nth-child(2) > div > div.analytics-handicap-map-data-container > div.analytics-handicap-map-data-bottom > div.analytics-handicap-map-data-table-container > table > tbody > tr:nth-child(1) > td:nth-child(2)",
        "count_maps_team_a": "#handicap > div.analytics-handicap-map-wrapper.g-grid > div:nth-child(1) > div > div.analytics-handicap-map-header > span.handicap-map-count.gtSmartphone-only",
        "count_maps_team_b": "#handicap > div.analytics-handicap-map-wrapper.g-grid > div:nth-child(2) > div > div.analytics-handicap-map-header > span.handicap-map-count.gtSmartphone-only",
    }
    try:
        for elemento in elementos:
            try:
                element = driver.find_element(By.CSS_SELECTOR, elementos[elemento])
                json_return.update({elemento: element.text})
                # print(element.text)
            except Exception as e:
                print(f"Erro ao encontrar elemento: {elemento}")
                json_return.update({elemento: "N/A"})
            
        driver.quit()
        json_return.update({"count_matchs_team_a": json_return["count_maps_team_a"].split(",")[0]})
        json_return.update({"count_matchs_team_b": json_return["count_maps_team_b"].split(",")[0]})
        json_return.update({"count_maps_team_a": json_return["count_maps_team_a"].split(",")[1]})
        json_return.update({"count_maps_team_b": json_return["count_maps_team_b"].split(",")[1]})
        return json_return
    except Exception as e:
        print(f"Erro ao encontrar elemento: {e}")
        
        return e