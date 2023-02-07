from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(class_="listicle-item")

with open("100Movies.txt", mode='w') as write_file:
    for index, title in enumerate(titles[::-1]):
        count = index + 1
        name = title.find(name="img")["alt"]
        movie = f"{count}) {name} \n"
        write_file.write(movie)
