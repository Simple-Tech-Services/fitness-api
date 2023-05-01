""" app properties  """
import sqlalchemy as sa
from workout import db
from workout.model.workout_model import WorkoutModel

class ExerciseModel(db.Model):
    """exercise model schema"""

    id = sa.Column(sa.Integer, primary_key=True)
    workout_id = sa.Column(sa.ForeignKey(WorkoutModel.id))
    name = sa.Column(sa.String(25), nullable=False)
    sets = sa.Column(sa.Integer, nullable=False)
    reps = sa.Column(sa.Integer, nullable=False)

    def __repr__(self):
        return '<Exercise %r>' % self.name