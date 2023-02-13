# export FLASK_APP=file name
# flask run
# http://127.0.0.1:5000/

from flask import Flask
# Because we're creating this app from this Flask class and in order to initialize a new Flask application there is only one required input,
# and that is the import_name.
# which prints __main__ which is one of the special attributes that's built into Python.
app = Flask(__name__)

# you could tap into the name to find out what is the current class, function, method, or descriptor's name.
# And when we get main, what it's telling us is basically we're executing the code in a particular module.
# So that means it's run as a script or from an interactive prompt, but it's not run from an imported module.

print(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/bye")
def say_bye():
    return "Bye"


# we're running the code from within this current file.
if __name__ == "__main__":
    # does exactly the same thing as when we went into the terminal and say flask run.
    app.run()
