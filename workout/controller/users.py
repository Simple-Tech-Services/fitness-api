from workout import app
from workout import db
from flask import request, jsonify

from workout.model.user import UserModel
#Route for all users
@app.route("/api/users", methods=['POST','DELETE', 'GET', 'PUT'])
def route_users():
    if(request.method == 'GET'):
        userList = []
        result = None

        try:
            result = db.session.execute(db.select(UserModel).order_by(UserModel.username)).scalars()
        except:
            return "Server Error"

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
#Route for specific user
@app.route("/api/user/<id>", methods=['POST','DELETE', 'GET', 'PUT'])
def route_user_id(id):
    if (request.method == "GET"):
        data = {}
        result = None
        
        try:
            result = db.session.execute(db.select(UserModel).filter_by(id=id)).one()
        except:
            return "User was not found"

        for user in result:
            data = {"username": user.username,
                    "firstName": user.first_name,
                    "lastName": user.last_name}

        return jsonify(data)

    elif (request.method == 'DELETE'):
        result = None
        try:
            result = db.session.execute(db.select(UserModel).filter_by(id=id)).one()
        except:
            return "User was not found"

        for user in result:
            db.session.delete(user)
            db.session.commit()

        return "deleting users"

    elif (request.method == 'PUT'):
        # store new values of user data
        data_list = request.json

        username = None 
        result = None      

        # get the user we want to change from db
        try:
            result = db.session.execute(db.select(UserModel).filter_by(id=id)).one()
        except:
            return "User was not found"
        
        # loop over data to get new value for field 
        for item in data_list:
            field = item.get("field")
            new_value = item.get("newValue")

            # update user with new values
            for user in result:
                username = user.username
                if(field == "firstName"):
                    user.first_name = new_value
                elif(field == "lastName"):
                    user.last_name = new_value
                elif(field == "userName"):
                    user.username = new_value
                elif(field == "password"):
                    user.password = new_value
                else:
                    return "user properties was not found"

        # commit changes
        db.session.commit()

        # return status code
        return f'user {username} was updated!'

    else:
        return "This route does not exist"
