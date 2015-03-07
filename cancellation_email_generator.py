__author__ = 'rwsmi_000'

import smtplib
from src.database.databaseEvent import Database
from email.mime.text import MIMEText
from src.database.database import Database
from src.database.databaseEvent import databaseEvent

db = Database()
db.connect() # might not need, per Pavin.

# Add DB queries here.

# Fill these string values from the DB:

advisor_name = ''
advisor_email = ''
student_name = ''
student_email = ''
date_of_appt = ''
time_of_appt = ''

# These strings should be in the same format as given in the sample cancellation email.
# Date should be in the format as given in the sample message, e.g. Thursday, November 15th, 2012.
# Same with time, e.g. 11:00am - 11:15am.

fromAddr = 'do.not.reply@engr.orst.edu'
toAddr = advisor_email

body = """\
Advising Signup with %s CANCELLED
Name: %s
Email: %s
Date: %s
Time: %s
Please contact support@engr.oregonstate.edu if you experience problems.
""" % (advisor_name, student_name, student_email, date_of_appt, time_of_appt)

msg = MIMEText(body, 'plain')

# fromAddr == the sender's email address
# toAddr == the recipient's email address
msg['Subject'] = 'Advising Signup Cancellation.'
msg['From'] = fromAddr
msg['To'] = toAddr

# Send the message via engr SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('mail.engr.oregonstate.edu')
s.sendmail(fromAddr, toAddr, msg.as_string())
s.quit()