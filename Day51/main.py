from twitter_bot_model import InternetSpeedTwitterBot

chrome_driver_path = "/Users/narcisabadea/Desktop/Development/chromedriver"

new_bot = InternetSpeedTwitterBot(chrome_driver_path)
new_bot.get_internet_speed()
