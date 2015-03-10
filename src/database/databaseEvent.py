__author__ = 'disatapp'

from database import Database

class databaseEvent(Database):
    #
	# def __init__(self):
	# 	Database.__init__(self)
    #   self.q = None

    ####################################################################      
    # Insert new Message row to table
    # Parameter: db = database object
    ####################################################################
    def createMessage(self, db, userName, studentName, Message):
        #self.Database()
        #self.connect()
        self.sql = "INSERT INTO Message (fkUser,fkStudent,mailbox) VALUES ((SELECT pkUser FROM User WHERE name = '%s'),(SELECT pkStudent FROM Student WHERE name = '%s'),%s)" % (userName, studentName, Message)
        db.update(self.sql)
        
    ####################################################################
    # Insert new Appointment row to table location null
    # Parameter: db = database object
    ####################################################################
    def addApp(self, db, userName, studentName, timeStart, timeEnd, date, uId, canceled=0):
        # self.Database()
        # self.connect()
        # userName = appObj.
        # studentName = appObj.
        # uId = appObj.
        # timeStart = appObj.
        # date = appObj.
        self.sql = "INSERT INTO Appointment (fkUser,fkStudent, timeStart, timeEnd, date, canceled, uId) VALUES ((SELECT pkUser FROM User WHERE name = '%s'),(SELECT pkStudent FROM Student WHERE name = '%s'),'%s', '%s', '%s','%d','%s')" % (userName, studentName, timeStart, timeEnd, date, canceled, uId)
        db.update(self.sql)

    ####################################################################
    # Update Appintment table. 
    # Parameter: db = database object
    ####################################################################
    def handleApp(self, db, appiontmentId, canceled=1):
        self.sql = "UPDATE Appointment SET canceled = %d WHERE pkAppointment = '%d'" % (canceled, appiontmentId)
        db.update(self.sql)

    ####################################################################
    # Get info from a student or user
    # Parameter: db = database object
    # Returns:
    #       0. user name
    #       1. email
    ####################################################################
    def getInfo(self, db, name, table=0):
        # self.Database()
        # self.connect()
        if table == 1:
            info = 'User'
        else:
            info = 'Student'
        self.sql = "SELECT * FROM %s WHERE name = '%s'" % (info, name)
        q = db.query(self.sql)
        return q 

    ####################################################################
    # Get Appointment ID & Unique ID
    # Parameter: db = database object
    # Returns:
    #       0. Appointment Id
    #       1. uId
    #       2. timeStart
    #       3. date
    ####################################################################
    def getAppID(self, db, userName, studentName, timeStart, date):
        self.sql = "SELECT pkAppointment, uId, timeStart, date FROM Appointment INNER JOIN Student ON Appointment.fkStudent = Student.pkStudent INNER JOIN User ON Appointment.fkUser = User.pkUser WHERE Student.name = '%s' AND Appointment.timeStart = %d AND Appointment.date = '%s' AND User.name = '%s'" % (info, studentName, timeStart, date, userName)
        q = db.query(self.sql)
        return q

    ####################################################################
    # Get Appointment info 
    # Parameter: db = database object
    # Returns:
    #       0. Appointment Id
    #       1. fkUser
    #       2. user name
    #       3. fkStudent
    #       4. student name
    #       5. email
    #       6. timeStart
    #       7. location
    #       8. date, 
    #       9. concanled
    #       10. uId
    ####################################################################
    def getApp(self, db, id):
        self.sql = "SELECT pkAppointment, fkUser, User.name, fkStudent, Student.name, Student.email, timeStart, location, date, canceled, uId FROM User INNER JOIN Appointment ON User.pkUser = Appointment.fkUser INNER JOIN Student ON Appointment.fkStudent = Student.pkStudent WHERE User.pkUser = '%s' ORDER BY Appointment.date" % (id)
        self.q = db.queryall(self.sql)
        return self.q 
