### CRUD Operations with SQLAlchemy

## Create a New Database

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///<name of database>.db"
db = SQLAlchemy(app)
```

## Create a New Table

```python
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False

db.create_all()
```

In addition to these things, the most crucial thing to figure out when working with any new database technology is how to CRUD data records.

- Create
- Read
- Update
- Delete

So, let's go through each of these using SQLite and SQLAlchemy:

## Create A New Record

```python
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()
```

NOTE: When creating new records, the primary key fields is optional. you can also write:

```python
new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
```

the id field will be auto-generated.

## Read All Records

```python
all_books = session.query(Book).all()
```

## Read A Particular Record By Query

```python
book = Book.query.filter_by(title="Harry Potter").first()
```

## Update A Particular Record By Query

```python
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()
```

## Update A Record By PRIMARY KEY

```python
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()
```

## Delete A Particular Record By PRIMARY KEY

```python
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
```

You can also delete by querying for a particular value e.g. by title or one of the other properties.
