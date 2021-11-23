# from flask import Flask, render_template, request, redirect, url_for, session
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import pymysql
# import re
# import mysql.connector
# import mysql

# app = Flask(__name__)
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="flaskapi"
# )

# mycursor = mydb.cursor()

# # mycursor.execute("CREATE DATABASE flaskapi")

# mycursor.execute("CREATE TABLE users(username VARCHAR(50), email VARCHAR(50), password VARCHAR(50))")

# mysql = MySQL(app)
# sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
# val = ("Rk", "Rk@gmail.com", "raj")
# mycursor.execute(sql,val)
# # mycursor.executemany(insert_query,users)
# for x in mycursor:
#   print(x)

# mydb.commit()
# mydb.close()


# mycursor.execute("SHOW TABLES")
# mycursor.execute("SHOW DATABASES")











# # import sqlite3
# # from sqlite3.dbapi2 import Cursor

# # connection = sqlite3.connect('data.db')

# # cursor =connection.cursor()
# # create_table="CREATE TABLE users(id int, username text,password text)"
# # cursor.execute(create_table)

# # user=(1,'ram','ram')
# # insert_query ="INSERT INTO users VALUES (?,?,?)"
# # cursor.execute(insert_query,user)
# # users=[
# #     (2,'rajkumar','rajkumar'),
# #     (3,'hitesh','hitesh')
# # ]
# # cursor.executemany(insert_query,users)

# # select_query="SELECT * FROM users"
# # for row in cursor.execute(select_query):
# #     print(row)

# # # connection.session.add(row)
# # connection.commit()
# # connection.close()

