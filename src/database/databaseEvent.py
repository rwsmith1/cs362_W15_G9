####################################################################
    # Name: databaseEvent.py
    # This program makes queries to the database. The purpose of each
    # function is outline below.
####################################################################
__author__ = 'disatapp'

import time
import datetime
from database import Database
from src.builders.appointmentBuilder import AppointmentBuilder

class databaseEvent(Database):
    ####################################################################
    # Insert new Message row to table
    # Parameter: db = database object
    ####################################################################
    def _createMessage(self, db, userEmail, studentName, Message):
        self.sql = "INSERT INTO Message (fkUser,fkStudent,mailbox) " \
                   "VALUES ((SELECT pkUser FROM User WHERE email = '%s'),(SELECT pkStudent FROM Student " \
                   "WHERE name = '%s'),%s)" % (userEmail, studentName, Message)
        db.update(self.sql)

    ####################################################################      
    # Insert new user row to table
    # Parameter: db = database object
    ####################################################################
    def _createUser(self, db, fName, lName, password, email):
        self.sql = "INSERT INTO User (fname, lname, password, email) " \
                   "VALUES (%s,%s,%s,%s,%s)" % (fName, lName, password, email)
        db.update(self.sql)

    ####################################################################      
    # Insert new Student row to table
    # Parameter: db = database object
    ####################################################################
    def _createStudent(self, db, studentName, studentEmail):
        self.sql = "INSERT INTO Student (name, email) VALUES ('%s','%s')" % (studentName, studentEmail)
        db.update(self.sql)
        
    ####################################################################
    # Insert new Appointment row to table location null
    # Parameter: db = database object
    ####################################################################
    def addApp(self, db, appointment, uId, canceled=0):
        #user = appointment.getUser()
        userEmail = appointment.getUserEmail()
        studentName = appointment.getStudent()
        studentEmail = appointment.getStudentEmail()
        timeStart = appointment.getStartDateTime().strftime('%H:%M:%S')
        timeEnd = appointment.getEndDateTime().strftime('%H:%M:%S')
        date = appointment.getStartDateTime().strftime('%Y-%m-%d')

        if not self.getInfo(db, studentEmail, 1):
            self._createStudent(db, studentName, studentEmail)

        if self.getInfo(db, userEmail):
            self.sql = "INSERT INTO Appointment (fkUser,fkStudent,timeStart, timeEnd, date, canceled, uId) " \
                       "VALUES ((SELECT pkUser FROM User WHERE email = '%s')," \
                       "(SELECT pkStudent FROM Student WHERE email = '%s'),'%s', '%s', '%s','%d','%s')" % \
                       (userEmail, studentEmail, timeStart, timeEnd, date, canceled, uId)
            db.update(self.sql)

    ####################################################################
    # Update Appointment to cancelled.
    # Parameter: db = database object
    ####################################################################
    def handleApp(self, db, appointmentId, canceled=1):
        self.sql = "UPDATE Appointment SET canceled = %d WHERE pkAppointment = '%d'" % (canceled, appointmentId)
        db.update(self.sql)

    ####################################################################
    # Get info from a student or user
    # Parameter: db = database object, email of user or student
    # Returns:
    #       0. student name
    #       1. email
    ####################################################################
    def getInfo(self, db, email, table=0):
        if table == 0:
            info = 'User'
        else:
            info = 'Student'
        self.sql = "SELECT * FROM `%s` WHERE email = '%s'" % (info, email)
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
    def getAppID(self, db, appointment):
        userEmail = appointment.getUserEmail()
        studentName = appointment.getStudent()
        timeStart = appointment.getStartDateTime().strftime('%H:%M:%S')
        date = appointment.getStartDateTime().strftime('%Y-%m-%d')
        self.sql = "SELECT pkAppointment, uId, timeStart, date FROM Appointment " \
                   "INNER JOIN Student ON Appointment.fkStudent = Student.pkStudent " \
                   "INNER JOIN User ON Appointment.fkUser = User.pkUser " \
                   "WHERE Student.name = '%s' AND Appointment.timeStart = '%s' AND Appointment.date = '%s' " \
                   "AND User.email = '%s'" % (studentName, timeStart, date, userEmail)

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
    #       8. date
    #       9. canceled
    #       10. uId
    ####################################################################
    def getApp(self, db, id):
        self.sql = "SELECT pkAppointment, fkUser, User.name, fkStudent, Student.name, Student.email, " \
                   "timeStart, timeEnd, location, date, canceled, uId FROM User " \
                   "INNER JOIN Appointment ON User.pkUser = Appointment.fkUser " \
                   "INNER JOIN Student ON Appointment.fkStudent = Student.pkStudent " \
                   "WHERE User.pkUser = '%s' ORDER BY Appointment.date" % (id)
        self.q = db.queryall(self.sql)
        return self.q 
