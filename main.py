from flask import Flask
from controller.users import Users
from controller.workouts import Workouts

app = Flask(__name__)

usersRoute = Users()


@app.route("/")
def hello_world():
    return "welcome to our fitness app api"

# Register User Routes

# Register Workout Routes
