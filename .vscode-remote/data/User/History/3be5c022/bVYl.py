from App.models import User
from App.database import db



def get_(id):
    return User.query.get(id)

def get_all_s():
    return User.query.all()