#!/usr/bin/python
####################################################################
    # Name: filter.py
    # Parameter: useremail password
    # This program reads an email message from the standard input and
    # from that builds a message (either for a new appointment or
    # a cancelled appointment) and an iCalendar appointment to be
    # sent to the Advisor. If it's a new appointment it is added to
    # the database, if it's a canceled appointment it is set to 
    # "canceled" in the database.
####################################################################
__author__ = 'rwsmi_000'

import sys, os
sys.path.append(os.getcwd())

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

fullMsg = sys.stdin.readlines()

'''
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
'''
fullMsg = """\
    From: do.not.reply@engr.orst.edu
Sent: Thursday, November 15, 2012 10:11
To: smithrog@engr.oregonstate.edu; smithrog@onid.oregonstate.edu
Subject: Advising Signup Cancellation
Advising Signup with McGrath, D Kevin CANCELLED
Name: REDACTED
Email: REDACTED@engr.orst.edu
Date: Wednesday, November 21st, 2012
Time: 1:00pm - 1:15pm
Please contact support@engr.oregonstate.edu if you experience problems."""
'''
'''
fullMsg = """\
    From: do.not.reply@engr.orst.edu
Sent: Thursday, November 15, 2012 10:11
To: smithrog@engr.oregonstate.edu; smithrog@onid.oregonstate.edu
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

db.connect() #might not need

#queries
q = databaseEvent()

print "Check for cancelled."

if appointment.getCanceled():

    # If the appointment email is a cancellation, get the original uid from the db so we can include it in
    # the cancelation iCalendar event. Also, mark event as cancelled in db.

    print "Request is a cancellation."

    # Get info re: existing appointment from db.

    array = q.getAppID(db, appointment)

    #       0. Appointment Id
    #       1. uId
    #       2. timeStart
    #       3. date

    # Cancel appointment in DB

    q.handleApp(db, array[0])

   # Set calendar request attributes for cancellation.

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
""" % (timecreated, timecreated, timestart, timeend, timecreated, message.subject, array[1], message.body)


else:

    q.addApp(db, appointment, uid)
    # If the request is not a cancellation, add it to the db and send out new icalendar event.

    print "Message is an appointment request."

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
