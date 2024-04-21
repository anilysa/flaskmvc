from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
from App.models import Exercise

exercise_views = Blueprint('exercise_views', __name__, template_folder='../templates')


