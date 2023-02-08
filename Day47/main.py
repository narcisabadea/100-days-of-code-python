import requests
from bs4 import BeautifulSoup
import smtplib

AMAZON_URL = "https://www.amazon.com/Instant-Pot-Electric-Sterilizer-Stainless/dp/B09MZTSSR2/ref=sr_1_1_sspa?keywords=Instant%2BPot%2BDuo%2BEvo%2BPlus&qid=1675868892&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMzJPOFVaWU5OQU8zJmVuY3J5cHRlZElkPUEwMzY3NDI0TzVOUzRGSFU0NlMzJmVuY3J5cHRlZEFkSWQ9QTA0NjgwMzYzNURPMDBZNkZQMlEmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1"
MY_EMAIL_GMAIL = "appbreweryinfo@gmail.com"
MY_EMAIL_YAHOO = "appbrewerytesting@yahoo.com"
MY_PASSWORD = "abcd1234()"
SMTP_INFO = "smtp.gmail.com"

PRICE_BUY = 130
headers = {
    "Accept-Language": "en-US,en;q=0.9,ro;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
response = requests.get(AMAZON_URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find(id="productTitle").getText().strip()
whole_price = soup.find(class_="a-price-whole").getText()
fractional_price = soup.find(class_="a-price-fraction").getText()
price = float(whole_price + fractional_price)

if price < PRICE_BUY:
    with smtplib.SMTP(SMTP_INFO) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL_GMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL_GMAIL,
                            to_addrs=MY_EMAIL_YAHOO, msj=f"Subject:Amazon price alert!\n\n{title} is now at the price of {price}!. See it here {AMAZON_URL}")
