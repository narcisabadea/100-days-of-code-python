from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

chrome_driver_path = "/Users/narcisabadea/Desktop/Development/chromedriver"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdMK-mRkGPuiMp6oNTrVqfwZGBbs80_1fPrI1dsGojxXH0Wyw/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "Accept-Language": "en-US,en;q=0.9,ro;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

response = requests.get(ZILLOW_URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Scrap zillow website with B4S for the link, price and address of the rental listings
grid_search_results = soup.find(id="grid-search-results")

all_link_elements = grid_search_results.find_all(name="a")
all_links = []
for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_prices_elements = grid_search_results.find_all(name="span")
all_prices = []
for price in all_prices_elements:
    if price.text[0] == '$':
        if "+" in price.text:
            all_prices.append(price.text.split("+")[0])
        elif "/mo" in price.text:
            all_prices.append(price.text.split("/mo")[0])
        else:
            all_prices.append(price.text)


all_addresses_elements = grid_search_results.find_all(name="address")
all_addresses = []
for address in all_addresses_elements:
    if len(address.text.split("|")) == 1:
        index = 0
    else:
        index = 1
    all_addresses.append(address.text.split("|")[index].strip())

print(all_links)
print(all_prices)
print(all_addresses)

# Add selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(options=options, service=service)

# Scrap Google form to add and submit the form for every link
for n in range(len(all_links)):
    driver.get(GOOGLE_FORM_URL)

    form_container = driver.find_element(By.CLASS_NAME, "o3Dpx")
    all_inputs = form_container.find_elements(By.TAG_NAME, "input")
    address_input = all_inputs[0]
    price_input = all_inputs[1]
    link_input = all_inputs[2]
    sleep(1)
    address_input.send_keys(all_addresses[n])
    sleep(1)
    price_input.send_keys(all_prices[n])
    sleep(1)
    link_input.send_keys(all_links[n])
    sleep(1)
    submit_button = driver.find_element(By.CLASS_NAME, "uArJ5e")
    submit_button.click()
