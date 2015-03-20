####################################################################
    # messageBuilder.py
    # This program reads and parses email messages from file, email
    # message, or string. It then sets the different values on the
    # email message including the sender, receiver, subject, and body.
####################################################################
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

    # Opens, reads and parses a message saved to file
    def buildMessageFromFile(self, mail):
        m = open(mail, 'rb')
        # Create MIMEtext object from file message
        self.fullMsg = MIMEText(m.read())
        # Parse message from file
        m.seek(0)
        self.inMsg = email.message_from_file(m)
        self.sendAddr = self.inMsg['from']
        self.destAddr = self.inMsg['to']
        self.subject = self.inMsg['subject']

        self.body = self.inMsg.get_payload()
        self.bodyParts = self.body.split('\n')
        self.subjectParts = self.subject.split()

        return self

    # Reads and parses a passed email message
    def buildMessageFromEmail(self, mail):
        # Create MIMEtext object from email message
        self.fullMsg = MIMEMessage(mail)
        # Parse email message
        self.inMsg = mail
        self.sendAddr = self.inMsg['from']
        self.destAddr = self.inMsg['to']
        self.subject = self.inMsg['subject']

        self.body = self.inMsg.get_payload()
        self.bodyParts =  self.body
        self.subjectParts = self.subject.split()

        return self

    # Opens, reads and parses a message saved to file
    def buildMessageFromString(self, full_msg):
        # Parse message string
        self.inMsg = email.message_from_string(''.join(full_msg))

        self.destAddr = self.inMsg['To'].split(';')[1]
        self.sendAddr = self.inMsg['From']
        self.subject = self.inMsg['Subject']

        self.subjectParts = self.subject.split()
        self.body = self.inMsg.get_payload()
        self.bodyParts = self.body.split('\n')

        return self
