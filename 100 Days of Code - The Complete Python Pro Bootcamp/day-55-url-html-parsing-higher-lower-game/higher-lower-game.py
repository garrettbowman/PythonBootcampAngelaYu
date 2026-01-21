from flask import Flask
import random

app = Flask(__name__)
number = random.randint(1, 10)
def make_bold(func):
    def wrapper():

        text = func()

        return f"<b>{text}</b>"
    return wrapper



@app.route("/")
def hello_world():
    return ("<h1 style = 'text-align:center'>Hello, World!</h1>"
            "<p>this is a test</p>"
            "<img src='https://static.stacker.com/s3fs-public/styles/sar_screen_maximum_large/s3/24281LV_30.png' width=200>")



# @app.route("/bye")
# def bye():
#     return ("<u><em><b>bye!</b></em></u>"
#
@app.route("/bye")
@make_bold
def bye():
    return "bye!"

# @app.route("/username/<name>")
# def say_greeting(name):
#     return f"Hello, {name}"

@app.route("/<int:num>")
def checknum(num):
    if num == number:

        return f"You got it, the number was {num}!"

    elif  num > number:
        return f"too high"

    else:
        return f"too low"


if __name__ == "__main__":
    app.run(debug=True)


checknum()