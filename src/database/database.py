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
        try:
            self.db = MySQLdb.connect("mysql.eecs.oregonstate.edu", "cs419-g9", "h8RWjc3qh9QnAJ42", "cs419-g9")
            self.cursor = self.db.cursor()
        except:
            print "Error: Could not connect to database."


    def close(self):
        # close database connection:
        self.db.close()

    def query(self, sql):
        # query the database
        try:
            self.cursor.execute(sql)
            self.results = self.cursor.fetchone()
            if self.results is not None:
                return self.results
        except:
            print "Error: Could not execute query."
