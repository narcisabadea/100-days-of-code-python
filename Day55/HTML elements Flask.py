from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
            "<img src='https://media0.giphy.com/media/Y1esOcsGWK4emAoQDt/giphy.gif?cid=ecf05e47wbbiq17j8i6df2326qcca11m1ztpzn4kf4fx91gs&rid=giphy.gif&ct=g' width=200>"



@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello, there {name}, you are {number} years old!'


@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)
