####################################################################
    # Name: messages.py
    # Initializes the parts of an email message to be used by other
    # classes.
####################################################################
__author__ = 'kkozee'

import sys

sys.path.append('/Users/kkozee/PycharmProjects/cs362_W15_G9/')

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.models.base import Base

class Messages(Base):

    def __init__(self):
        self.fullMsg = None
        self.inMsg = None
        self.sendAddr = None
        self.destAddr = None
        self.subject = None
        self.body = None
        self.bodyParts = None
        self.subjectParts = None
        self.mimeText = None
        self.calendarRequest = None
        self.msg = MIMEMultipart('alternative')
        self.pt1 = MIMEText(self.mimeText, 'plain')
        self.pt2 = MIMEText(self.calendarRequest, 'calendar')