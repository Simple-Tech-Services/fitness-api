from os import getenv, getcwd
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import jwt

# imports all routes from the controller directory
from workout.model import user, workout
from workout.controller import exercises, users, workouts

# load enviroment variables from .env file
cwd = getcwd()
load_dotenv(cwd + "/.env")

# store env variables
username = getenv('DB_USERNAME')
password = getenv('DB_PASSWORD')
host = getenv('DB_HOST')
name = getenv('DB_NAME')
secret = getenv('SECRET_KEY')

# init flask app and database
db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = secret

# configure database connection
connectionURL = f'mysql+pymysql://{username}:{password}@{host}/{name}'
app.config["SQLALCHEMY_DATABASE_URI"] = connectionURL
db.init_app(app)

# root route


@app.route("/")
def hello_world():
    return "welcome to our fitness app api"


with app.app_context():
    db.create_all()
