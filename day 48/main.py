from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

big_cookie = driver.find_element(By.ID, value="cookie")
total_cookies = driver.find_element(By.ID, value="money")
store_section = driver.find_element(By.ID, value="store")
cookies_per_second = driver.find_element(By.ID, value="cps")

def get_cookie_count():
    return int(total_cookies.text.replace(",", ""))

game_is_on = True
initial_time = time.time()
last_check_time = initial_time

while game_is_on:
    big_cookie.click()

    current_time = time.time()
    if current_time - initial_time >= 300:  
        game_is_on = False

    if current_time - last_check_time >= 5: 
        cookie_count = get_cookie_count()
        upgrades_available = {}

        upgrades = store_section.find_elements(By.TAG_NAME, "div")
        for upgrade in upgrades:
            try:
                upgrade_value = upgrade.find_element(By.TAG_NAME, "b").text
                
                value_number = int(upgrade_value.split("-")[1].strip().replace("Price:", "").replace(",", ""))
            
                if cookie_count >= value_number:
                    upgrades_available[upgrade] = value_number
            except:
                continue 


        if upgrades_available:
            biggest_value_key = max(upgrades_available.items(), key=lambda item: item[1])[0]
            biggest_value_key.click()

        last_check_time = current_time

# Fecha o navegador
driver.quit()