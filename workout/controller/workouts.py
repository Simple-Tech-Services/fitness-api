from workout import app, db
from flask import request
from workout.model.workout import WorkoutModel

@app.route("/api/workouts", methods=['POST', 'GET'])
def route_workouts():
    if (request.method == 'GET'):
        return "Getting all workouts"

    elif (request.method == 'POST'):
        name = request.form['name']

        # creating workout object
        workout = WorkoutModel(name = name)

        # save on database
        db.session.add(workout)
        db.session.commit()


        return f'workout {name} was created'
        
    else:
        return "This route does not exist"