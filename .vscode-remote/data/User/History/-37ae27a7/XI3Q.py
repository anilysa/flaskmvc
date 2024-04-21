import os
from flask import Flask, render_template, request, jsonify
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import csv

from App.database import init_db
from App.config import load_config
from App.controllers import setup_jwt, add_auth_context
from App.views import views, setup_admin

def add_views(app):
    for view in views:
        print(f"Adding {view} view to Blueprints")
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
        exercises = load_exercises_from_csv('dataset.csv')
        return render_template('temp.html', exercises=exercises)

    @app.route('/exercise/info/<int:exercise_id>', methods=['GET'])
    def get_exercise_info(exercise_id):
        exercise = Exercise.query.get(exercise_id)
        if exercise:
            return jsonify(exercise.get_exercise_info()), 200
        else:
            return jsonify({'error': 'Exercise not found'}), 404

    @app.route('/exercise/view', methods=['GET'])
    def display_exercises():
        exercises = Exercise.query.all()
        return render_template('exercises.html', exercises=exercises)

    def load_exercises_from_csv(file_path):
        exercises = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'name' in row:  # Check if 'name' key exists in the row
                    exercises.append(row)
                else:
                    print("Warning: 'name' key not found in a row. Skipping this row.")
        return exercises

    @app.route('/signup')
    def signup():
        return render_template('temp.html')

    @app.route('/workout')
    def workout():
        return render_template('workout.html')

    @app.route('/routine')
    def routine():
        return render_template('routine.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/logout')
    def logout():
        return render_template('login.html')

    @app.route('/view')
    def view():
        return render_template('routineview.html')

    @app.route('/add_exercise', methods=['POST'])
    def add_exercise():
        exercise = request.form['exercise']
        day = request.form['day']
        # Here you can add the exercise to the routine and render the new page
        return render_template('routineview.html', exercise=exercise, day=day)


    return app