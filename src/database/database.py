####################################################################
    # Name: database.py
    # Basic database functionality to connect to the cs419_g9 mySQL
    # database: connect, close, query(fetchone), query all(fetchall),
    # and update.
####################################################################
__author__ = 'kkozee'

import MySQLdb


class Database(object):
    def __init__(self):
        self.db = None
        self.results = None
        self.sql = None
        self.results = None
        self.cursor = None

    def connect(self):
        # connect to the database
        try:
            self.db = MySQLdb.connect("mysql.eecs.oregonstate.edu", "cs419-g9", "h8RWjc3qh9QnAJ42", "cs419-g9")
            self.cursor = self.db.cursor()
        except:
            print "Error (connect()): Could not connect to database."


    def close(self):
        # close database connection:
        self.db.close()

    def query(self, sql):
        # query the database for first result
        try:
            self.cursor.execute(sql)
            self.results = self.cursor.fetchone()
            if self.results is not None:
                return self.results
        except:
            print "Error (query): Could not execute query."

    def queryall(self, sql):
        # query the database for all results
        try:
            self.cursor.execute(sql)
            self.results = self.cursor.fetchall()
            if self.results is not None:
                return self.results
        except:
            print "Error (queryall): Could not connect to database."

    def update(self, sql):
        # update the database
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print "Error (update): Could not connect to database."
