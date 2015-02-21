#!/usr/bin/python

import sys
import curses
from curses import wrapper
import MySQLdb


def main(stdscr):
    # get username and password from command line:
    args = len(sys.argv)
    if args < 3:
        sys.exit("Invalid Input: include username and password in command line")
    userName = sys.argv[1]
    userPass = sys.argv[2]
    results = ""
    userId = ""
    password = ""
    email = ""
    n = 0

    # establish database connection:
    db = MySQLdb.connect("mysql.eecs.oregonstate.edu", "cs419-g9", "h8RWjc3qh9QnAJ42", "cs419-g9")
    cursor = db.cursor()

    # query the database
    try:
        sqlUser = "SELECT * FROM User WHERE name = '%s'" % (userName)
        cursor.execute(sqlUser)
        results = cursor.fetchone()
        if results is not None:
            userId = results[0]
            password = results[2]
            email = results[3]
    except:
        print "Error"

    # check for valid user/password
    if results is None:
        sys.exit("Invalid Username")
    if password != userPass:
        sys.exit("Invalid Password")

    # clear screen
    stdscr.clear()
    # turn off cursor
    curses.curs_set(False)

    # main menu program loop:
    while n != ord('3'):
        stdscr.clear()
        stdscr.addstr('Welcome ' + userName)
        stdscr.addstr(2, 0, 'Enter a Number:')
        stdscr.addstr(3, 2, '1 - View Schedule')
        stdscr.addstr(4, 2, '2 - Cancel Appointment')
        stdscr.addstr(5, 2, '3 - Exit')
        stdscr.refresh()
        n = stdscr.getch()
        # view the schedule:
        if n == ord('1'):
            stdscr.clear()
            stdscr.addstr('Press Any Key for Main Menu')
            stdscr.addstr(2, 0, 'DATE')
            stdscr.addstr(2, 15, 'TIME')
            stdscr.addstr(2, 30, 'STUDENT')
            stdscr.addstr(2, 50, 'STUDENT EMAIL')
            sql = "SELECT * FROM Appointment WHERE fkUser = '%d' ORDER BY date" % (userId)
            cursor.execute(sql)
            appts = cursor.fetchall()
            row = 3
            for app in appts:
                studentId = app[2]
                sql = "SELECT name, email FROM Student WHERE pkStudent = '%d'" % (studentId)
                cursor.execute(sql)
                student = cursor.fetchone()
                time = str(app[3])
                date = str(app[4])
                #location = app[5]
                stdscr.addstr(row, 0, date)
                stdscr.addstr(row, 15, time)
                stdscr.addstr(row, 30, student[0])
                stdscr.addstr(row, 50, student[1])
                row += 1

            stdscr.refresh()
            stdscr.getkey()
        # cancel an appointment
        if n == ord('2'):
            stdscr.clear()
            stdscr.addstr('Cancel view')
            stdscr.refresh()
            stdscr.getkey()

    # close database connection:
    db.close()

# curses wrapper initiates and exits window/curses
wrapper(main)
