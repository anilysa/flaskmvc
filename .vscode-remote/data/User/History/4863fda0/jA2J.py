from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
from App.models import Workout

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')


@app.route('/workout')
def workout():
    return render_template('workout.html')


@app.route('/workout/view/<int:user_id>', methods=['GET'])
    def view_workout(user_id):
        return render_template('workout.html')