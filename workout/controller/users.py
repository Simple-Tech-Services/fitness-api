from workout import app
from workout import db
from flask import request, jsonify

from workout.model.user import UserModel

@app.route("api/users", methods=['POST','DELETE', 'GET', 'PUT'])
def route_users():
    if(request.method == 'GET'):
        return 'got all users'
    
    elif (request.method == 'POST'):
        # store user info
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        
        # create user object
        user = UserModel(username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name)

        # save on db
        db.session.add(user)
        db.session.commit()

        return "user was created"
    
    else:
        return "This route does not exist"

@app.route("api/user/<id>", methods=['POST','DELETE', 'GET', 'PUT'])
def route_user_id(id):
    if (request.method == "GET"):
        data = {}

        result = db.session.execute(db.select(UserModel).filter_by(id=id)).one()

        for row in result:
            data = {"username": row.username,
                    "firstName": row.first_name,
                    "lastName": row.last_name}

        return jsonify(data)

    elif (request.method == 'DELETE'):
        return "deleting users"

    elif (request.method == 'PUT'):
        return "updates users"
    
    else:
        return "This route does not exist"