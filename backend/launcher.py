from data_model.user import User
from data_model.team import Team


user1 = User(1, "no", "Elijah", "Ku")

amazon_team = Team(1, "IFS", [user1])

import json

with open("test.json", 'w') as f:
    json.dumps(user1.__dict__)

