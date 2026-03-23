from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv
import requests


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location  = StringField('Location Google Maps link', validators=[DataRequired()])
    open = StringField('Open e.g. 8AM', validators=[DataRequired()])
    close = StringField('Close e.g. 5PM', validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=[("☕️","☕️"), ("☕️☕️","☕️☕️"),("☕️☕☕️","☕️☕️☕️"),("☕️☕️☕️☕️","☕️☕️☕️☕️")], validators=[DataRequired()])
    wifi = SelectField('Wifi', choices=[("✘","✘"), ("💪","💪"),("💪💪","💪💪"),("💪💪💪","💪💪💪")],validators=[DataRequired()])
    power = SelectField('Power', choices=[("✘","✘"), ("🔌","🔌"),("🔌🔌","🔌🔌"),("🔌🔌🔌","🔌🔌🔌")],validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods= ["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        location = form.location.data
        opening = form.open.data
        close = form.close.data
        coffee = form.coffee.data
        wifi = form.wifi.data
        power = form.power.data
        add_to_file(cafe_name,location,opening,close,coffee,wifi,power)
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()

    return render_template('add.html', form=form)

def add_to_file(cafe_name, location, opening, close, coffee, wifi, power):
    with open("cafe-data.csv", "a", encoding='utf-8') as f:
        f.write(f"\n{cafe_name},{location},{opening},{close},{coffee},{wifi},{power}")


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
