####################################################################
    # Name: mailbox.py
    # Initializes a User
####################################################################
__author__ = 'kkozee'

from src.models.user import User


class UserBuilder(User):

    def __init__(self, id, name, email, password):
        super(UserBuilder, self).__init__(id, name, email, password)