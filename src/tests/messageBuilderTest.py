__author__ = 'kkozee'

import sys, os
sys.path.append(os.getcwd())

from src.builders.messageBuilder import MessageBuilder
from src.builders.appointmentBuilder import AppointmentBuilder

mb = MessageBuilder()

mb.buildMessageFromFile('cancellation.txt')

ab = AppointmentBuilder()

appt = ab.buildApptFromMessage(mb)

print appt.user
print appt.student
print appt.canceled
print appt.startDateTime
print appt.endDateTime

mb.buildMessageFromFile('email.txt')

ab = AppointmentBuilder()

appt = ab.buildApptFromMessage(mb)

print appt.user
print appt.student
print appt.canceled
print appt.startDateTime
print appt.endDateTime