__author__ = 'kkozee'

import datetime
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
        date = self.bodyParts[3].split("Date: ")[1]
        timeStr = self.bodyParts[4].split("Time: ")[1]
        
        dateParts = date.split(',')
        dateString = (dateParts[0] + dateParts[1][0:-2] + dateParts[2]).strip()
        startTimeStr = timeStr.split(" - ")[0]
        endTimeStr = timeStr.split(" - ")[1]

        startDateTime = datetime.datetime.strptime(startTimeStr + ' ' + dateString, '%I:%M%p %A %B %d %Y')
        
        endDateTime = datetime.datetime.strptime(endTimeStr + ' ' + dateString, '%I:%M%p %A %B %d %Y')
        
        self.setStartDateTime(startDateTime)
        
        self.setEndDateTime(endDateTime)
        
        return self
