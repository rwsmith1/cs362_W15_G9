#!/usr/bin/env python

# Script only works when run on OSU servers.

import smtplib
import email
import sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# This should allow messages to be piped through by the procmail filter,
# but I'm not sure how to test it. It works when mail data is entered
# manually on the console.

fullMsg = sys.stdin.readlines()

inMsg = email.message_from_string(''.join(fullMsg))

# destAddr == recipient's email address
destAddr = inMsg['to']
sendAddr = inMsg['from']		# Could probably hard code this.
subject = inMsg['subject']
advisorName = ""
apptStatus = ""

# Pulls the body.
body = inMsg.get_payload()
bodyParts = body.split('\n')

# This is to split the multiple destination addresses ("REDACTED@.."), if
# necessary.

# destAddrs = inMsg['to'].split('; ')

# sendAddr == my email address
# sendAddr = "do.not.reply@oregonstate.edu"

# This parsing is a bit "brute force" for my liking. Anyone have a better
# ideas how to pull this info?

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
        
studentName = bodyParts[1].split("Name: ")[1]
date = bodyParts[3].split("Date: ")[1]
time = bodyParts[4].split("Time: ")[1]

# Database interaction script call goes here...

# Create message container
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = sendAddr		# Could probably hard code this.
msg['To'] = destAddr
# msg['To'] = destAddrs[1]

# Create iCalendar object.
mimeText = ""
calendarRequest = ""  # Variable to hold the calendar request
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
