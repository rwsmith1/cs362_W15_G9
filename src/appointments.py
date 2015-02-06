__author__ = 'kkozee'


class Appointments(object):

    id = 0
    user = ""
    student = ""
    time = ""
    date = ""
    location = ""

    def setID(self, id):
        self.id = id
        return self.id

    def getID(self):
        return self.id

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