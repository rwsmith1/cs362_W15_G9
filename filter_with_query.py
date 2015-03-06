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

mb = MessageBuilder()
ab = AppointmentBuilder()

message = mb.buildMessageFromString(fullMsg)
appointment = ab.buildApptFromMessage(message)

advisorName = ""
apptStatus = ""

subjectParts = inMsg['subject'].split(' ')

if subjectParts[0] == "Advising" and subjectParts[1] == "Signup" and subjectParts[2] == "with":
    advisorName = subjectParts[3] + " " + subjectParts[4];
    if subjectParts[5] != "confirmed":
        advisorName += " " + subjectParts[5]
        apptStatus = subjectParts[6]
    else:
        apptStatus = subjectParts[5]

if subjectParts[0] == "Advising" and subjectParts[1] == "Signup" and subjectParts[2] == "Cancellation":
    # We should only need both emails, date, and time to cancel an appointment.
    apptStatus = "cancelled"

body = inMsg.get_payload()
bodyParts = body.split('\n')

studentName = bodyParts[1].split("Name: ")[1]
date = bodyParts[3].split("Date: ")[1]
timeStr = bodyParts[4].split("Time: ")[1]

'''
Create datetime object to pass to DB.
'''

dateParts = date.split(',')
dateString = (dateParts[0] + dateParts[1][0:-2] + dateParts[2]).strip()
startTimeStr = timeStr.split(" - ")[0]
endTimeStr = timeStr.split(" - ")[1]

startDateTimeObj = datetime.datetime.strptime(startTimeStr + ' ' + dateString, '%I:%M%p %A %B %d %Y')
endDateTimeObj = datetime.datetime.strptime(endTimeStr + ' ' + dateString, '%I:%M%p %A %B %d %Y')


# Create email.
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = sendAddr		# Could probably hard code this.
msg['To'] = destAddr

# Create iCalendar object.
timecreated = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())
uid = timecreated + "@" + socket.gethostname()
timestart = startDateTimeObj.strftime('%Y%m%dT%H%M%S')
timeend = endDateTimeObj.strftime('%Y%m%dT%H%M%S')

##############################################
#############connect to database##############
##############################################

db = Database()
db.connect() #might not need

#queries
q = databaseEvent()
#username, studentname, uid, time, data, location, canceled
sql = q.addApp(advisorName, studentName, uid, INSERT_TIME_HERE, INSERT_DATE_HERE)
add = db.update(sql)

#return student name, time, date, uid
sql = getAppID(advisorName, studentName, INSERT_TIME_HERE, INSERT_DATE_HERE)
array = db.query(sql)

#Kevin might want this in a message object
studentVar = str(array[0])
timeVar = str(array[1])
dataVar = str(array[2])
uidVar = str(array[3])

##############################################

mimeText = ""
calendarRequest ="""\
BEGIN:VCALENDAR
METHOD:REQUEST
PRODID:MAST
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
""" % (timecreated, timecreated, timestart, timeend, timecreated, inMsg['subject'], uid, body)

# Variable to hold the calendar request
# (for when we figure out how to do that.)

pt1 = MIMEText(mimeText, 'plain')
pt2 = MIMEText(calendarRequest, 'calendar')
pt2.add_header('Content-Disposition', 'attachment', method='REQUEST')

# Attach parts into message container.
msg.attach(pt1)
msg.attach(pt2)

# Send the message via OSU Engineering server. We could change this to gmail for
# ease of testing. Any opinions?

s = smtplib.SMTP('mail.engr.oregonstate.edu')
s.sendmail(sendAddr, destAddr, msg.as_string())
s.quit()
exit()