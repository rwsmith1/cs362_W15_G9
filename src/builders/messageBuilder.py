__author__ = 'kkozee'

import sys

sys.path.append('/Users/kkozee/PycharmProjects/cs362_W15_G9/')

import email
from email.mime.text import MIMEText
from src.models.messages import Messages

class MessageBuilder(Messages):

    def __init__(self):
        super(MessageBuilder, self).__init__()

    def buildMessageFromEmail(self, mail):
        m = open(mail, 'rb')

        self.fullMsg = MIMEText(m.read())

        self.inMsg = email.message_from_string(''.join(self.fullMsg))

        self.sendAddr = self.inMsg['from']
        self.destAddr = self.inMsg['to']
        self.subject = self.inMsg['subject']

        self.body = self.inMsg.get_payload()
        self.bodyParts = self.body.split('\n')

        self.subjectParts = self.inMsg['subject'].split(' ')

        return self