from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from .user import UserModel
from .exercise import ExerciseModel

Base = declarative_base()

class WorkoutModel(Base):
    name = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey(UserModel.id), nullable = False)
    exerciseList = Column(ForeignKey('userId'))