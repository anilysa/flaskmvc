import os
from flask import Flask, render_template, redirect, url_for
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
        return render_template('signup.html')

    @app.route('/view')
    def view():
        return render_template('routineview.html')


    # @app.route('/add_exercise', methods=['POST'])
    # def add_exercise():
    #     exercise = request.form['exercise']
    #     day = request.form['day']
    #     # Here you can add the exercise to the routine and render the new page
    #         return render_template('routineview.html', exercise=exercise, day=day)

# # Login
# @app.route('/login', methods=['POST'])
# def user_login_view():
#   data = request.json
#   return login_user(data['username'], data['password'])


# @app.route('/identify')
# @jwt_required()
# def identify_view():
#   username = get_jwt_identity()
#   user = User.query.filter_by(username=username).first()
#   if user:
#     return jsonify(user.get_json())
#   return jsonify(message='Invalid user'), 403


# # Sign Up
# @app.route('/signup', methods=['POST'])
# def signup_user_view():
#   data = request.json
#   try:
#     new_user = RegularUser(data['username'], data['email'], data['password'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(
#         message=f'User {new_user.id} - {new_user.username} created!'), 201
#   except IntegrityError:
#     db.session.rollback()
#     return jsonify(error='Username already exists'), 400


# # Logout
# @app.route('/logout', methods=['GET'])
# def logout():
#   response = jsonify(message='Logged out')
#   unset_jwt_cookies(response)
#   return response


    return app
