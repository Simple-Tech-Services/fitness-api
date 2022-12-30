from workout import db
import sqlalchemy as sa

class UserModel(db.Model):
    id = sa.Column(sa.Integer, primary_key = True)
    username = sa.Column(sa.String(25), unique = True, nullable = False)
    password = sa.Column(sa.String(25), nullable = False)
    first_name = sa.Column(sa.String(25), nullable = False)
    last_name = sa.Column(sa.String(25), nullable = False)