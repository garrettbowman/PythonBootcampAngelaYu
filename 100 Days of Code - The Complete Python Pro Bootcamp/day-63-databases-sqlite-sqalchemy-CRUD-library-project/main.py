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

app = Flask(__name__)
##CREATE DATABASE
class Base(DeclarativeBase):
    pass


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection2.db"
# initialize the app with the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str]= mapped_column(String(250), nullable=False)
    rating: Mapped[float]= mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD

# with app.app_context():
#     new_book = Book(title="Harry Potter and", author="J. K. Rowling", rating=3.4)
#     db.session.add(new_book)
#     db.session.commit()

all_booksQ = []


@app.route('/', methods=['GET','POST'])
def home():
    # if request.method == "POST":
    #     data = request.form
    #     with app.app_context():
    #         book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    #         # or book_to_update = db.get_or_404(Book, book_id)
    #         book_to_update.rating = data["rating"]
    #         db.session.commit()

    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
        print(all_books)
    return render_template('index.html',books=all_books)


@app.route('/<int:id>', methods=['GET','POST'])
def home2(id):
    if request.method == "POST":
        data = request.form
        with app.app_context():
            # book_to_update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
            book_to_update = db.get_or_404(Book, id)
            book_to_update.rating = data["rating"]
            db.session.commit()

    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
        print(all_books)
    return render_template('index.html', books=all_books)







@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == "POST":
        data = request.form
        # all_booksQ.append({"title": data["title"], "author":data["author"], "rating": data["rating"]})
        with app.app_context():
            new_book = Book(title=data["title"], author=data["author"], rating=data["rating"])
            db.session.add(new_book)
            db.session.commit()

        return render_template('add.html')

    return render_template('add.html' )

@app.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    if request.method == "GET":
        data = request.form
        with app.app_context():
            ebook = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
            return render_template('edit.html', book=ebook)

    if request.method == "POST":
        data = request.form
        with app.app_context():
            # book_to_update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
            book_to_update = db.get_or_404(Book, id)
            book_to_update.rating = data["rating"]
            db.session.commit()
            return render_template('index.html')
    return render_template('edit.html')

@app.route("/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    with app.app_context():
        # book_to_delete = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        book_to_delete = db.get_or_404(Book, id)
        db.session.delete(book_to_delete)
        db.session.commit()

    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
        print(all_books)

    return render_template('index.html', books=all_books)

if __name__ == "__main__":
    app.run(debug=True)

