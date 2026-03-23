from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html',books=all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == "POST":
        data = request.form
        all_books.append({"name": data["name"], "author":data["author"], "rating": data["rating"]})
        return render_template('add.html')


    return render_template('add.html' )


if __name__ == "__main__":
    app.run(debug=True)

