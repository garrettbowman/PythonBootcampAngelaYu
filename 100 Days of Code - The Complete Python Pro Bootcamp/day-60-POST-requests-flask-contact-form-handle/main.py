from flask import Flask, render_template,request
import requests

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
# posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def receive_data():
    name = request.form['username']
    password = request.form['password']
    return f"<h1>name:{name}password:{password}</h1>"



if __name__ == "__main__":
    app.run(debug=True, port=5001)
