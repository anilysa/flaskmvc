from App.models import User
from App.database import db



def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()