import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy;
from controller import Users, Workouts, Exercises

# load enviroment variables from .env file
cwd = os.getcwd()
load_dotenv(cwd + "/.env")

# store Env Variables
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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

with app.app_context():
    db.create_all()


# Routes
user_routes = Users()
workout_routes = Workouts()
exercises_routes = Exercises()


@app.route("/")
def hello_world():
    return "welcome to our fitness app api"


# Users routes


# Workout routes
@app.route("/workouts", methods=['POST', 'GET', 'DELETE', 'PUT'])
def route_workout():
    if (request.method == 'GET'):
        response = workout_routes.get_workouts()
        return response


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


