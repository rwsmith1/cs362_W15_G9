__author__ = 'kkozee'

from src.models.user import User

class Student(User):

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email