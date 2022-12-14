from os import getenv, getcwd
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# load enviroment variables from .env file
cwd = getcwd()
load_dotenv(cwd + "/.env")

# store env variables
username = getenv('DB_USERNAME')
password = getenv('DB_PASSWORD')
host = getenv('DB_HOST')
name = getenv('DB_NAME')

# init flask app and database
db = SQLAlchemy()
app = Flask(__name__)

# configure database connection
connectionURL = f'mysql+pymysql://{username}:{password}@{host}/{name}'
app.config["SQLALCHEMY_DATABASE_URI"] = connectionURL
db.init_app(app)

# root route
@app.route("/")
def hello_world():
    return "welcome to our fitness app api"

from workout.model import user, workout
# imports all routes from the controller directory
from workout.controller import exercises, users, workouts

with app.app_context():
    db.create_all()