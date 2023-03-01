# SQLAlchemy is defined as an ORM Object Relational Mapping library
# This means that it's able to map the relationships in the database into Objects
# Fields become Object properties
# Tables can be defined as separate Classes and each row of data is a new Object
# This will make more sense after we write some code and see how we can create a Database/Table/Row of data using SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CREATE DATABASE
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

with app.app_context():
    # CREATE TABLE
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.Float, nullable=False)

        def __repr__(self):
            return f'<Book {self.title}>'
            
    db.create_all()

    # CREATE RECORD
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
