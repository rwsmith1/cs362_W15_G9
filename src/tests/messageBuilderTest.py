__author__ = 'kkozee'

import sys, os
sys.path.append(os.getcwd())

from src.builders.messageBuilder import MessageBuilder

mb = MessageBuilder()

mb.buildMessageFromEmail('email.txt')