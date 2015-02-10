__author__ = 'kkozee'

import sys

<<<<<<< Updated upstream
sys.path.append('')
=======
sys.path.append('/nfs/stak/students/k/kozeek/Capstone/cs362_W15_G9/')
>>>>>>> Stashed changes

from src.models.user import User
from src.models.filter import Filter

user = User(0, "Kevin", "kkozee@gmail.com", "pass")

f = Filter(user)

f.createMessage()
f.setParts()
f.attachParts()

f.sendMessage()
