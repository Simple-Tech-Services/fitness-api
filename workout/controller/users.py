from workout import app
from workout import db
from flask import request, jsonify

from workout.model.user import UserModel

@app.route("/api/users", methods=['POST','DELETE', 'GET', 'PUT'])
def route_users():
    if(request.method == 'GET'):
        userList = []

        result = db.session.execute(db.select(UserModel).order_by(UserModel.username)).scalars()
        
        for user in result:
            userDict = {
                        "id" : user.id,
                        "username" : user.username,
                        "first_name" : user.first_name,
                        "last_name" : user.last_name
                        }
            userList.append(userDict)
        
        return jsonify(userList)
    
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

        return f'user {username} was created'
    
    else:
        return "This route does not exist"

@app.route("/api/user/<id>", methods=['POST','DELETE', 'GET', 'PUT'])
def route_user_id(id):
    if (request.method == "GET"):
        data = {}

        result = db.session.execute(db.select(UserModel).filter_by(id=id)).one()

        for user in result:
            data = {"username": user.username,
                    "firstName": user.first_name,
                    "lastName": user.last_name}

        return jsonify(data)

    elif (request.method == 'DELETE'):
        result = db.session.execute(db.select(UserModel).filter_by(id=id)).one()

        for user in result:
            db.session.delete(user)
            db.session.commit()

        return "deleting users"

    elif (request.method == 'PUT'):
        return "updates users"
    
    else:
        return "This route does not exist"
