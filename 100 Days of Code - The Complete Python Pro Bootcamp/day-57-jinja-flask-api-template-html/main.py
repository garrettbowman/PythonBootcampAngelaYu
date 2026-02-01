from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_n = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html",num=random_n,year=year)


@app.route('/guess/<string:name>')
def naming(name):
    name = name.capitalize()
    gender1 = requests.get(f"https://api.genderize.io?name={name}")
    gender = gender1.json()
    age1 = requests.get(f"https://api.agify.io?name={name}")
    age = age1.json()


    return render_template("nameguess.html",name=name,gender=gender["gender"],age=age["age"])
@app.route('/blog/<num>')
def blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogg = response.json()


    return render_template("blog.html",posts=blogg)

if __name__ == "__main__":
    app.run(debug=True)


