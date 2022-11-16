from flask import Flask, request
from controller import Users, Workouts

app = Flask(__name__)

registerUsersRoutes = Users()
registerWrokoutRoutes = Workouts()

@app.route("/")
def hello_world():
    # Register User Routes # Register Workout Routes
    return "welcome to our fitness app api"


@app.route("/workout")
def route_workout():
    response = registerUsersRoutes.getUsers()
    return response


