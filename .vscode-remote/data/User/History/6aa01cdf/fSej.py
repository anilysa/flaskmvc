from App.database import db
from flask_sqlalchemy import SQLAlchemy

class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    _type = db.Column(db.String(80), nullable=False)
    body_part = db.Column(db.String(80), nullable=False)
    equipment = db.Column(db.String(80), nullable=False)
    level = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.String(4), nullable=False)
    rating_desc = db.Column(db.Text, nullable=False)

    def __init__(self, title, desc, _type, body_part, equipment, level, rating, rating_desc):
        self.title = title
        self.desc = desc
        self._type = _type
        self.body_part = body_part
        self.equipment = equipment
        self.level = level
        self.rating = rating
        self.rating_desc = rating_desc

    def get_json(self):
        return {
            "title": self.title,
            "desc": self.desc,
            "type": self._type,
            "body_part": self.body_part,
            "equipment": self.equipment,
            "level": self.level,
            "rating": self.rating,
            "rating_desc": self.rating_desc
        }
