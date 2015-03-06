__author__ = 'holly'

import sys
import curses
from curses import wrapper
from src.models.user import User
from src.database.database import Database
from src.database.databaseEvent import databaseEvent

class View(User):

    def __init__(self, currentUsername, currentPassword):
        self.currentUsername = currentUsername
        self.currentPassword = currentPassword
        self.stdscr = None
        self.n = 0
        self.m = 0
        self.c = 0
        self.db = None
        self.userId = None

    def validateUser(self):
        self.db = Database()
        self.db.connect()
        sql = "SELECT * FROM User WHERE name = '%s'" % (self.currentUsername)
        results = self.db.query(sql)

        if results is not None:
            self.userId = results[0]
            self.password = results[2]
            self.email = results[3]
        elif results is None:
            sys.exit("Invalid Username")
        if self.password != self.currentPassword:
            sys.exit("Invalid Password")

    def initView(self):
        self.stdscr = curses.initscr()
        q = databaseEvent()
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
                self.stdscr.addstr('Schedule View - *Press Any Key for Main Menu*')
                self.stdscr.addstr(2, 0, 'DATE')
                self.stdscr.addstr(2, 15, 'TIME')
                self.stdscr.addstr(2, 30, 'STUDENT')
                self.stdscr.addstr(2, 50, 'STUDENT EMAIL')
                sql = q.getApp(self.userId)
                appts = self.db.queryall(sql)
                row = 3
                for app in appts:
                    #studentId = app[3]
                    studentName = str(app[4])
                    studentEmail = str(app[5])
                    time = str(app[6])
                    date = str(app[8])
                    status = str(app[9])
                    #location = app[5]
                    if status == "0":
                        self.stdscr.addstr(row, 0, date)
                        self.stdscr.addstr(row, 15, time)
                        self.stdscr.addstr(row, 30, studentName)
                        self.stdscr.addstr(row, 50, studentEmail)
                        row += 1
                self.stdscr.refresh()
                self.stdscr.getkey()
            if self.n == ord('2'):
                self.stdscr.clear()
                self.stdscr.addstr('Cancel View - *Press "x" for Main Menu*')
                self.stdscr.addstr(1, 0, 'Enter the ID number of the Appointment you would like to Cancel')
                self.stdscr.addstr(3, 0, 'Appointment ID')
                self.stdscr.addstr(3, 15, 'DATE')
                self.stdscr.addstr(3, 30, 'STATUS')
                self.stdscr.addstr(3, 50, 'STUDENT')
                sql = q.getApp(self.userId)
                appts2 = self.db.queryall(sql)
                row = 4
                for app2 in appts2:
                    appId = str(app2[0])
                    studentName = str(app2[4])
                    date = str(app2[8])
                    status = str(app2[9])
                    if status == "1":
                        status = "Canceled"
                    else:
                        status = "Active"
                    self.stdscr.addstr(row, 0, appId)
                    self.stdscr.addstr(row, 15, date)
                    self.stdscr.addstr(row, 30, status)
                    self.stdscr.addstr(row, 50, studentName)
                    row += 1

                self.m = self.stdscr.getch()
                if self.m != ord('x'):
                    for app2 in appts2:
                        if str(unichr(self.m)) == str(app2[0]):
                            self.stdscr.clear()
                            self.stdscr.addstr('Are you sure you would like to cancel this appointment? (y/n)')
                            self.stdscr.addstr(2, 0, 'Appointment ID')
                            self.stdscr.addstr(2, 15, 'DATE')
                            self.stdscr.addstr(2, 30, 'STUDENT')
                            appId = str(app2[0])
                            studentName = str(app2[4])
                            date = str(app2[8])
                            self.stdscr.addstr(3, 0, appId)
                            self.stdscr.addstr(3, 15, date)
                            self.stdscr.addstr(3, 30, studentName)
                            self.c = self.stdscr.getch()
                            if self.c == ord('y'):
                                sql = q.handleApp(app2[0])
                                self.db.update(sql)
                                self.stdscr.clear()
                                self.stdscr.addstr('Cancelled! - *Press any key for main menu*')
                            else:
                                self.stdscr.clear()
                                self.stdscr.addstr('Not cancelled - *Press any key for main menu*')
                self.stdscr.refresh()
                self.stdscr.getkey()

    def initWrapper(self):
        # curses wrapper initiates and exits window/curses
        wrapper(self.initView())