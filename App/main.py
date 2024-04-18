import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from App.database import init_db
from App.config import load_config

from App.controllers import (
    setup_jwt,
    add_auth_context
)

from App.views import views

# # Configure Flask App
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'MySecretKey'
# app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token'
# app.config['JWT_REFRESH_COOKIE_NAME'] = 'refresh_token'
# app.config["JWT_TOKEN_LOCATION"] = ["cookies", "headers"]
# app.config["JWT_COOKIE_SECURE"] = True
# app.config["JWT_SECRET_KEY"] = "super-secret"
# app.config["JWT_COOKIE_CSRF_PROTECT"] = False
# app.config['JWT_HEADER_TYPE'] = ""
# app.config['JWT_HEADER_NAME'] = "Cookie"


# # Initialize App 
# db.init_app(app)
# app.app_context().push()
# CORS(app)
# jwt = JWTManager(app)

# #configure flask app
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://plannerdb_049p_user:Krn1KBahuPdvkEidAZDf05fEUgzxLRDd@dpg-co8v3420si5c739402fg-a/plannerdb_049p'
# db = SQLAlchemy(app)

# app.config['secret key'] = 'secret key'

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

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/temp')
    def temp():
        return render_template('temp.html')

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

# please dont remove code from above, if you need to comment it off



   


    return app

