""" flask api tools and workout app variables """
from flask import request, jsonify
from workout import app, db
from workout.model.workout_model import WorkoutModel


@app.route("/api/workouts", methods=['POST', 'GET'])
def route_workouts():
    """ workout api CRUD operations """
    if request.method == 'GET':
        return "Getting all workouts"

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        # creating workout object
        workout = WorkoutModel(name=name, description=description)

        # save on database
        db.session.add(workout)
        db.session.commit()

        return f'workout {name} was created'

    return "This route does not exist"


@app.route("/api/workout/<workout_id>", methods=['POST', 'GET', 'DELETE', 'PUT'])
def route_workout_id(workout_id):
    """ specific workout with ID api CRUD operations """
    if request.method == 'GET':
        data = {}
        result = None

        try:
            result = db.session.execute(
                db.select(WorkoutModel).filter_by(id=workout_id)).one()
        except:
            return "workout not found"

        for workout in result:
            data = {"workoutName": workout.name,
                    "description": workout.description}

        return jsonify(data)

    if request.method == 'DELETE':
        result = None

        try:
            result = db.session.execute(
                db.select(WorkoutModel).filter_by(id=workout_id)).one()
        except:
            return "workout was not found"

        for workout in result:
            db.session.delete(workout)
            db.session.commit()

        return "deleting a workout"

    if request.method == 'PUT':
        data_list = request.json

        name = None
        result = None

        try:
            result = db.session.execute(
                db.select(WorkoutModel).filter_by(id=workout_id)).one()
        except:
            return "workout was not found"

        for items in data_list:
            field = items.get("field")
            new_value = items.get("newValue")

            for workout in result:
                name = workout.name
                if field == "name":
                    workout.name = new_value
                elif field == "description":
                    workout.description = new_value

        db.session.commit()

        return f'workout {name} was updated'

    return "route does not exist"
