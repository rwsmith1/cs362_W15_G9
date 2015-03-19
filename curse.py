#!/usr/bin/python
####################################################################
    # Name: curse.py
    # Parameter: useremail password
    # This program is called from the command line to initiate the
    # CLI client. The user email address and password should be
    # passed on the command line.
    # example: python curse.py sample@gmail.com 1234
####################################################################

import sys
from src.view.view import View

# get username (email) and password from command line:
args = len(sys.argv)
if args < 3:
    sys.exit("Invalid Input: include user-email and password in command line")
userName = sys.argv[1]
userPass = sys.argv[2]

# start the curses CLI program from src/view/view.py
newView = View(userName, userPass)
newView.validateUser()
newView.initWrapper()