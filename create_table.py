# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="flaskapi"

# )

# mycursor = mydb.cursor()
# # mycursor.execute("CREATE DATABASE flaskapi")

# mycursor.execute("CREATE TABLE users(ID int NOT NULL PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), email VARCHAR(50), password VARCHAR(50))")

# sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
# val = ("Rk", "Rk@gmail.com", "raj")
# mycursor.execute(sql, val)
# for x in mycursor:
#   print(x)

# mydb.commit()
# mydb.close()
# # mycursor.execute("SHOW TABLES")
# # mycursor.execute("SHOW DATABASES")

# # print(mycursor.rowcount, "record inserted.")










# # import sqlite3
# # # from sqlite3.dbapi2 import Cursor
# # # from typing import Collection

# # connection = sqlite3.connect('data.db')
# # cursor = connection.cursor()

# # create_table ="CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text,password text)"
# # cursor.execute(create_table)


# # connection.commit()

# # connection.close()
 
# # from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy

# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# # db = SQLAlchemy(app)


# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(80), unique=True, nullable=False)
# #     email = db.Column(db.String(120), unique=True, nullable=False)

# #     def __repr__(self):
# #         return '<User %r>' % self.username1