from workout import app, db
from flask import request, jsonify, make_response
import uuid
from workout.model.user import UserModel
from datetime import datetime, timedelta
import jwt


@app.route('/api/login', methods=['POST'])
def login():
    auth = request.form

    # safe guard to check if ther is an email and password
    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return 'could not verify'

    # getting user data
    user = None
    try:
        result = db.session.execute(
            db.select(UserModel).filter_by(email=auth.get('email'))).one()

        for currentUser in result:
            user = currentUser

    except:
        return 'no user was found'

    # check for password
    if auth.get('password') == user.password:
        # give jwt token
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return make_response(jsonify({'token': token}))

    return 'wrong password'


@app.route('/api/signup', methods=['POST'])
def signup():
    # create a dictionary of the form data
    data = request.form

    # get name, email and password
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    username = request.form['username']
    email = data.get('email'),
    password = data.get('password')

    # checking for existing user
    user = None

    try:
        result = db.session.execute(
            db.select(UserModel).filter_by(email=email)).one()

        for currentUser in result:
            user = currentUser

    except:
        pass

    if not user:
        # create user object
        user = UserModel(
            public_id=str(uuid.uuid4()),
            last_name=last_name,
            first_name=first_name,
            username=username,
            email=email,
            password=password)

        # save on db
        db.session.add(user)
        db.session.commit()

        return f'user {username} was created'
    else:
        return 'User already exists. Please Log in.'


# Route for all users
@app.route("/api/users", methods=['POST', 'DELETE', 'GET', 'PUT'])
def route_users():
    if (request.method == 'GET'):
        userList = []
        result = None

        try:
            result = db.session.execute(
                db.select(UserModel).order_by(UserModel.username)).scalars()
        except:
            return "Server Error"

        for user in result:
            userDict = {
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name
            }
            userList.append(userDict)

        return jsonify(userList)

    else:
        return "This route does not exist"

# Route for specific user


@app.route("/api/user/<id>", methods=['POST', 'DELETE', 'GET', 'PUT'])
def route_user_id(id):
    if (request.method == "GET"):
        data = {}
        result = None

        try:
            result = db.session.execute(
                db.select(UserModel).filter_by(id=id)).one()
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
            result = db.session.execute(
                db.select(UserModel).filter_by(id=id)).one()
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
            result = db.session.execute(
                db.select(UserModel).filter_by(id=id)).one()
        except:
            return "User was not found"

        # loop over data to get new value for field
        for item in data_list:
            field = item.get("field")
            new_value = item.get("newValue")

            # update user with new values
            for user in result:
                username = user.username
                if (field == "firstName"):
                    user.first_name = new_value
                elif (field == "lastName"):
                    user.last_name = new_value
                elif (field == "userName"):
                    user.username = new_value
                elif (field == "password"):
                    user.password = new_value
                else:
                    return "user properties was not found"

        # commit changes
        db.session.commit()

        # return status code
        return f'user {username} was updated!'

    else:
        return "This route does not exist"
