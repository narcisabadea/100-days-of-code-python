# Beautiful Soup is a Python library for pulling data out of HTML and XML files.

from bs4 import BeautifulSoup

with open("website.html") as website:
    content = website.read()
soup = BeautifulSoup(content, 'html.parser')
print(soup)
print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.a)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

name = soup.select_one(selector="#name")
print(name)
