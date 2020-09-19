import json

from data_model.team import Team
from data_model.user import User
from utils import default_serialize

user1 = User(1, "https://randomuser.me/api/portraits/lego/8.jpg", "Elijah", "Ku")
amazon_team = Team(1, "IFS", [user1])


with open("../example_json/team.json", 'w') as f:
    json.dump(amazon_team, f, default=default_serialize)

with open("../example_json/user.json", 'w') as f:
    json.dump(user1, f, default=default_serialize)
