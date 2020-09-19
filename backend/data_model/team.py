from typing import List

from data_model.json_serializable import JsonSerializable
from data_model.user import User


class Team(JsonSerializable):
    def __init__(self, team_id: int, team_name: str, users: List[User]):
        self.team_id = team_id
        self.users = users
        self.team_name = team_name

    @staticmethod
    def from_json(elem):
        assert elem["class"] == Team.__name__
        del elem["class"]
        elem = dict(elem)
        elem["users"] = [User.from_json(u) for u in elem["users"]]
        return Team(**elem)

    def __eq__(self, other):
        if not isinstance(other, Team):
            return False
        return all(
            [
                self.team_id == other.team_id,
                self.users == other.users,
                self.team_name == other.team_name,
            ]
        )
