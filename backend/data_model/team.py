from collections import defaultdict
from typing import List, Dict

from data_model.json_serializable import JsonSerializable
from data_model.user import User


class Team(JsonSerializable):
    def __init__(self, team_id: int, team_name: str, users: List[User], connections: Dict = None):
        self.team_id = team_id
        self.users = users
        self.team_name = team_name
        self.connections = defaultdict(list)
        if connections:
            self.connections.update(connections)

    @staticmethod
    def from_json(elem):
        assert elem["class"] == Team.__name__
        del elem["class"]
        elem = dict(elem)
        elem["users"] = [User.from_json(u) for u in elem["users"]]
        elem["connections"] = {int(k): v for k, v  in elem["connections"].items()}
        return Team(**elem)


    def add_connection(self, user_id_1: int, user_id_2: int):
        """Register that two users would like to work together. """

        assert user_id_1 != user_id_2, "Can only connect two distinct users."
        this_team = {u.user_id for u in self.users}
        assert user_id_1 in this_team, f"User {user_id_1} is not part of team {self.team_name}"
        assert user_id_2 in this_team, f"User {user_id_2} is not part of team {self.team_name}"

        self.connections[user_id_1].append(user_id_2)
        self.connections[user_id_2].append(user_id_1)

    def __eq__(self, other):
        if not isinstance(other, Team):
            return False
        return all(
            [
                self.team_id == other.team_id,
                self.users == other.users,
                self.team_name == other.team_name,
                self.connections == other.connections
            ]
        )
