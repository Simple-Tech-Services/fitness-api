from workout import app
from flask import request


@app.route("/exercises", methods=['POST', 'GET', 'DELETE', 'PUT'])
def route_exercises():
    if (request.method == 'GET'):
        return "got all exercises"

    elif (request.method == 'POST'):
        return "exercise created"
    
    elif (request.method == 'PUT'):
        return "exercise updated"

    elif (request.method == 'DELETE'):
        return "exercise deleted"

    else:
        return "route does not exist."