__author__ = 'kkozee'

from src.models.base import Base

class Appointment(Base):

    canceled = 0
    user = ""
    student = ""
    time = ""
    date = ""
    location = ""

    def __init__(self, id, user, student, time, date, location):
        self.id = id
        self.canceled = 0
        self.user = user
        self.student = student
        self.time = time
        self.date = date
        self.location = location

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

    def setTime(self, time):
        self.time = time
        return self.time

    def getTime(self):
        return self.time

    def setDate(self, date):
        self.date = date
        return self.date

    def getDate(self):
        return self.date

    def setLocation(self, location):
        self.location = location
        return self.location

    def getLocation(self):
        return self.location

    def setCanceled(self, canceled):
        self.canceled = canceled
        return self.canceled

    def getCanceled(self):
        return self.canceled

    def cancelAppointment(self):
        self.canceled = 1
        return self.canceled