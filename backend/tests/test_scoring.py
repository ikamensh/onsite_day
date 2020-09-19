import pytest

from data_model.team import Team
from data_model.user import User

from score_calculator import average_score, synergy_score, onsite_score
import persistence


@pytest.fixture()
def my_team(monkeypatch):
    user1 = User(1, "https://randomuser.me/api/portraits/lego/8.jpg", "Elijah", "Ku", friday=4)
    user2 = User(2, "https://randomuser.me/api/portraits/lego/8.jpg", "Sam", "Ku", monday=0)
    monkeypatch.setattr(persistence, "_all_users", {1: user1, 2: user2})
    my_team = Team(1, "IFS", [user1, user2])

    yield my_team


def test_avg_score(my_team):
    """Verifies average score has all days as keys and is normalized. """

    score = average_score(my_team)
    assert set(score.keys()) == set(range(5))

    for v in score.values():
        assert 0. <= v <= 1.


def test_synergy_score(my_team):
    """Verifies synergy score has all days as keys and is normalized. """

    my_team.add_connection(1, 2)

    score = synergy_score(my_team)
    assert set(score.keys()) == set(range(5))

    for v in score.values():
        assert 0. <= v <= 1.


def test_synergy_score_no_connection(my_team):
    """Verifies synergy score has all days as keys and is normalized - even if no connection is present. """

    score = synergy_score(my_team)
    assert set(score.keys()) == set(range(5))

    for v in score.values():
        assert 0. <= v <= 1.


def test_onsite_score(my_team):
    """Verifies onsite score has all days as keys and is normalized. """

    score = onsite_score(my_team)
    assert set(score.keys()) == set(range(5))

    for v in score.values():
        assert 0. <= v <= 1.
