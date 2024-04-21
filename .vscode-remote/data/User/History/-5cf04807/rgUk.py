from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
from App.models import Exercise

exercise_views = Blueprint('exercise_views', __name__, template_folder='../templates')


    # @app.route('/exercise/info/<int:exercise_id>', methods=['GET'])
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
        
    @app.route('/exercise/add', methods=['POST'])
    def add_exercise():
        exercise = request.form['exercise']
        day = request.form['day']
        # Here you can add the exercise to the routine and render the new page
        return render_template('routineview.html', exercise=exercise, day=day)

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
