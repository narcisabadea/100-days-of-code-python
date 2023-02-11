from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from configparser import ConfigParser


def _get_api_key():
    config = ConfigParser()
    config.read("../secrets.ini")
    return config["twitter"]


keys = _get_api_key()

PROMISED_DOWN = 150
PROMISED_UP = 10
SPEED_TEST = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login"
EMAIL = keys["EMAIL"]
PASSWORD = keys["PASSWORD"]
USERNAME = keys["USERNAME"]


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        self.down = 0
        self.up = 0
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(options=options, service=service)

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST)

        # accept pop-up conditions
        sleep(2)
        accept_button = self.driver.find_element(By.ID,
                                                 "onetrust-accept-btn-handler")
        accept_button.click()
        sleep(3)

        self.driver.find_element(
            By.CLASS_NAME, "js-start-test.test-mode-multi").click()
        sleep(45)
        self.up = self.driver.find_element(
            By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed").text
        self.down = self.driver.find_element(
            By.CLASS_NAME, "result-data-large.number.result-data-value.upload-speed").text
        print(f"UP speed: {self.up} Mbps")
        print(f"Down speed: {self.down} Mbps")

        if int(float(self.up)) < PROMISED_UP or int(float(self.down)) < PROMISED_DOWN:
            self.tweet_at_provider()

    def tweet_at_provider(self):
        # Login into twitter
        self.driver.get(TWITTER_URL)
        sleep(2)
        email_input = self.driver.find_element(By.NAME, "text")
        email_input.send_keys(EMAIL)
        email_input.send_keys(Keys.ENTER)
        sleep(1)
        username_input = self.driver.find_element(By.NAME, "text")
        username_input.send_keys(USERNAME)
        username_input.send_keys(Keys.ENTER)
        sleep(1)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        sleep(2)

        # Compose tweet
        tweet_compose = self.driver.find_element(
            By.CLASS_NAME, "notranslate")
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        tweet_compose.send_keys(Keys.COMMAND+Keys.ENTER)

        sleep(2)
        self.driver.quit()
