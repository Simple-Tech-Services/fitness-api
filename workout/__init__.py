"""
setup - imports enviroment variables
        initializes flask application and database connnection

controller - routes for all crud operations

model - schemas for all data models
"""
from workout.setup import app, db
from workout.controller import exercises, users, workouts
from workout.model import *

@app.route("/")
def hello_world():
    """hello world  route of api"""
    return "welcome to our fitness app api"

with app.app_context():
    db.create_all()
