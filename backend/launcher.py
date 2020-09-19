from data_model.user import User
from data_model.team import Team


user1 = User(1, "no", "Elijah", "Ku")

amazon_team = Team(1, "IFS", [user1])

import json


def my_serialize(x):
    if hasattr(x, "__dict__"):
        return x.__dict__
    else:
        return str(x)

with open("test.json", 'w') as f:
    json.dump(amazon_team.__dict__, f, default=my_serialize)
