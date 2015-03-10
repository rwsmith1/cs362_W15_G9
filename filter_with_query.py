__author__ = 'rwsmi_000'

import datetime
import email
import fileinput
import re
import smtplib
import socket
import string
import sys
import time
from src.database.database import Database
from src.database.databaseEvent import databaseEvent
from src.builders.messageBuilder import MessageBuilder
from src.builders.appointmentBuilder import AppointmentBuilder
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Read in message from the standard input.

#fullMsg = sys.stdin.readlines()

fullMsg = """\
From: do.not.reply@engr.orst.edu
Sent: Monday, November 26, 2012 19:15
To: smithrog@engr.oregonstate.edu; smithrog@onid.oregonstate.edu
Subject: Advising Signup with McGrath, D Kevin confirmed for Brabham, Matthew Lawrence
Advising Signup with McGrath, D Kevin confirmed
Name: REDACTED
Email: REDACTED@oregonstate.edu
Date: Wednesday, November 21st, 2012
Time: 1:00pm - 1:15pm
Please contact support@engr.oregonstate.edu if you experience problems
"""

'''
fullMsg = """\
    From: do.not.reply@engr.orst.edu
Sent: Thursday, November 15, 2012 10:11
To: smithrog@engr.oregonstate.edu
Subject: Advising Signup Cancellation
Advising Signup with McGrath, D Kevin CANCELLED
Name: REDACTED
Email: REDACTED@engr.orst.edu
Date: Thursday, November 15th, 2012
Time: 11:00am - 11:15am
Please contact support@engr.oregonstate.edu if you experience problems."""
'''

# REDACTED@engr.orst.edu; dmcgrath@eecs.oregonstate.edu

# Build message and appointment objects from inputted string.

mb = MessageBuilder()
ab = AppointmentBuilder()

message = mb.buildMessageFromString(fullMsg)
appointment = ab.buildApptFromMessage(message)

# Create email.
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Message from EECS Advising'   #message.subject
msg['From'] = message.sendAddr		# Could probably hard code this.
msg['To'] = message.destAddr

# Create iCalendar object.
timecreated = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())
uid = timecreated + "@" + socket.gethostname()
timestart = appointment.getStartDateTime().strftime('%Y%m%dT%H%M%S')
timeend = appointment.getEndDateTime().strftime('%Y%m%dT%H%M%S')
calendarRequest = ""
mimeText = ""

##############################################
#############connect to database##############
##############################################

db = Database()

try:
    db.connect() #might not need

except:
    print "Could not connect to db."
    exit()

print "DB connected."

#queries
q = databaseEvent()

# If the appointment email is a cancellation, get the original uid from the db so we can include it in
# the cancelation iCalendar event. Also, mark event as cancelled in db.

print "Check for cancelled."

if appointment.getCanceled():
    print "Request is a cancellation."
    # array = getAppID(db, advisorName, studentName, INSERT_TIMESTART_HERE, INSERT_DATE_HERE)

    try:
        print "Getting appt info."
        array = q.getAppID(db, appointment.getUser(), appointment.getStudent(), appointment.getStartDateTime().strftime('%H:%M:%S'), appointment.getStartDateTime().strftime('%Y-m-%d'))
    except:
        print "Could not get appt. info."
        exit()

    studentVar = str(array[0])
    uidVar = str(array[1])
    timeVar = str(array[2])
    dataVar = str(array[3])


    try:
        print "Setting appointment cancelled."
        db.query("UPDATE Appointment SET canceled = 1 WHERE pkAppointment = %s" % (studentVar))

    except:
        print "Could not set cancellation in db."
        exit()


    calendarRequest ="""\
    BEGIN:VCALENDAR
    METHOD:CANCEL
    PRODID:FILTER
    VERSION:2.0
    BEGIN:VEVENT
    CREATED:%s
    DTSTAMP:%s
    DTSTART:%s
    DTEND:%s
    LAST-MODIFIED:%s
    SUMMARY:%s
    UID:%s
    DESCRIPTION:%s
    SEQUENCE:0
    STATUS:CANCELLED
    TRANSP:OPAQUE
    END:VEVENT
    END:VCALENDAR
    """ % (timecreated, timecreated, timestart, timeend, timecreated, message.subject, uidVar, message.body)


# If the request is not a cancellation, add it to the db.
else:
    print "Message is an appointment request."
    #insert
    # db, userName, studentName, timeStart, date, location, uId, canceled=0
    # q.addApp(db, advisorName, studentName, INSERT_TIME_START_HERE, INSERT_TIME_END_HERE, INSERT_DATE_HERE, uid)
    try:
        q.addApp(db, appointment.getUser(), appointment.getStudent(), appointment.getStartDateTime().strftime('%H:%M:%S'), appointment.getEndDateTime().strftime('%H:%M:%S'), appointment.getStartDateTime().strftime('%Y-m-%d'), uid)
    except:
        print "Could not add appt to db."
        exit()

    calendarRequest ="""\
    BEGIN:VCALENDAR
    METHOD:REQUEST
    PRODID:FILTER
    VERSION:2.0
    BEGIN:VEVENT
    CREATED:%s
    DTSTAMP:%s
    DTSTART:%s
    DTEND:%s
    LAST-MODIFIED:%s
    SUMMARY:%s
    UID:%s
    DESCRIPTION:%s
    SEQUENCE:0
    STATUS:CONFIRMED
    TRANSP:OPAQUE
    END:VEVENT
    END:VCALENDAR
    """ % (timecreated, timecreated, timestart, timeend, timecreated, message.subject, uid, message.body)

db.close()

print "DB closed."

#pass db object in the first field
#return student name, time, date, uid

##############################################

# Assemble email and iCalendar object.

pt1 = MIMEText(mimeText, 'plain')
pt2 = MIMEText(calendarRequest, 'calendar')
pt2.add_header('Content-Disposition', 'attachment', method='REQUEST')

# Attach parts into message container.
msg.attach(pt1)
msg.attach(pt2)

# Send the message via OSU Engineering server.

print "Sending email."

s = smtplib.SMTP('mail.engr.oregonstate.edu')
s.sendmail(message.sendAddr, message.destAddr, msg.as_string())
s.quit()
exit()