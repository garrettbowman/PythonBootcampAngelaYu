from flask import Flask, render_template
import random
import datetime
import requests
blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
app = Flask(__name__)

blog_resp = requests.get(blog_url)
blog = blog_resp.json()


@app.route('/')
def home():
    posts = blog
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():

    return render_template("about.html")


@app.route('/post/<int:num>')
def post(num):
    return render_template("post.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)