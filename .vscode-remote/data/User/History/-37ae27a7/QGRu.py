import os
from flask import Flask, render_template, request, jsonify
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import csv

from App.database import init_db
from App.config import load_config
from App.controllers import setup_jwt, add_auth_context, get_all_exercises
from App.views import views, setup_admin

def add_views(app):
    for view in views:
        app.register_blueprint(view)

def process_csv():
    dataset_file = 'dataset.csv'  # Modify this line to specify the path to your dataset
    exercises = []
    with open(dataset_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            exercises.append({
                "Title": row['Title'],
                "Desc": row['Desc'],
                "Type": row['Type'],
                "BodyPart": row['BodyPart'],
                "Equipment": row['Equipment'],
                "Level": row['Level'],
                "Rating": float(row['Rating']),
                "RatingDesc": row['RatingDesc']
            })
    return exercises

def create_app(overrides={}):
    app = Flask(__name__, static_url_path='/static')
    load_config(app, overrides)
    CORS(app)
    add_auth_context(app)
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app)
    init_db(app)
    jwt = setup_jwt(app)
    setup_admin(app)

    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def custom_unauthorized_response(error):
        return render_template('401.html', error=error), 401

    app.app_context().push()

    @app.route('/temp')
    def temp():
        exercises = get_all_exercises()
        return render_template('temp.html', exercises=exercises)

    
    

   



    return app