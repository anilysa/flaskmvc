from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize

import csv
from App.models import db, Exercise

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

def process_csv():
    dataset_file = 'dataset.csv'  # Modify this line to specify the path to your dataset
    exercises = []
    with open(dataset_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_exercise = Exercise(
                "Title": row['Title'] if row['Title'] else 'N/A',
                "Desc": row['Desc'] if row['Desc'] else 'N/A',
                "Type": row['Type'] if row['Type'] else 'N/A',
                "BodyPart": row['BodyPart'] if row['BodyPart'] else 'N/A',
                "Equipment": row['Equipment'] if row['Equipment'] else 'N/A',
                "Level": row['Level'] if row['Level'] else 'N/A',
                "Rating": float(row['Rating']) if row['Rating'] else 'N/A',
                "RatingDesc": row['RatingDesc'] if row['RatingDesc'] else 'N/A'
            )
            exercises.append(
    return exercises

@index_views.route('/init', methods=['GET'])
def init():
    exercises = process_csv()
    return jsonify(message=f'Data initialised with {len(exercises)} exercises', status=200)

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})