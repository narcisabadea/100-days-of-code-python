# Selenium WebDriver

# Is a technology for advanced web scraping, it's also probably one of the most well-known automation and testing tools for web developers out there.
# So when we load up a website with beautiful soup, we can't, for example, type something into the website and then click on something.
# And to create these chains of continuous actions where we basically automate the entire flow of a particular job or a particular task.
# To do that, we're going to need to use Selenium WebDriver.
# This is a free tool and it basically allows the browser to do things automatically depending on a script or a piece of code that we write.
# Might use something like selenium to automate filling in forms or transferring information from an Excel spreadsheet to a online Google form, or basically doing anything that is repetitive and tedious.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

AMAZON_URL = "https://www.amazon.com/Instant-Pot-Electric-Sterilizer-Stainless/dp/B09MZTSSR2/ref=sr_1_1_sspa?keywords=Instant%2BPot%2BDuo%2BEvo%2BPlus&qid=1675868892&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMzJPOFVaWU5OQU8zJmVuY3J5cHRlZElkPUEwMzY3NDI0TzVOUzRGSFU0NlMzJmVuY3J5cHRlZEFkSWQ9QTA0NjgwMzYzNURPMDBZNkZQMlEmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1"
chrome_driver_path = "/Users/narcisabadea/Desktop/Development/chromedriver"
# added option to not close the chrome window after the code is finished executing
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(chrome_driver_path)
driver = webdriver.Chrome(options=options, service=service)

driver.get(AMAZON_URL)

whole_price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
fractional_price = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
price = float(whole_price + "." + fractional_price)
print(price)
