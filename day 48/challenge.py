from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, value="fName")
first_name_input.clear()

first_name = "Mariana"
first_name_input.send_keys(first_name)

last_name_input = driver.find_element(By.NAME, value="lName")
last_name_input.clear()

last_name = "Moreira"
last_name_input.send_keys(last_name)

email_input = driver.find_element(By.NAME, value="email")
email_input.clear()

email = "example@gmail.com"
email_input.send_keys(email)

sign_up_button = driver.find_element(By.CLASS_NAME, value="btn")
sign_up_button.click()