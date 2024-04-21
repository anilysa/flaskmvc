from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    workouts = db.relationship('Workout', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        """Create hashed password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    exercises = db.relationship('Exercise', backref='workout', lazy=True)

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(120), nullable=False)  # Maps to 'Title' column
    Desc = db.Column(db.Text, nullable=False)  # Maps to 'Desc' column
    Type = db.Column(db.String(80), nullable=False)  # Maps to 'Type' column
    BodyPart = db.Column(db.String(80), nullable=False)  # Maps to 'BodyPart' column
    Equipment = db.Column(db.String(80), nullable=False)  # Maps to 'Equipment' column
    Level = db.Column(db.String(80), nullable=False)  # Maps to 'Level' column
    Rating = db.Column(db.Float, nullable=False)  # Maps to 'Rating' column
    RatingDesc = db.Column(db.Text, nullable=False)  # Maps to 'RatingDesc' column

    def get_exercise_info(self):
        return {
            "Title": self.Title,
            "Desc": self.Desc,
            "Type": self.Type,
            "BodyPart": self.BodyPart,
            "Equipment": self.Equipment,
            "Level": self.Level,
            "Rating": self.Rating,
            "RatingDesc": self.RatingDesc
        }
