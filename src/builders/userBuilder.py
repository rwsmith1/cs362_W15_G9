__author__ = 'kkozee'

from src.models.user import User

class UserBuilder(User):

    user = ""

    def __init__(self):
        self.buildUser()
        self.user = User(self.id, self.name, self.email, self.password)

    def buildUser(self):
        return