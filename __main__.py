__author__ = 'kkozee'

from src.models.user import User
from src.models.filter import Filter
from src.view.view import View
import getpass

import sys

if __name__ == '__main__':

    args = len(sys.argv)
    if args < 3:
        currentUsername = raw_input("Username: ")
        currentPassword = getpass.getpass()
    else:  # get username and password from command line
        currentUsername = sys.argv[1]
        currentPassword = sys.argv[2]

    view = View(currentUsername, currentPassword)
   
    view.validateUser()

    view.initWrapper()










