import json

from data_model.team import Team
from data_model.user import User
from utils import default_serialize

from data_model import team
from config import teams_file

_all_teams = {}
_all_users = {}


def save_data(teams_file=teams_file):
    with open(teams_file, 'w') as f:
        json.dump(list(_all_teams.values()), f, default=default_serialize)


def load_data(teams_file=teams_file):
    global _all_users
    global _all_teams

    _all_users = {}
    _all_teams = {}

    with open(teams_file, 'r') as f:
        elems = json.load(f)

    for e in elems:
        t = team.Team.from_json(e)
        for user in t.users:
            add_user(user)
        add_team(t)


def add_user(user: User):
    if user.user_id in _all_users:
        if user is not _all_users[user.user_id]:
            raise Exception(f"User ID {user.user_id} is already in use.")

    _all_users[user.user_id] = user


def add_team(team: Team):
    if team.team_id in _all_teams:
        if team is not _all_teams[team.team_id]:
            raise Exception(f"User ID {team.team_id} is already in use.")

    for user in team.users:
        assert user in _all_users.values()

    _all_teams[team.team_id] = team


def get_team(team_id: int) -> Team:
    return _all_teams[team_id]


def get_user(user_id: int) -> User:
    return _all_users[user_id]
