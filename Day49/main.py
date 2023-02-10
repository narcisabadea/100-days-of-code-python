from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from configparser import ConfigParser


def _get_api_key():
    config = ConfigParser()
    config.read("../secrets.ini")
    return config["linkedin"]


keys = _get_api_key()
EMAIL = keys["EMAIL"]
PASSWORD = keys["PASSWORD"]

chrome_driver_path = "/Users/narcisabadea/Desktop/Development/chromedriver"
URL = "https://www.linkedin.com/jobs"
EASY_APPLY = "Easy Apply"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(options=options, service=service)
driver.get(URL)

# Login to linkedin
email_input = driver.find_element(By.ID, "session_key")
password_input = driver.find_element(By.ID, "session_password")

email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)

sign_in = driver.find_element(
    By.CLASS_NAME, "sign-in-form__submit-button")

sign_in.send_keys(Keys.ENTER)
sleep(3)

# Search for developer jobs
search_bar = driver.find_element(
    By.CLASS_NAME, "jobs-search-box__text-input")
search_bar.send_keys("Developer")
sleep(2)
search_bar.send_keys(Keys.ENTER)

sleep(2)

# all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")

# If we have an apply button, if not we skip the job
try:
    # Select easy apply jobs
    filter_bar = driver.find_element(By.ID, "search-reusables__filters-bar")
    filter_buttons = filter_bar.find_elements(
        By.TAG_NAME, "button")

    for button in filter_buttons:
        if button.text == EASY_APPLY:
            button.click()

    # Click to apply
    sleep(2)
    easy_apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
    easy_apply_button.click()

    # Enter phone, attach resume and submit application
    sleep(2)
    phone_number_input = driver.find_element(
        By.CLASS_NAME, "artdeco-text-input--input")
    phone_number_input.send_keys("074000000")

    job_resume_picker = driver.find_element(
        By.CLASS_NAME, "jobs-resume-picker__resume-btn-container")
    choose_resume = job_resume_picker.find_element(
        By.TAG_NAME, "button")
    choose_resume.click()
    sleep(1)

    footer = driver.find_element(
        By.TAG_NAME, "footer")
    submit_resume = footer.find_element(
        By.TAG_NAME, "button")
    submit_resume.click()

# If already applied to job or job is no longer accepting applications, then skip.
except NoSuchElementException:
    print("No application button, skipped.")
    # continue

sleep(5)
driver.quit()
