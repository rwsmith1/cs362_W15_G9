__author__ = 'roger'

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from users import Users

class Filter():

    # Script only works when run on OSU servers.


    user = ""
    sendAddr = "" # sendAddr == my email address
    destAddr = "" # destAddr == recipient's email address
    msg = ""
    pt1 = ""
    pt2 = ""

    def __init__(self, oUser):
        self.user = oUser
        self.msg = MIMEMultipart('alternative')
        self.pt1 = MIMEText(MIMEText, 'plain')
        self.pt2 = MIMEText(calendarRequest, 'calendar')
        self.sendAddr = "donotreply@oregonstate.edu"
        self.destAddr = self.user.getEmail()

    # Create message container

    def createMessage(self):
        self.msg['Subject'] = "New Advising Session"
        self.msg['From'] = self.sendAddr
        self.msg['To'] = self.destAddr

    mimeText = ""
    calendarRequest = ""  # Variable to hold the calendar request

    def setParts(self):
        self.pt2.add_header('Content-Disposition', 'attachment', method='REQUEST')

    # Attach parts into message container.

    def attachParts(self):
        self.msg.attach(self.pt1)
        self.msg.attach(self.pt2)

    # Send the message via OSU Engineering server. We could change this to gmail for
    # ease of testing. Any opinions?

    def sendMessage(self):
        s = smtplib.SMTP('mail.engr.oregonstate.edu')
        s.sendmail(self.sendAddr, self.destAddr, self.msg.as_string())
        s.quit()
