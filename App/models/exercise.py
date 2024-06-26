from App.database import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(120), nullable=False)  # Maps to 'Title' column
    Desc = db.Column(db.Text, nullable=False)  # Maps to 'Desc' column
    Type = db.Column(db.String(80), nullable=False)  # Maps to 'Type' column
    BodyPart = db.Column(db.String(80), nullable=False)  # Maps to 'BodyPart' column
    Equipment = db.Column(db.String(80), nullable=False)  # Maps to 'Equipment' column
    Level = db.Column(db.String(80), nullable=False)  # Maps to 'Level' column
    Rating = db.Column(db.String(4), nullable=False)  # Maps to 'Rating' column
    RatingDesc = db.Column(db.Text, nullable=False)  # Maps to 'RatingDesc' column


    def __init__(self, title, desc, _type, bodypart, equipment, level, rating, rating_desc):
        self.Title = title
        self.Desc = desc
        self.Type = _type
        self.BodyPart = bodypart
        self.Equipment = equipment
        self.Level = level
        self.Rating = rating
        self.RatingDesc = rating_desc

    def get_json(self):
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