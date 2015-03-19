####################################################################
    # Name: student.py
    # Initializes values for a Student
####################################################################
__author__ = 'kkozee'

from src.models.user import User

class Student(User):

    def __init__(self, id, name, email):
        self.id = id
        self.studentName = name
        self.email = email