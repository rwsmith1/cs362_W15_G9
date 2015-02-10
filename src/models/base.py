__author__ = 'kkozee'

class Base(object):

    def __init__(self, id):
        self.id = id

    def setID(self, id):
        self.id = id
        return self.id

    def getID(self):
        return self.id