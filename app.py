from typing import Text
from flask import Flask, request ,render_template, session, sessions
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
# from create_table import mydb
from security import auth, identity
from user import Update, UserRegister
# from test import mydb
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

mysql = MySQL(app)
jwt = JWT(app, auth, identity)

allname = []
import mysql.connector
connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="flaskapi")
class User(Resource):      
    # @ jwt_required
    def delete(self, email,password):
        # if ("SELECT * FROM users WHERE email=%s AND password=%s",(email,password)):
            c=connection.cursor()
            c.execute("DELETE FROM users WHERE email=%s AND password=%s",(email,password))
            msg="User data delete.."
            # record = c.fetchone()
            # if record !=0:  
            connection.commit()
            return (msg)
        # else:
        #     return ("Not Deleted")

class Login(Resource):
   def get(self,email,password):
     
     c=connection.cursor()
     c.execute("SELECT * FROM users WHERE email=%s AND password=%s",(email,password))
  
     record = c.fetchone()
     all=[]
     print(record)
     if record:
        # session['email']= True
        # session['password']=True

        record = {
                    'username':record[0],
                    'email':record[1],
                    'password':record[2],
                    }
        all.append(record)
        return {'USERS' : all}
     else :
           return("Incorrect username or password. try again!")


class Forgot(Resource):
    parser =reqparse.RequestParser()
    parser.add_argument('password',
    type=str,
    required=True,
    help="This field can't be blank.."
  )
    parser.add_argument('email',
    type=str,
    required=True,
    help="This field can't be blank.."
  )

    @jwt_required()  
    def put(self,email):
        data=Forgot.parser.parse_args()
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="flaskapi")
        c=connection.cursor()
        c.execute("SELECT email FROM users WHERE email=%s",(email,))
        
        record = c.fetchone()  
        print(record)
        if record !=0:
         query= ("UPDATE users SET password=%s where email=%s ")
         val =(data['password'],data['email'])
         c.execute(query,val)

         connection.commit()
         connection.close()
         return{"message": "User Update successfully.."},201



class UserList(Resource):
    def get(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="flaskapi")
        
        query="SELECT * from users"
        c=connection.cursor()
        c.execute(query)
        records = c.fetchall()
        all=[]
        for allname in records:
            obj = {'username':allname[0],
                    'email':allname[1]}
            all.append(obj)
        return {'USERS' : all}
          

api.add_resource(User, '/user/<string:email>/<string:password>')
api.add_resource(UserList, '/allname')
api.add_resource(Forgot, '/forgot/<string:email>')
api.add_resource(Login, '/login/<string:email>/<string:password>')
api.add_resource(UserRegister, '/register')
api.add_resource(Update, '/update/<string:email>/<string:password>')
if __name__ == '__main__':
    app.run(debug=True) 
  









# from os import name
# from typing import Text
# from flask import Flask, request
# from flask_restful import Resource, Api, reqparse
# from flask_jwt import JWT, jwt_required, current_identity
# # from create_table import connection
# from security import authenticate, identity
# from user import UserRegister
# # from test import connection

# app = Flask(__name__)
# app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
# app.secret_key = 'jose'
# api = Api(app)

# jwt = JWT(app, authenticate, identity)

# allname = []

# class User(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('email',
#         type=Text,
#         required=True,
#         help="This field cannot be left blank!"
#     )

#     parser.add_argument('password',
#         type=Text,
#         required=True,
#         help="This field cannot be left blank!"
#     )

#     # @jwt_required()

#     def post(self, name):
#         if next(filter(lambda x: x['name'] == name, allname), None) is not None:
#             return {'message': "An User with this name '{}' already exists.".format(name)}

#         data = User.parser.parse_args()

#         user = {'name': name, 'email': data['email'], 'password':data['password']}
#         allname.append(user)
#         # return user,201
#         return "User registeration seccessfuly",201

#     @jwt_required()
#     def delete(self, name):
#         global allname
#         allname = list(filter(lambda x: x['name'] != name,allname))
#         return {'message': 'User deleted'}

#     @jwt_required()
#     def put(self, name):
#         data = User.parser.parse_args()
#         # Once again, print something not in the args to verify everything works
#         user = next(filter(lambda x: x['name'] == name, allname), None)
#         if user is None:
#             user = {'name': name, 'email': data['email'], 'password':data['password']}
#             allname.append(user)
#         else:
#             user.update(data)
#         return user

# class Forgot(Resource):
#     @jwt_required()
#     def put(self, email):
#       if next(filter(lambda x: x['email'] != email, allname), None) is not None:
#         return {'message': "An User with this email '{}' isn't exists.".format(email)}
#       else:
#         data = User.parser.parse_args()
#         # Once again, print something not in the args to verify everything works
#         user = next(filter(lambda x: x['email'] == email, allname), None)
#         if user is None:
#             user = {'email': data['email'], 'password':data['password']}
#             allname.append(user)
#         else:
#             user.update(data)
#         return "Update successfully"


# class Login(Resource):
#    def get(self, name,email,password):
#      if   next(filter(lambda x: x['name'] == name, allname), None):
#         if next(filter(lambda x: x['email'] == email, allname), None) is not None:
#            if  next(filter(lambda x: x['password'] == password, allname), None) is not None:
#             #  return {'message': "An User with this email '{}' isn't exists.".format(email)}
#             user= next(filter(lambda x: x['name'] == name, allname), None)
#             return {'user':user},200 if user else 404
           
#             # return  '{} {} {}'.format(firstname, lastname, cellphone)
#            else:
#                 return"Password is incorrect.."      
#         else:
#              return"email is incorrect.."   
#      else:
#           return"name is incorrect.."

# class Update(Resource):
#  @jwt_required()
#  def put(self, email):
#       if next(filter(lambda x: x['email'] != email, allname), None) is not None:
#         return {'message': "An User with this email '{}' isn't exists.".format(email)}
#       else:
#         data = User.parser.parse_args()
#         # Once again, print something not in the args to verify everything works
#         user = next(filter(lambda x: x['name'] == name, allname), None)
#         if user is None:
#             user = {'name': data['name'], 'password':data['password']}
#             allname.append(user)
#         else:
#             user.update(data)
#         return "Update successfully"

# class UserList(Resource):
#     def get(self):
#         return {'USERS': allname}

# api.add_resource(User, '/user/<string:name>')
# api.add_resource(UserList, '/allname')
# api.add_resource(Forgot, '/forgot/<string:email>')
# api.add_resource(Login, '/login/<string:name>/<string:email>/<string:password>')
# api.add_resource(Update, '/update/<string:email>')
# # api.add_resource(index.html, '/allname')
# api.add_resource(UserRegister, '/register')

# if __name__ == '__main__':
#     app.run(debug=True) 
  