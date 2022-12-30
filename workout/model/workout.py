from workout import db

class WorkoutModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    exercise_list = db.Column(db.ForeignKey('userId'))