import requests
from twilio.rest import Client
from configparser import ConfigParser

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def _get_api_key():
    config = ConfigParser()
    config.read("../secrets.ini")
    keys = {
        "twilio":  config["twilio"],
        "stock": config["stock"],
        "news": config["news"]
    }
    return keys


keys = _get_api_key()

VIRTUAL_TWILIO_NUMBER = keys["twilio"]["VIRTUAL_TWILIO_NUMBER"]
VERIFIED_NUMBER = keys["twilio"]["VERIFIED_NUMBER"]
TWILIO_SID = keys["twilio"]["TWILIO_SID"]
TWILIO_AUTH_TOKEN = keys["twilio"]["TWILIO_SID"]
STOCK_API_KEY = keys["stock"]["STOCK_API_KEY"]
NEWS_API_KEY = keys["news"]["NEWS_API_KEY"]


stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}


# Calling the stock endpoint
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# Getting yesterday's closing stock price
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"Yesterday's closing price was: {yesterday_closing_price}")

# Getting the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(
    f"The day before yesterday the closing price was: {day_before_yesterday_closing_price}")

# Getting the difference between the 2 days
difference = float(yesterday_closing_price) - \
    float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Getting the difference in percentage
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(
    f"The difference is {difference} ({diff_percent}%), so we have {up_down}")

# If difference percentage is greater than 5 then get news articles and send some info to your phone by using twilio
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    # Send a message with each article's title and description to your phone.

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
