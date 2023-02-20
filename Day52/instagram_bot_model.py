from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import random
from configparser import ConfigParser


def _get_api_key():
    config = ConfigParser()
    config.read("../secrets.ini")
    return config["instagram"]


keys = _get_api_key()

INSTAGRAM_URL = "https://www.instagram.com/"
EMAIL = keys["EMAIL"]
PASSWORD = keys["PASSWORD"]
SIMILAR_ACCOUNT = "chefsteps"


class InstaFollower:
    def __init__(self, chrome_driver_path):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(options=options, service=service)

    def login(self):
        self.driver.get(INSTAGRAM_URL)

        # Accept pop-up conditions
        sleep(2)
        all_buttons = self.driver.find_elements(By.TAG_NAME,
                                                "button")
        for button in all_buttons:
            if button.text == "Only allow essential cookies":
                button.click()
        sleep(3)

        # Login
        self.driver.find_element(By.NAME, "username").send_keys(EMAIL)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        self.driver.find_element(By.ID, "loginForm").click()

        sleep(3)
        self.find_followers()

    def find_followers(self):
        sleep(3)
        self.driver.get(
            f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        sleep(3)
        self.follow()

    def follow(self):
        try:
            list_of_followers = self.driver.find_elements(
                By.CSS_SELECTOR, 'button')
            for item in list_of_followers:
                if item.text == "Follow":
                    item.click()
                    sleep(random.randint(5, 10))

        except Exception as e:
            print(e)
