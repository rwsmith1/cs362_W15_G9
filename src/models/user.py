__author__ = 'kkozee'

from src.models.base import Base

class User(Base):

    name = ""
    email = ""
    password = ""

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def setName(self, name):
        self.name = name
        return self.name

    def getName(self):
        return self.name

    def setEmail(self, email):
        self.email = email
        return self.email

    def getEmail(self):
        return self.email

    def setPassword(self, password):
        self.password = password
        return self.password

    def getPassword(self):
        return self.password


