from workout import app, db
from flask import request, jsonify
from workout.model.exercise import ExerciseModel


@app.route("/api/exercises", methods=['POST', 'GET'])
def route_exercises():
    if (request.method == 'GET'):
        exerciseList = []
        result = None

        try:
            result = db.session.execute(db.select(ExerciseModel).order_by(ExerciseModel.id)).scalars()
        except:
            return "Server Error"

        for exercise in result:
            exerciseDict = {
                        "id" : exercise.id,
                        "name" : exercise.name,
                        "sets" : exercise.sets,
                        "reps" : exercise.reps
                        }
            exerciseList.append(exerciseDict)

        return jsonify(exerciseList)

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
    

    else:
        return "route does not exist."

@app.route("/api/exercise/<id>", methods=['GET', 'DELETE', 'PUT'])
def route_exercise_id(id):
    if (request.method == 'GET'):
        data = {}
        result = None
        
        try:
            result = db.session.execute(db.select(ExerciseModel).filter_by(id=id)).one()
        except:
            return "Exercise was not found"

        for exercise in result:
            data = {"name": exercise.name,
                    "sets": exercise.sets,
                    "reps": exercise.reps}

        return jsonify(data)

    elif (request.method == 'PUT'):
        return "exercise updated"

    elif (request.method == 'DELETE'):
        result = None
        try:
            result = db.session.execute(db.select(ExerciseModel).filter_by(id=id)).one()
        except:
            return "Exercise was not found"

        for exercise in result:
            db.session.delete(exercise)
            db.session.commit()
            
        return "exercise deleted"
    else:
        return "route does not exist."