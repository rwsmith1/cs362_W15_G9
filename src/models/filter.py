__author__ = 'rwsmith1'

import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from src.models.base import Base


class Filter(Base):

    # Script only works when run on OSU servers.

    def __init__(self, oUser):
        self.mimeText = None
        self.calendarRequest = None
        self.user = oUser
        self.msg = MIMEMultipart('alternative')
        self.pt1 = MIMEText(self.mimeText, 'plain')
        self.pt2 = MIMEText(self.calendarRequest, 'calendar')
        self.sendAddr = "donotreply@oregonstate.edu"
        self.destAddr = self.user.getEmail()

    # Create message container

    def createMessage(self):
        self.msg['Subject'] = "New Advising Session"
        self.msg['From'] = self.sendAddr
        self.msg['To'] = self.destAddr

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
