import json

from data_model.user import User

user1 = User(1, "https://randomuser.me/api/portraits/lego/8.jpg", "Elijah", "Ku")


def test_cycles():
    elem = json.loads(user1.to_json())
    cycled = User.from_json(elem)
    assert cycled is user1
