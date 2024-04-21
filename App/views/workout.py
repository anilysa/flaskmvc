from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
from App.models import Workout

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')


