__author__ = 'rwsmith1'

import datetime
import time
import smtplib
from src.models.base import Base

class Filter(Base):

    # Script only works when run on OSU servers.

    def __init__(self, oUser, oStudent, oAppt, oMessage):
        self.user = oUser
        self.student = oStudent
        self.appointment = oAppt
        self.message = oMessage

    # Create message container

    def createMessage(self):
        self.message.msg['Subject'] = "New Advising Session"
        self.message.msg['From'] = self.message.sendAddr
        self.message.msg['To'] = self.message.destAddr

    def setParts(self):
        self.message.pt2.add_header('Content-Disposition', 'attachment', method='REQUEST')

    # Attach parts into message container.

    def attachParts(self):
        self.message.msg.attach(self.message.pt1)
        self.message.msg.attach(self.message.pt2)

    # Send the message via OSU Engineering server. We could change this to gmail for
    # ease of testing. Any opinions?

    def sendMessage(self):
        s = smtplib.SMTP('mail.engr.oregonstate.edu')
        s.sendmail(self.message.sendAddr, self.message.destAddr, self.message.msg.as_string())
        s.quit()

    def createCalObj(self):
        timecreated = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())
        uid = timecreated + "@" + socket.gethostname()
        timestart = self.appointment.startDateTime.strftime('%Y%m%dT%H%M%S')
        timeend = self.appointment.endDateTime.strftime('%Y%m%dT%H%M%S')

        mimeText = ""
        calendarRequest ="""\
        BEGIN:VCALENDAR
        METHOD:REQUEST
        PRODID:FILTER
        VERSION:2.0
        BEGIN:VEVENT
        CREATED:%s
        DTSTAMP:%s
        DTSTART:%s
        DTEND:%s
        LAST-MODIFIED:%s
        SUMMARY:%s
        UID:%s
        DESCRIPTION:%s
        SEQUENCE:0
        STATUS:CONFIRMED
        TRANSP:OPAQUE
        END:VEVENT
        END:VCALENDAR
        """ % (timecreated, timecreated, timestart, timeend, timecreated, inMsg['subject'], uid, body)
