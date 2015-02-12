__author__ = 'kkozee'

import sys

sys.path.append('/Users/kkozee/PycharmProjects/cs362_W15_G9/')

from src.models.user import User
from src.models.filter import Filter
from src.models.messages import Messages
from src.builders.messageBuilder import MessageBuilder
from src.view.view import View
import getpass

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

    m = MessageBuilder()

    m.buildMessageFromEmail('email.txt')











