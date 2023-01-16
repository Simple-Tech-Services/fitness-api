from workout import app, db
from flask import request, jsonify
from workout.model.exercise import ExerciseModel


@app.route("/api/exercises", methods=['POST', 'GET', 'DELETE', 'PUT'])
def route_exercises():
    if (request.method == 'GET'):
        return "got all exercises"

    elif (request.method == 'POST'):
        name = request.form['name']
        sets = request.form['sets']
        reps = request.form['reps']

        exercise = ExerciseModel(name=name,
                                 sets=sets,
                                 reps=reps)

        db.session.add(exercise)
        db.session.commit()

        return f'exercise {name} was created'
    
    elif (request.method == 'PUT'):
        return "exercise updated"

    elif (request.method == 'DELETE'):
        return "exercise deleted"

    else:
        return "route does not exist."