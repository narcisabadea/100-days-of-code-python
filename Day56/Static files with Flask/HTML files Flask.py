from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    # file needs to be in the template folder
    return render_template("index.html")


@app.route('/cv')
def cv():
    # file needs to be in the template folder
    return render_template("cv/cv.html")


if __name__ == "__main__":
    app.run(debug=True)
