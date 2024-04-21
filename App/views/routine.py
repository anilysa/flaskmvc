from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
from App.models import Exercise

routine_views = Blueprint('routie_views', __name__, template_folder='../templates')


 @app.route('/routine')
    def get_routines():
        return render_template('routine.html')

    @app.route('/routine/view/<int:routine_id>')
    def view_routine(routine_id):
        return render_template('routineview.html')