from workout import db
import sqlalchemy as sa
from user import UserModel

class WorkoutModel(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    owner_id = sa.Column(sa.ForeignKey(UserModel.id))
    name = sa.Column(sa.String, nullable = False)
    #exercise_list = db.Column(db.ForeignKey('userId'))