import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy;

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
workout_routes = Workouts()


@app.route("/")
def hello_world():
    return "welcome to our fitness app api"


# users routes


# Workout routes
@app.route("/workouts", methods=['POST', 'GET', 'DELETE', 'PUT'])
def route_workout():
    if (request.method == 'GET'):
        response = workout_routes.get_workouts()
        return response


# exercise routes