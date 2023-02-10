from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "/Users/narcisabadea/Desktop/Development/chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")


timeout = time.time() + 5
play_time = time.time() + 60 * 5

while time.time() < play_time:
    cookie.click()

    if time.time() > timeout:
        # items that can be bought have a white background (so not greyed out)
        buyable_items = driver.find_elements(
            By.CSS_SELECTOR, "#store > div:not(.grayed)")

        # if we have items that can be bought we click on the last one to buy it
        if len(buyable_items) > 0:
            buyable_items[-1].click()

        # we repeat the process every 5 seconds
        timeout = time.time() + 5

print("Your final score:", driver.find_element(By.ID, "cps").text)
driver.save_screenshot("result.png")
