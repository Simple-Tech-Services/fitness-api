from workout import app
from flask import request

@app.route("/workouts", methods=['POST', 'GET', 'DELETE', 'PUT'])
def route_workouts():
    if (request.method == 'GET'):
        return "Getting all workouts"

    elif (request.method == 'POST'):
        return "creates new workouts"

    elif (request.method == 'PUT'):
        return "updates workouts"

    elif (request.method == "DELETE"):
        return "deleting workouts"
        
    else:
        return "This route does not exist"