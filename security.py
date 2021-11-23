from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1,'jayy','jay')
]

username_mapping = {u.username:u for u in users}
uid_mapping ={u.username:u for u in users}

def auth(username,password):
    user = username_mapping.get(username,None)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    id =payload['identity']
    return uid_mapping.get(id,None)

# def auth(username,email):
#     user = username_mapping(username,None)
#     if user and safe_str_cmp(user.email,email):
#         return user

# def identity(payload):
#     id =identity['payload']
#     return uid_mapping(is,None)


# def authenticate(username, email):
#     # print(username,email)
#     users = User.find_by_username(username)
#     if users and safe_str_cmp(users.email, email):
#         return users

# def identity(payload):
#     user_email = payload['identity']
#     return User.find_by_id(user_email)



# from werkzeug.security import safe_str_cmp
# from user import User

# def authenticate(username, password):
#     user = User.find_by_username(username)
#     if user and safe_str_cmp(user.password, password):
#         return user

# def identity(payload):
#     user_id = payload['identity']
#     return User.find_by_id(user_id)