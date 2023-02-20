from instagram_bot_model import InstaFollower

chrome_driver_path = "/Users/narcisabadea/Desktop/Development/chromedriver"

new_bot = InstaFollower(chrome_driver_path)
new_bot.find_followers()