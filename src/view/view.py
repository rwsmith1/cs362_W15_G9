__author__ = 'holly'

import sys
import curses
from curses import wrapper
#import MySQLdb
from src.models.user import User
from src.database.database import Database

class View(User):

    stdscr = ""
    currentUsername = ""
    currentPassword = ""
    n = 0

    def __init__(self, currentUsername, currentPassword):
        self.currentUsername = currentUsername
        self.currentPassword = currentPassword

    def validateUser(self):
        db = Database()
        db.connect()
        sql = "SELECT * FROM User WHERE name = '%s'" % (self.currentUsername)
        results = db.query(sql)

        self.password = results[2]
        self.email = results[3]

        if self.results is None:
            sys.exit("Invalid Username")
        if self.password != self.currentPassword:
            sys.exit("Invalid Password")

    def initView(self):
        self.stdscr = curses.initscr()

        # clear screen
        self.stdscr.clear()
        # turn off cursor
        curses.curs_set(False)

        # main menu program loop:
        while self.n != ord('3'):
            self.stdscr.clear()
            self.stdscr.addstr('Welcome ' + self.currentUsername)
            self.stdscr.addstr(2, 0, 'Enter a Number:')
            self.stdscr.addstr(3, 2, '1 - View Schedule')
            self.stdscr.addstr(4, 2, '2 - Cancel Appointment')
            self.stdscr.addstr(5, 2, '3 - Exit')
            self.stdscr.refresh()

            self.n = self.stdscr.getch()
            if self.n == ord('1'):
                self.stdscr.clear()
                self.stdscr.addstr('Schedule view')
                self.stdscr.refresh()
                self.stdscr.getkey()
            if self.n == ord('2'):
                self.stdscr.clear()
                self.stdscr.addstr('Cancel view')
                self.stdscr.refresh()
                self.stdscr.getkey()

    def initWrapper(self):
        # curses wrapper initiates and exits window/curses
        wrapper(self.initView())