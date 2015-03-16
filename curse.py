#!/usr/bin/python

import sys
from src.view.view import View

# get username (email) and password from command line:
args = len(sys.argv)
if args < 3:
    sys.exit("Invalid Input: include user-email and password in command line")
userName = sys.argv[1]
userPass = sys.argv[2]

newView = View(userName, userPass)
newView.validateUser()

newView.initWrapper()