from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize

import csv
from App.models import Exercise

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
            print("Title:", row['Title'])
            print("Desc:", row ['Desc'])
            print("Type:", row ['Type'])
            print("BP:", row ['BodyPart'])
            print("Equip:", row ['Equipment'])
            print("Level:", row ['Level'])
            print("Rating:", float(row['Rating']) if row['Rating'] else 'N/A')
            print("Rating Desc:", row ['RatingDesc'])
            print()
            exercises.append({
                "Title": row['Title'],
                "Desc": row['Desc'],
                "Type": row['Type'],
                "BodyPart": row['BodyPart'],
                "Equipment": row['Equipment'],
                "Level": row['Level'],
                "Rating": float(row['Rating']) if row['Rating'] else 'N/A',
                "RatingDesc": row['RatingDesc']
            })
    return jsonify(message="successfully initialised db", status=200)


@index_views.route('/init', methods=['GET'])
def init():
    process_csv()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})