from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy;
from controller import Users, Workouts

app = Flask(__name__)

user_routes = Users()
workout_routes = Workouts()


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