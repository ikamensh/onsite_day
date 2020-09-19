from collections import defaultdict
from typing import Dict

from data_model.team import Team
from data_model.user import Weekdays
from persistence import get_user


def average_score(team: Team) -> Dict[int, float]:
    """Average score shows how team likes a given day on average.

    It's normalized from 0 to 1. """
    scores = defaultdict(list)

    for user in team.users:
        for i, day in enumerate(Weekdays.all_days):
            score = getattr(user, day)
            scores[i].append(score)

    scores_raw = {day: sum(score) / len(team.users) / 4 for day, score in scores.items()}
    return scores_raw


def synergy_score(team: Team) -> Dict[int, float]:
    """Synergy score shows if the day facilitates cooperation between people in joint projects.

    It's normalized from 0 to 1."""

    scores = defaultdict(list)

    for user in team.users:
        connected = team.connections[user.user_id]
        for other_id in connected:
            other = get_user(other_id)
            for i, day in enumerate(Weekdays.all_days):
                score1 = getattr(user, day)
                score2 = getattr(other, day)
                scores[i].append(score1 * score2)

    n_connections = 0
    for uid, connected in team.connections.items():
        n_connections += len(connected)
    if not n_connections:
        return {i: 0.5 for i in range(5)}

    scores_raw = {k: (sum(v) / n_connections / 16) ** 0.5 for k, v in scores.items()}
    return scores_raw


def onsite_score(team: Team) -> Dict[int, float]:
    """Computes the onsite score per 5 weekdays for the given team.

    It's normalized from 0 to 1. """

    gs = synergy_score(team)
    ds = average_score(team)
    return {i: 0.5 * gs[i] + 0.5 * ds[i] for i in range(5)}
