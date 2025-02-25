from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

statistics = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a[title='Special:Statistics']")
total_eng_articles = statistics[1]

total_eng_articles.click()