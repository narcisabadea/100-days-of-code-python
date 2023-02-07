# https://news.ycombinator.com/robots.txt

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)

site_title = soup.title
titles = soup.find_all(class_="titleline")

score = soup.find_all(class_="score")

for title in titles:
    print(title.getText())

for sc in score:
    print(sc.getText())
