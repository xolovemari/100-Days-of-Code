from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

load_dotenv()

class InternetSpeedTwitterBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        try:
            accept_button = WebDriverWait(self.driver, 300).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            accept_button.click()
        except Exception as e:
            print(f"Error clicking button: {e}")

        try:
            analyze_speed_button = WebDriverWait(self.driver, 300).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a"))
            )
            analyze_speed_button.click()
        except Exception as e:
            print(f"Error clicking button: {e}")

        time.sleep(60)
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed.result-data-large").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed.result-data-large").text
        print(f"down: {self.down}\nup: {self.up}")


    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        
        try:
            username_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']"))
            )
            username = os.getenv("TWITTER_USERNAME")
            username_input.send_keys(username, Keys.ENTER)
        except Exception as e:
            print(f"Error sending username: {e}")
        
        try:
            password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='current-password']"))
            )
            password = os.getenv("TWITTER_PASSWORD")
            password_input.send_keys(password, Keys.ENTER)
        except Exception as e:
            print(f"Error sending password: {e}")
        
        try:
            tweet_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/compose/post']"))
            )
            tweet_button.click()
        except Exception as e:
            print(f"Error clicking tweet button: {e}")

        try:
            post = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
            )
            tweet_text = (
                f"Hello, why is my internet speed {self.down} Mbps down "
                f"and {self.up} Mbps up, when I pay for {PROMISED_DOWN} Mbps down and {PROMISED_UP} Mbps up? "
                f"Please fix this!"
            )
            post.send_keys(tweet_text)
        except Exception as e:
            print(f"Error writing tweet: {e}")

        try:
            tweet_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButton']"))
            )
            tweet_button.click()
        except Exception as e:
            print(f"Error sending tweet: {e}")