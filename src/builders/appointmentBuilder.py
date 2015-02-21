__author__ = 'kkozee'

from src.models.appointment import Appointment
from src.models.messages import Messages

class AppointmentBuilder(Appointment, Messages):

    def __init__(self, id, user, student, time, date, location):
        super(AppointmentBuilder, self).__init__(id, user, student, time, date, location)

    def buildApptFromMessage(self):
        if self.subjectParts[0].lower() == "advising" and self.subjectParts[1].lower() == "signup" and self.subjectParts[2].lower() == "with":
            self.user.name = self.subjectParts[3] + " " + self.subjectParts[4]

            if self.subjectParts[6] == "confirmed":
                self.student.setName(self.subjectParts[5])
                self.setCanceled(0)

        if self.subjectParts[0].lower() == "advising" and self.subjectParts[1].lower() == "signup" and self.subjectParts[2].lower() == "cancellation":
            self.setCanceled(1)

        # We should only need both emails, date, and time to cancel an appointment
        self.student.setName(self.bodyParts[1].split("Name: ")[1])
        self.setDate(self.bodyParts[3].split("Date: ")[1])
        self.setTime(self.bodyParts[4].split("Time: ")[1])
