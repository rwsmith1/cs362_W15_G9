__author__ = 'holly'

import sys
import datetime
import smtplib
import curses
from curses import wrapper
from email.mime.text import MIMEText
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
        results = databaseEvent().getInfo(self.db, self.currentUsername)

        if results is not None:
            self.userId = results[0]
            self.userName = results[1]
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
            self.stdscr.addstr('Welcome ' + self.userName)
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
                self.stdscr.addstr(2, 13, 'TIME')
                self.stdscr.addstr(2, 30, 'STUDENT')
                self.stdscr.addstr(2, 50, 'STUDENT EMAIL')
                appts = q.getApp(self.db, self.userId)
                row = 3
                for app in appts:
                    studentName = str(app[4])
                    studentEmail = str(app[5])
                    startTime = str(app[6])
                    endTime = str(app[7])
                    time = startTime + "-" + endTime
                    status = str(app[10])
                    date = str(app[9])
                    if status == "0":
                        self.stdscr.addstr(row, 0, date)
                        self.stdscr.addstr(row, 13, time)
                        self.stdscr.addstr(row, 30, studentName)
                        self.stdscr.addstr(row, 50, studentEmail)
                        row += 1
                self.stdscr.refresh()
                self.stdscr.getkey()
            if self.n == ord('2'):
                curses.curs_set(True)
                self.stdscr.clear()
                self.stdscr.addstr('Cancel View')
                self.stdscr.addstr(1, 0, 'Enter ID number of Appointment you would like to Cancel or "exit" for Main Menu')
                self.stdscr.addstr(2, 0, '::', curses.A_BOLD)
                self.stdscr.addstr(4, 0, 'Appt ID')
                self.stdscr.addstr(4, 10, 'DATE')
                self.stdscr.addstr(4, 25, 'TIME')
                #self.stdscr.addstr(4, 45, 'STATUS')
                self.stdscr.addstr(4, 45, 'STUDENT')
                appts2 = q.getApp(self.db, self.userId)
                row = 5
                appIds = []
                for app2 in appts2:
                    appIds.append(str(app2[0]))
                    appId = str(app2[0])
                    studentName = str(app2[4])
                    startTime = str(app2[6])
                    endTime = str(app2[7])
                    time = startTime + "-" + endTime
                    date = str(app2[9])
                    status = str(app2[10])
                    #if status == "1":
                    #    status = "Canceled"
                    #else:
                    #    status = "Active"
                    if status == "0":
                        self.stdscr.addstr(row, 1, appId)
                        self.stdscr.addstr(row, 10, date)
                        self.stdscr.addstr(row, 25, time)
                        #self.stdscr.addstr(row, 45, status)
                        self.stdscr.addstr(row, 45, studentName)
                        row += 1

                self.stdscr.move(2, 3)
                self.m = self.stdscr.getstr()
                while self.m not in appIds and self.m != "exit":
                    self.stdscr.move(2, 3)
                    self.stdscr.clrtoeol()
                    self.m = self.stdscr.getstr()
                self.stdscr.addstr(6, 5, "good id")

                if self.m != "exit":
                    curses.curs_set(False)
                    for app2 in appts2:
                        if self.m == str(app2[0]):
                            self.stdscr.clear()
                            self.stdscr.addstr('Are you sure you would like to cancel this appointment? (y/n)')
                            self.stdscr.addstr(2, 0, 'Appt ID')
                            self.stdscr.addstr(2, 10, 'DATE')
                            self.stdscr.addstr(2, 25, 'TIME')
                            self.stdscr.addstr(2, 45, 'STUDENT')
                            appId = str(app2[0])
                            studentName = str(app2[4])
                            startTime = str(app2[6])
                            eStart = app2[6]
                            endTime = str(app2[7])
                            eEnd = app2[7]
                            time = startTime + "-" + endTime
                            date = str(app2[9])
                            eDate = app2[9]
                            studentEmail = str(app2[5])
                            self.stdscr.addstr(3, 1, appId)
                            self.stdscr.addstr(3, 10, date)
                            self.stdscr.addstr(3, 25, time)
                            self.stdscr.addstr(3, 45, studentName)
                            self.c = self.stdscr.getch()
                            if self.c == ord('y'):
                                sql = q.handleApp(self.db, app2[0])
                                self.sendCancellation(self.userName, self.email, studentName, studentEmail, eDate, eStart, eEnd)
                                self.stdscr.clear()
                                self.stdscr.addstr('Cancelled! - *Press any key for main menu*')
                                #self.stdscr.refresh()
                                self.stdscr.getkey()
                            else:
                                self.stdscr.clear()
                                self.stdscr.addstr('Not cancelled - *Press any key for main menu*')
                                #self.stdscr.refresh()
                                self.stdscr.getkey()
                else:
                    self.initView()



    def initWrapper(self):
        # curses wrapper initiates and exits window/curses
        wrapper(self.initView())

    def sendCancellation(self, name, email, student_name, student_email, date, startTime, endTime):
        self.db = Database()
        self.db.connect()
        dateStr = date.strftime('%A, %B %d, %Y')
        period = "am"
        startHour = startTime.seconds // 3600
        startMins = (startTime.seconds % 3600) // 60
        if startHour > 12:
            startHour = startHour - 12
            period = "pm"
        startStr = str(startHour) + ":" + str(startMins) + period
        endHour = endTime.seconds // 3600
        endMins = (endTime.seconds % 3600) // 60
        if endHour > 12:
            endHour = startHour - 12
            period = "pm"
        endStr = str(endHour) + ":" + str(endMins) + period
        time = startStr + "-" + endStr

        fromAddr = 'do.not.reply@engr.orst.edu'
        toAddr = email
        #toAddr = 'harmonh@onid.oregonstate.edu'
        body = """\
        Advising Signup with %s CANCELLED
        Name: %s
        Email: %s
        Date: %s
        Time: %s
        Please contact support@engr.oregonstate.edu if you experience problems.
        """ % (name, student_name, student_email, dateStr, time)

        msg = MIMEText(body, 'plain')

        msg['Subject'] = 'Advising Signup with %s CANCELLED.' % name
        msg['From'] = fromAddr
        msg['To'] = toAddr

        s = smtplib.SMTP('mail.engr.oregonstate.edu')
        s.sendmail(fromAddr, toAddr, msg.as_string())
        s.quit()