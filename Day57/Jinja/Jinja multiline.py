from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)

all_posts = [
    {
        "id": 1,
        "title": "The Life of Cactus",
        "subtitle": "Who knew that cacti lived such interesting lives.",
        "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify."
    },
    {
        "id": 2,
        "title": "Top 15 Things to do When You are Bored",
        "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities.",
        "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today."
    },
    {
        "id": 3,
        "title": "Introduction to Intermittent Fasting",
        "subtitle": "Learn about the newest health craze.",
        "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake."
    }
]


@app.route('/')
def home():
    random_number = random.randint(0, 10)
    current_year = date.today().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    genderize_reponse = requests.get(f"https://api.genderize.io?name={name}")
    get_gender = genderize_reponse.json()
    agefy_reponse = requests.get(f"https://api.agify.io?name={name}")
    get_age = agefy_reponse.json()
    return render_template("guess.html", name=name, gender=get_gender["gender"], age=get_age["age"])


@app.route('/blog/<num>')
def get_blog(num):
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
