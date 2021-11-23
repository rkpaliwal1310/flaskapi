import mysql.connector
import mysql
from  flask_restful import Resource,reqparse
from flask import request, session
from flask_jwt import JWT, jwt_required, current_identity

class User():
    def __init__(self,id, username,password):
        self.id=id
        self.username = username
        self.password = password
        # self.password = password
    # @classmethod
    # def find_by_username(cls,username):
    #     # connection = mysql.connector.connect('flaskapi')
    #  connection = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="root",
    #         database="flaskapi")
    #  cursor = connection.cursor()

    #  query = f"SELECT username FROM users WHERE username=%s ",(username)
    #  result=cursor.execute(query,(username,))
    #  row=result.fetchone()
    #  if row :
    #         user = cls(*row)
    #  else:
    #         user = None
    #  connection.close()
    #  return user

    # @classmethod
    # def find_by_id(cls,email):
    #    connection = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="root",
    #         database="flaskapi")
    #    cursor = connection.cursor()

    #    query = "SELECT email FROM users WHERE email=%s ",(email)
    #    result=cursor.execute(query,(email,))
    #    row=result.fetchone()
    #    if row :
    #         user = cls(*row)
    #    else:
    #         user = None
    #    connection.close()
    #    return user   


class UserRegister(Resource):

    parser =reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help="This field can't be blank.."
  )
    # parser =reqparse.RequestParser()
    parser.add_argument('email',
    type=str,
    required=True,
    help="This field can't be blank.."
  )
    # parser =reqparse.RequestParser()
    parser.add_argument('password',
    type=str,
    required=True,
    help="This field can't be blank.."
  )

    def post(self):
        data=UserRegister.parser.parse_args()
        
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="flaskapi")
        c=connection.cursor()
        query= f"INSERT INTO users (username,email,password) VALUES (%s,%s,%s)"
        val =(data['username'],data['email'],data['password'])
        c.execute(query,val)
        

        connection.commit()
        connection.close()

        return{"message": "User create successfully.."},201


class Update(Resource):

    parser =reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help="This field can't be blank.."
  )
    # parser =reqparse.RequestParser()
    parser.add_argument('email',
    type=str,
    required=True,
    help="This field can't be blank.."
  )
    # parser =reqparse.RequestParser()
    parser.add_argument('password',
    type=str,
    required=True,
    help="This field can't be blank.."
  )

  
    def post(self,email,password):
        data=Update.parser.parse_args()
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="flaskapi")
        c=connection.cursor()
        c.execute("SELECT email,password FROM users WHERE email=%s AND password=%s",(email,password))
    
        record = c.fetchone()  
        print(record)
        if record !=0:
         query= ("UPDATE users SET username=%s ,email=%s where password=%s ")
         val =(data['username'],data['email'],data['password'])
         c.execute(query,val)
    
        #  query= ("UPDATE users SET username=%s ,email=%s password=%s  WHERE id=%s")
        #  val =(data['username'],data['email'],data['password'],session['id'])
      
         connection.commit()
         connection.close()
         return{"message": "User Update successfully.."},201

        else:
          print("Please enter valid email and password")





# import sqlite3
# from sqlite3.dbapi2 import Connection, Cursor
# from  flask_restful import Resource,reqparse
# class User():
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password

#     @classmethod
#     def find_by_username(cls,username):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()

#         query = "SELECT * FROM users WHERE username=?"
#         result=cursor.execute(query,(username,))
#         row=result.fetchone()
#         if row :
#             user = cls(*row)

#         else:
#             user = None

#         connection.close()
#         return user

#     @classmethod
#     def find_by_id(cls,id):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()

#         query = "SELECT * FROM users WHERE id=?"
#         result=cursor.execute(query,(id,))
#         row=result.fetchone()
#         if row :
#             user = cls(*row)

#         else:
#             user = None

#         connection.close()
#         return user   