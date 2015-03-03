__author__ = 'kkozee'

import sys
sys.path.append(os.getcwd())

from src.database.database import Database

db = Database()

db.connect()