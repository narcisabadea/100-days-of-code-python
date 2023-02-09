from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver_path = "/Users/narcisabadea/Desktop/Development/chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(chrome_driver_path)
driver = webdriver.Chrome(options=options, service=service)

driver.get(URL)

article = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
article_count = article.text
print(article_count)

# clicking on the page
article.click()
view_history_link = driver.find_element(By.LINK_TEXT, 'View history')
view_history_link.click()

# search
search_bar = driver.find_element(By.CSS_SELECTOR, ".vector-search-box-input")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
