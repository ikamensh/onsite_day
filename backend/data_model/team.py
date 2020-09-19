from typing import List

from data_model.user import User

all_teams = {}

class Team:
    def __init__(self, team_id: int, team_name: str, users: List[User]):
        self.team_id = team_id
        self.users = users
        self.team_name = team_name
        if team_id in all_teams:
            raise Exception(f"Team ID {team_id} is already in use.")

        all_teams[team_id] = self



