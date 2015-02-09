__author__ = 'kkozee'

#import MySQLdb

class Database(object):

    db = ""
    results = ""
    sql = ""
    results = ""


    def __init__(self):
        self.cursor = self.db.cursor()

    def connect(self):
        try:
            self.db = MySQLdb.connect("mysql.eecs.oregonstate.edu", "cs419-g9", "h8RWjc3qh9QnAJ42", "cs419-g9")
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
            print "Error: Could not connect to database."