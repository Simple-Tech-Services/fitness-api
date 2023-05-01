""" import database instance and sqlalchemy"""
import sqlalchemy as sa
from workout import db

class UserModel(db.Model):
    """user model schema"""
    id = sa.Column(sa.Integer, primary_key=True)
    public_id = sa.Column(sa.String(100), unique=True, nullable=False)
    username = sa.Column(sa.String(25), unique=True, nullable=False)
    password = sa.Column(sa.String(25), nullable=False)
    first_name = sa.Column(sa.String(25), nullable=False)
    last_name = sa.Column(sa.String(25), nullable=False)
    email = sa.Column(sa.String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
