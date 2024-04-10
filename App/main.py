import os
from flask import Flask, render_template
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

from App.database import init_db
from App.config import load_config

from App.controllers import (
    setup_jwt,
    add_auth_context
)

from App.views import views

def add_views(app):
    for view in views:
        app.register_blueprint(view)

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
    
    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def custom_unauthorized_response(error):
        return render_template('401.html', error=error), 401
    
    app.app_context().push()
    return app

# @app.route('/')
# def index():
#     form = SignUpForm()
#     return render_template('signup.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle sign-up form submission
        email = request.form['email']
        password = request.form['password']
        # Add user to database or perform other sign-up logic
        flash('Sign-up successful!')
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        email = request.form['email']
        password = request.form['password']
        # Authenticate user and set session cookie
        flash('Login successful!')
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/routines')
def workout_routines():
    routines = WorkoutRoutine.query.all()
    return render_template('workout_routine.html', routines=routines)

@app.route('/routines/<int:routine_id>/edit')
def edit_routine(routine_id):
    routine = WorkoutRoutine.query.get_or_404(routine_id)
    return render_template('edit_routine.html', routine=routine)

@app.route('/routines/<int:routine_id>/delete', methods=['POST'])
def delete_routine(routine_id):
    routine = WorkoutRoutine.query.get_or_404(routine_id)
    db.session.delete(routine)
    db.session.commit()
    flash('Routine deleted successfully.', 'success')
    return redirect(url_for('workout_routines'))
