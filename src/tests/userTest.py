__author__ = 'kkozee'

import sys

sys.path.append('')

from src.models.user import User
from src.models.filter import Filter

user = User(0, "Kevin", "kkozee@gmail.com", "pass")

f = Filter(user)

f.createMessage()
f.setParts()
f.attachParts()

f.sendMessage()
