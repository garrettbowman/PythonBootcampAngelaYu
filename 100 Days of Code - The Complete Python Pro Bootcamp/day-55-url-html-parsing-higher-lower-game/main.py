from flask import Flask

app = Flask(__name__)




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
@make_emphasis
@make_underlined
def bye():
    return "bye!"

# @app.route("/username/<name>")
# def say_greeting(name):
#     return f"Hello, {name}"

@app.route("/username/<path:name>")
def say_greeting(name):
    return f"Hello, {name}"


if __name__ == "__main__":
    app.run(debug=True)

say_greeting()