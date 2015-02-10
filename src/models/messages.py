__author__ = 'kkozee'

import sys
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.models.base import Base
from src.builders.messageBuilder import MessageBuilder

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

    def buildMessageFromEmail(self, mail):
        message = MessageBuilder()
        message.buildMessageFromEmail(mail)

        return message