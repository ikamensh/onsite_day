from typing import List

from data_model.json_serializable import JsonSerializable
from data_model.user import User

_all_teams = {}


def get_team(team_id: int):
    return _all_teams[team_id]


class Team(JsonSerializable):

    def __new__(cls, team_id: int, *args, **kwargs):
        would_be_result = super(Team, cls).__new__(cls)
        would_be_result.__init__(team_id, *args, **kwargs)

        if team_id in _all_teams:
            existing = _all_teams[team_id]
            if existing != would_be_result:
                raise Exception(
                    f"User ID {team_id} is already in use. Tried to create a non-identical instance.")
            return existing
        else:
            _all_teams[team_id] = would_be_result
            return would_be_result

    def __init__(self, team_id: int, team_name: str, users: List[User]):
        self.team_id = team_id
        self.users = users
        self.team_name = team_name

    @staticmethod
    def from_json(elem):
        uid = int(elem["team_id"])
        return _all_teams[uid]
