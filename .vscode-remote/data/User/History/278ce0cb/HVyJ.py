from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize

import csv
from App.database import db
from App.models import Exercise

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

def process_csv():
    dataset_file = 'dataset.csv'  # Modify this line to specify the path to your dataset
    exercises = []
    max_rating = 0
    with open(dataset_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_exercise = Exercise(
                row['Title'] if row['Title'] else 'N/A',
                row['Desc'] if row['Desc'] else 'N/A',
                row['Type'] if row['Type'] else 'N/A',
                row['BodyPart'] if row['BodyPart'] else 'N/A',
                row['Equipment'] if row['Equipment'] else 'N/A',
                row['Level'] if row['Level'] else 'N/A',
                float(row['Rating']) if row['Rating'] else 'N/A',
                row['RatingDesc'] if row['RatingDesc'] else 'N/A'
            )
            if new_exercise.Rating > max_rating:
                max_rating = new_exercise.Rating
            exercises.append(new_exercise)
            db.session.add(new_exercise)
    
    db.session.commit()
    print("Maximum rating:", max_rating)
    
    return exercises

@index_views.route('/init', methods=['GET'])
def init():
    exercises = process_csv()
    return jsonify(message=f'Data initialised with {len(exercises)} exercises', status=200)

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})