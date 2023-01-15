from workout import app, db
from flask import request, jsonify
from workout.model.workout import WorkoutModel

@app.route("/api/workouts", methods=['POST', 'GET'])
def route_workouts():
    if (request.method == 'GET'):
        return "Getting all workouts"

    elif (request.method == 'POST'):
        name = request.form['name']
        description = request.form['description']

        # creating workout object
        workout = WorkoutModel(name=name,
                               description=description)

        # save on database
        db.session.add(workout)
        db.session.commit()


        return f'workout {name} was created'
        
    else:
        return "This route does not exist"

@app.route("/api/workout/<id>", methods=['POST', 'GET', 'DELETE', 'PUT'])
def route_workout_id(id): 
    if (request.method == 'GET'):
        data = {}
        result = None

        try:
            result = db.session.execute(db.select(WorkoutModel).filter_by(id=id)).one()
        except:
            return "workout not found"
        
        for workout in result:
            data = {"workout name": workout.name,
                    "description": workout.description}

        return jsonify(data)

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
    
    elif (request.method == 'PUT'):
        data_list = request.json

        name = None
        result = None

        try:
            result = db.session.execute(db.select(WorkoutModel).filter_by(id=id)).one()
        except:
            return "workout was not found"
        
        for items in data_list:
            field = items.get("field")
            new_value = items.get("newValue")

            for workout in result:
                name = workout.name
                if(field == "name"):
                    workout.name = new_value
                elif(field == "description"):
                    workout.description = new_value

        db.session.commit()

        return f'workout {name} was updated'

    else:
        return "route does not exist"

