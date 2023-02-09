from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"
chrome_driver_path = "/Users/narcisabadea/Desktop/Development/chromedriver"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(URL)

times = driver.find_elements(By.CLASS_NAME, "event-widget time")
descriptions = driver.find_elements(By.CLASS_NAME, "event-widget li a")

events = {}
for n in range(len(times)):
    events[n] = {
        "time": times[n].text,
        "name": descriptions[n].text
    }

print(events)
