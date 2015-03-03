__author__ = 'kkozee'

from src.models.base import Base

class Appointment(Base):

        def __init__(self, id, user, student):
        self.id = id
        self.canceled = 0
        self.user = user
        self.student = student
        self.startDateTime = None
        self.endDateTime = None

    def setUser(self, user):
        self.user = user
        return self.user

    def getUser(self):
        return self.user

    def setStudent(self, student):
        self.student = student
        return self.student

    def getStudent(self):
        return self.student

    def setStartDateTime(self, startDateTime):
        self.startDateTime = startDateTime
        return self.startDateTime
    
        def getStartDateTime(self):
        return self.startDateTime

    def setEndDateTime(self, endDateTime):
        self.endDateTime = endDateTime
        return self.endDateTime

    def getEndDateTime(self):
        return self.endDateTime

    def setCanceled(self, canceled):
        self.canceled = canceled
        return self.canceled

    def getCanceled(self):
        return self.canceled

    def cancelAppointment(self):
        self.canceled = 1
        return self.canceled
