__author__ = 'kkozee'

import sys, os
sys.path.append(os.getcwd())

from src.models.mailbox import Mailbox
from src.builders.messageBuilder import MessageBuilder

m = Mailbox()

m.connectAndLogin()

for i in m.getMail():
    mb = MessageBuilder()
    mb.buildMessageFromEmail(i)
    print mb.subject

m.disconnectAndLogout()