__author__ = 'kkozee'

import sys

sys.path.append('/Users/kkozee/PycharmProjects/cs362_W15_G9/')

import email
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage
from src.models.messages import Messages

class MessageBuilder(Messages):

    def __init__(self):
        super(MessageBuilder, self).__init__()

    def buildMessageFromFile(self, mail):
        m = open(mail, 'rb')

        self.fullMsg = MIMEText(m.read())

        m.seek(0)
        self.inMsg = email.message_from_file(m)

        self.sendAddr = self.inMsg['from']
        self.destAddr = self.inMsg['to']
        self.subject = self.inMsg['subject']

        self.body = self.inMsg.get_payload()
        self.bodyParts = self.body.split('\n')

        self.subjectParts = self.subject.split()

        return self

    def buildMessageFromEmail(self, mail):
        self.fullMsg = MIMEMessage(mail)

        self.inMsg = mail

        self.sendAddr = self.inMsg['from']
        self.destAddr = self.inMsg['to']
        self.subject = self.inMsg['subject']

        self.body = self.inMsg.get_payload()
        self.bodyParts =  self.body

        self.subjectParts = self.subject.split()

        return self