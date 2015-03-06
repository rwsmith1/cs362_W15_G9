__author__ = 'disatapp'

from database import Database

class databaseEvent(Database):
    #
    # def __init__(self):
    #   Database.__init__(self)
        # self.q = None
        
    # Insert new Message row to table
    def createMessage(self, userName, studentName, Message):
        #self.Database()
        #self.connect()
        self.sql = "INSERT INTO Message (fkUser,fkStudent,mailbox) VALUES ((SELECT pkUser FROM User WHERE name = '%s'),(SELECT pkStudent FROM Student WHERE name = '%s'),%s)" % (userName, studentName, Message)
        return self.sql
        # self.q = self.query(self.sql)
        # return self.q       


    # Insert new Appointment row to table
    def addApp(self, userName, studentName, timeStart, date, location, canceled):
        #self.Database()
        #self.connect()
        self.sql = "INSERT INTO Appointment (fkUser,fkStudent, timeStart, data, location, canceled) VALUES ((SELECT pkUser FROM User WHERE name = '%s'),(SELECT pkStudent FROM Student WHERE name = '%s'),'%s','%s','%s','%d')" % (userName, studentName, timeStart, date, location, canceled)
        return self.sql
        # self.q =self.query(self.sql)
        # return self.q 

    #get Appointment info 
    def getApp(self, id):
#       self.Database()
        #self.connect()
        self.sql = "SELECT pkAppointment, fkUser, User.name, fkStudent, Student.name, Student.email, timeStart, location, date, canceled FROM User INNER JOIN Appointment ON User.pkUser = Appointment.fkUser INNER JOIN Student ON Appointment.fkStudent = Student.pkStudent WHERE User.pkUser = '%s' ORDER BY Appointment.date" % (id)
        return self.sql
        # self.q =self.query(self.sql)
        # return self.q 

    # Update Appintment table.
    def handleApp(self, appiontmentId, canceled=1):
        #self.connect()
        self.sql = "UPDATE Appointment SET canceled = %d WHERE pkAppointment = '%d'" % (canceled, appiontmentId)
        return self.sql
        # self.q =self.query(self.sql)
        # return self.q 

    # Get info from a student or user
    def getInfo(self, id,table=0):
#        self.Database()
        #self.connect()
        if table == 1:
            info = 'User'
        else:
            info = 'Student'
        self.sql = "SELECT name, email FROM %s WHERE pkStudent = '%d'" % (info,id)
        return self.sql
        # self.q =self.query(self.sql)
        # return self.q 

    #Get ID
    def getAppID(self, userName, nameStudent, timeStart, date):
    #        self.Database()
    #self.connect()
        self.sql = "SELECT pkAppointment FROM Appointment INNER JOIN Student ON Appointment.fkStudent = Student.pkStudent INNER JOIN User ON Appointment.fkUser = User.pkUser WHERE Student.name = '%s' AND Appointment.timeStart = %d AND Appointment.date = '%s' AND User.name = '%s'" % (info, nameStudent, timeStart, date, userName)
        # self.q =self.query(self.sql)
        # return self.q
        return self.sql