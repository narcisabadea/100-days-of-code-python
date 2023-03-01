# the most used database in the world is SQLite, included by default in all Python installations
import sqlite3

# create a connection to a new database (if the database does not exist then it will be created)
db = sqlite3.connect("books-collection.db")

# we need to create a cursor(pointer) which will control our database.

cursor = db.cursor()
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor - this is the mouse pointer in our database that is going to do all the work
# .execute() - this method will tell the cursor to execute an action. All actions in SQLite databases are expressed as SQL (Structured Query Language) commands
# CREATE TABLE -  this will create a new table in the database. The name of the table comes after this keyword
# books -  this is the name that we've given the new table we're creating
# () -  the parts that come inside the parenthesis after CREATE TABLE books ( ) are going to be the fields in this table
# id INTEGER PRIMARY KEY -  this is the first field, it's a field called "id" which is of data type INTEGER and it will be the PRIMARY KEY for this table. The primary key is the one piece of data that will uniquely identify this record in the table
# title varchar(250) NOT NULL UNIQUE -  this is the second field, it's called "title" and it accepts a variable-length string composed of characters. The 250 in brackets is the maximum length of the text. NOT NULL means it must have a value and cannot be left empty. UNIQUE means no two records in this table can have the same title
#  author varchar(250) NOT NULL -  a field that accepts variable-length Strings up to 250 characters called author that cannot be left empty
# rating FLOAT NOT NULL -  a field that accepts FLOAT data type numbers, cannot be empty and the field is called rating

# open DB using https://sqlitebrowser.org/dl/

# create a new entry in our books table for the Harry Potter book and commit the changes to our database.
cursor.execute(
    "INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
