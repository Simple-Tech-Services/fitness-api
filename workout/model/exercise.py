from workout import db
import sqlalchemy as sa
from .workout import WorkoutModel


class ExerciseModel(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    workout_id = sa.Column(sa.ForeignKey(WorkoutModel.id))
    name = sa.Column(sa.String(25), nullable=False)
    sets = sa.Column(sa.Integer, nullable=False)
    reps = sa.Column(sa.Integer, nullable=False)
