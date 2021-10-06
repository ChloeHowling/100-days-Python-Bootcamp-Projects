from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrap_func():
        return f"<b>{function()}</b>"
    return wrap_func


def make_emphasis(function):
    def wrap_func():
        return f"<em>{function()}</em>"
    return wrap_func


def make_underline(function):
    def wrap_func():
        return f"<u>{function()}</u>"
    return wrap_func

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
@make_underline
@make_emphasis
def say_bye():
    return "Bye!"


@app.route('/Hi')
def say_hi():
    return "Hi"


@app.route('/username/<name>')
def greet(name):
    return f"<h1 style='text-align: center'>Hello {name}! Welcome!</h1>" \
           f"<p>This is a paragraph</p>" \
           f"<img src='https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif' width=200>"

# export


if __name__ == "__main__":
    app.run(debug=True)
