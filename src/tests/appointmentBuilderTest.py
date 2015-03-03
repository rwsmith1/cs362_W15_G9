__author__ = 'kkozee'

import sys
sys.path.append(os.getcwd())

from src.builders.appointmentBuilder import AppointmentBuilder

ab = AppointmentBuilder()

ab.buildApptFromMessage()