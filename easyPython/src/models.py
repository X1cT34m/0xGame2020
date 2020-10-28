
from flask_login import UserMixin

class User(UserMixin):
    pass

users = [
    {'id':'admin', 'username': 'admin', 'password': '123456'},
    {'id':'Tom', 'username': 'Tom', 'password': '123456'}
]

def query_user(id):
    for user in users:
        if id == user['id']:
            return user