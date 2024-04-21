from App.database import db
from flask_sqlalchemy import SQLAlchemy

class Workout(db.Model):
    __tablename__ = 'workouts'

    users = db.relationship('User', backref='workouts', lazy=True)
    exercises = db.relationship('Exercise', backref='workout', lazy=True)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
