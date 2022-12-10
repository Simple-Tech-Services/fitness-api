import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from controller import Users, Workouts
from model import UserModel, WorkoutModel, ExerciseModel


# load enviroment variables from .env file
cwd = os.getcwd()
load_dotenv(cwd + "/.env")

# store env variables
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
name = os.getenv('DB_NAME')

# init flask app and database
db = SQLAlchemy()
app = Flask(__name__)

# configure database connection
connectionURL = f'mysql+pymysql://{username}:{password}@{host}/{name}'
app.config["SQLALCHEMY_DATABASE_URI"] = connectionURL
db.init_app(app)

# generate tables
registerUserModel = UserModel()
registerWorkoutModel =  WorkoutModel()
registerExerciseModel = ExerciseModel()

with app.app_context():
    db.create_all()

# routes
user_routes = Users()
workouts_routes = Workouts()
exercises_routes = Exercises()


@app.route("/")
def hello_world():
    return "welcome to our fitness app api"


# Users routes
@app.route("/users", methods=['POST','DELETE', 'GET', 'PUT'])
def route_users():
    if(request.method == 'GET'):
        response = user_routes.get_users()
        return response
    
    elif (request.method == 'POST'):
        response = user_routes.post_users()
        return response
    
    elif (request.method == 'DELETE'):
        response = user_routes.delete_users()
        return response


    elif (request.method == 'PUT'):
        response = user_routes.put_users()
        return response
    else:
        return "This route does not exist"

# Workout routes
@app.route("/workouts", methods=['POST', 'GET', 'DELETE', 'PUT'])
def route_workouts():
    if (request.method == 'GET'):
        response = workouts_routes.get_workouts()
        return response

    elif (request.method == 'POST'):
        response = workouts_routes.post_workouts()
        return response

    elif (request.method == "DELETE"):
        response = workouts_routes.delete_workouts()
        return response
    
    elif (request.method == 'PUT'):
        response = workouts_routes.put_workouts()
        return response
    
    else:
        return "This route does not exist"

# Exercise routes
@app.route("/exercises", methods=['POST', 'GET', 'DELETE', 'PUT'])
def route_exercises():
    if (request.method == 'GET'):
        response = exercises_routes.get_exerises()
        return response

    elif (request.method == 'POST'):
        response = exercises_routes.post_exercises()
        return response
    
    elif (request.method == 'DELETE'):
        response = exercises_routes.delete_exercises()
        return response

    elif (request.method == 'PUT'):
        response = exercises_routes.put_exercises()
        return response

    else:
        return "This route does not exist."

