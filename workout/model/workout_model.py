"""db and user model"""
import sqlalchemy as sa
from workout import db
from workout.model.user_model import UserModel

class WorkoutModel(db.Model):
    """workout model schema"""

    id = sa.Column(sa.Integer, primary_key=True)
    owner_id = sa.Column(sa.ForeignKey(UserModel.id))
    name = sa.Column(sa.String(25), nullable=False)
    description = sa.Column(sa.String(250), nullable=True)

    def __repr__(self):
        return 'Workout %r' % self.name
