""" flask api tool and workout model and variables """
from flask import request, jsonify
from workout import app, db
from workout.model.exercise_model import ExerciseModel


@app.route("/api/exercises", methods=["POST", "GET"])
def route_exercises():
    """exercise routes for CRUD operations"""
    if request.method == "GET":
        exercise_list = []
        result = None

        try:
            result = db.session.execute(
                db.select(ExerciseModel).order_by(ExerciseModel.id)
            ).scalars()
        except:
            return "Server Error"

        for exercise in result:
            exercise_dict = {
                "id": exercise.id,
                "name": exercise.name,
                "sets": exercise.sets,
                "reps": exercise.reps,
            }
            exercise_list.append(exercise_dict)

        return jsonify(exercise_list)

    if request.method == "POST":
        name = request.form["name"]
        sets = request.form["sets"]
        reps = request.form["reps"]

        exercise = ExerciseModel(name=name, sets=sets, reps=reps)

        db.session.add(exercise)
        db.session.commit()

        return f"exercise {name} was created"

    return "route does not exist."


@app.route("/api/exercise/<exercise_id>", methods=["GET", "DELETE", "PUT"])
def route_exercise_id(exercise_id):
    """exercise routes for CRUD operations"""
    if request.method == "GET":
        data = {}
        result = None

        try:
            result = db.session.execute(
                db.select(ExerciseModel).filter_by(id=exercise_id)
            ).one()
        except:
            return "Exercise was not found"

        for exercise in result:
            data = {"name": exercise.name, "sets": exercise.sets, "reps": exercise.reps}

        return jsonify(data)

    if request.method == "PUT":
        data_list = request.json

        name = None
        result = None

        # get the user we want to change from db
        try:
            result = db.session.execute(db.select(ExerciseModel).filter_by(id=id)).one()
        except:
            return "Exercise was not found"

        # loop over data to get new value for field
        for item in data_list:
            field = item.get("field")
            new_value = item.get("newValue")

            # update user with new values
            for exercise in result:
                name = exercise.name
                if field == "name":
                    exercise.name = new_value
                elif field == "sets":
                    exercise.sets = new_value
                elif field == "reps":
                    exercise.reps = new_value

                else:
                    return "exercise properties was not found"

        # commit changes
        db.session.commit()

        # return status code
        return f"exercise {name} was updated!"

    if request.method == "DELETE":
        result = None
        try:
            result = db.session.execute(db.select(ExerciseModel).filter_by(id=id)).one()
        except:
            return "Exercise was not found"

        for exercise in result:
            db.session.delete(exercise)
            db.session.commit()

        return "exercise deleted"

    return "route does not exist."
