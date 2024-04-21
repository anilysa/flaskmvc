from App.models import Exercise
from App.database import db


def get_exercise(id):
    return Exercise.query.get(id)

def get_all_exercises():
    return Exercise.query.all()