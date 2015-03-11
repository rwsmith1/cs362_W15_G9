__author__ = 'kkozee'

import datetime
from src.models.appointment import Appointment
from src.models.messages import Messages

class AppointmentBuilder():

    def buildApptFromMessage(self, message):

        if message.subjectParts[0].lower() == "advising" and message.subjectParts[1].lower() == "signup" and message.subjectParts[2].lower() == "with":
            name = message.subjectParts[5] + " " + message.subjectParts[3].replace(',', '')
            student = message.bodyParts[1].split("Name: ")[1]
            date = message.bodyParts[3].split("Date: ")[1]
            timeStr = message.bodyParts[4].split("Time: ")[1]

            if message.subjectParts[6] == "confirmed":
                canceled = 0

        elif message.subjectParts[0].lower() == "advising" and message.subjectParts[1].lower() == "signup" and message.subjectParts[2].lower() == "cancellation":
            name = message.bodyParts[0].split()[5] + " " + message.bodyParts[0].split()[3].replace(',', '')
            canceled = 1
            student = message.bodyParts[1].split("Name: ")[1]
            date = message.bodyParts[3].split("Date: ")[1]
            timeStr = message.bodyParts[4].split("Time: ")[1]

        dateParts = date.split(',')
        dateString = (dateParts[0] + dateParts[1][0:-2] + dateParts[2]).strip()

        startTimeStr = timeStr.split(" - ")[0]
        endTimeStr = timeStr.split(" - ")[1]

        appt = Appointment(name, student)
        appt.setCanceled(canceled)

        studentEmail = message.bodyParts[2].split('Email: ')[1]

        appt.setStudentEmail(studentEmail)

        startDateTime = datetime.datetime.strptime(startTimeStr + ' ' + dateString, '%I:%M%p %A %B %d %Y')
        endDateTime = datetime.datetime.strptime(endTimeStr + ' ' + dateString, '%I:%M%p %A %B %d %Y')
        
        appt.setStartDateTime(startDateTime)
        appt.setEndDateTime(endDateTime)
        
        return appt
