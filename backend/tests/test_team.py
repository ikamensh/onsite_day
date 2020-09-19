import json

from data_model.team import Team
from data_model.user import User

user1 = User(1, "https://randomuser.me/api/portraits/lego/8.jpg", "Elijah", "Ku")
user2 = User(2, "https://randomuser.me/api/portraits/lego/8.jpg", "Eli", "Kuh")

amazon_team = Team(1, "IFS", [user1, user2])
amazon_team.add_connection(1, 2)


def test_cycles():
    elem = json.loads(amazon_team.to_json())
    cycled = Team.from_json(elem)
    assert cycled == amazon_team
