from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


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