__author__ = 'kkozee'

import imaplib
import email
import sys, os
sys.path.append(os.getcwd())
from src.builders.appointmentBuilder import AppointmentBuilder
from src.builders.messageBuilder import MessageBuilder

class Mailbox:

    def __init__(self):
        self.server = "imap.gmail.com"
        self.port = 993
        self.emailAddr = "kozeepythontest@gmail.com"
        self.emailPass = "GoBeavsOSU345"
        self.connection = None
        self.result = None
        self.message = []

    def setEmailAddr(self, emailAddr):
        self.emailAddr = emailAddr

    def getEmailAddr(self):
        return self.emailAddr

    def setEmailPass(self, emailPass):
        self.emailPass = emailPass

    def getEmailPass(self):
        return self.emailPass

    def connectAndLogin(self):
        self.connection = imaplib.IMAP4_SSL(self.server, self.port)
        self.connection.login(self.emailAddr, self.emailPass)
        self.connection.select('"[Gmail]/All Mail"')

    def getMail(self):
        self.result, data = self.connection.uid('search', None, "ALL")
        if self.result == 'OK':
            for i in data[0].split():
                self.result, data = self.connection.uid('fetch', i, '(RFC822)')
            if self.result == 'OK':
                self.message.append(email.message_from_string(data[0][1]))
            else:
                self.message.append("An error occured.")
        return self.message

    def disconnectAndLogout(self):
        self.connection.close()
        self.connection.logout()