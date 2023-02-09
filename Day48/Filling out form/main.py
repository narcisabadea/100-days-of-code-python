from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "/Users/narcisabadea/Desktop/Development/chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(chrome_driver_path)
driver = webdriver.Chrome(options=options, service=service)

driver.get(URL)

first_name_input = driver.find_element(By.CLASS_NAME, "top")
second_name_input = driver.find_element(By.CLASS_NAME, "middle")
email_input = driver.find_element(By.CLASS_NAME, "bottom")

first_name_input.send_keys("First name")
second_name_input.send_keys("Second name")
email_input.send_keys("email@email.com")

submit_button = driver.find_element(By.CLASS_NAME, "btn")

submit_button.send_keys(Keys.ENTER)
