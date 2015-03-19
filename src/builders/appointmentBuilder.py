####################################################################
    # Name: appointmentBuilder.py
    # This class parses a passed email/text message for the adviser's
    # name, student's name, appointment date, appointment time and
    # whether the message was for a new appointment or a cancellation.
    # It takes the information and creates a new appointment in the
    # database.
####################################################################
__author__ = 'kkozee'

import datetime
from src.models.appointment import Appointment
from src.models.messages import Messages

class AppointmentBuilder():

    def buildApptFromMessage(self, message):
        # Message is for new Appointment
        if message.subjectParts[0].lower() == "advising" and message.subjectParts[1].lower() == "signup" \
                and message.subjectParts[2].lower() == "with":
            name = message.subjectParts[5] + " " + message.subjectParts[3].replace(',', '')
            student = message.bodyParts[1].split("Name: ")[1]
            date = message.bodyParts[3].split("Date: ")[1]
            timeStr = message.bodyParts[4].split("Time: ")[1]

            if message.subjectParts[6] == "confirmed":
                canceled = 0
        # Message is for a Cancelled Appointment
        elif message.subjectParts[0].lower() == "advising" and message.subjectParts[1].lower() == "signup" \
                and message.subjectParts[2].lower() == "cancellation":
            name = message.bodyParts[0].split()[5] + " " + message.bodyParts[0].split()[3].replace(',', '')
            canceled = 1
            student = message.bodyParts[1].split("Name: ")[1]
            date = message.bodyParts[3].split("Date: ")[1]
            timeStr = message.bodyParts[4].split("Time: ")[1]

        # Parse date and time from strings
        dateParts = date.split(',')
        dateString = (dateParts[0] + dateParts[1][0:-2] + dateParts[2]).strip()
        startTimeStr = timeStr.split(" - ")[0]
        endTimeStr = timeStr.split(" - ")[1]

        # Create new appointment
        appt = Appointment(name, student)
        appt.setCanceled(canceled)

        studentEmail = message.bodyParts[2].split('Email: ')[1]
        appt.setStudentEmail(studentEmail)
        appt.setUserEmail(message.destAddr)

        # Convert from string to datetime
        startDateTime = datetime.datetime.strptime(startTimeStr + ' ' + dateString, '%I:%M%p %A %B %d %Y')
        endDateTime = datetime.datetime.strptime(endTimeStr + ' ' + dateString, '%I:%M%p %A %B %d %Y')
        appt.setStartDateTime(startDateTime)
        appt.setEndDateTime(endDateTime)
        
        return appt
