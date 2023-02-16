from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
