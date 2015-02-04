#!/usr/bin/env python

# Script only works when run on OSU servers.

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# sendAddr == my email address
sendAddr = "do.not.reply@oregonstate.edu"

# destAddr == recipient's email address
# Currently set to my email address.
# Please change if you are going to do any testing.
destAddr = "smithrog@onid.oregonstate.edu"

# Create message container
msg = MIMEMultipart('alternative')
msg['Subject'] = "New Advising Session"
msg['From'] = sendAddr
msg['To'] = destAddr

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
