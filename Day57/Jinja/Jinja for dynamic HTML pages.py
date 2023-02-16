# Jinja is a fast, expressive, extensible templating engine.
# Special placeholders in the template allow writing code similar to Python syntax.
# Then the template is passed data to render the final document.

from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(0, 10)
    current_year = date.today().year
    return render_template("index.html", num=random_number, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
