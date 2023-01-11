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

@app.route("/api/workout/<id>", methods=['POST', 'GET', 'DELETE', 'PUT'])
def route_workout_id(id):

    if (request.method == 'GET'):
        return "getting a workout"

    elif (request.method == 'DELETE'):
        result = None

        try:
            result = db.session.execute(db.select(WorkoutModel).filter_by(id=id)).one()
        
        except:
            return "workout was not found"
        
        for workout in result:
            db.session.delete(workout)
            db.session.commit()

        return "deleting a workout"
