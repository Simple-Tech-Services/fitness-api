from workout import db
import sqlalchemy as sa

class UserModel(db.Model):
    id = sa.Column(sa.Integer, primary_key = True)
    public_id = sa.Column(sa.String(100), unique = True, nullable = False)
    username = sa.Column(sa.String(25), unique = True, nullable = False)
    password = sa.Column(sa.String(25), nullable = False)
    first_name = sa.Column(sa.String(25), nullable = False)
    last_name = sa.Column(sa.String(25), nullable = False)
    email = sa.Column(sa.String(25), nullable = False)