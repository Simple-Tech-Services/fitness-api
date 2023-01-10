from workout import db
import sqlalchemy as sa
from workout import WorkoutModel
class ExerciseModel(db.Model):
    workout_id = sa.Column(sa.ForeignKey(WorkoutModel.id))
    