from sqlalchemy import Column, Integer, String, relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserModel(Base):
    id = Column(Integer, primary_key = True)
    username = Column(String, unique = True, nullable = False)
    password = Column(String, nullable = False)
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    workouts = relationship('WorkoutModel', backref = 'user')