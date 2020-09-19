import persistence
from data_model.team import Team
from data_model.user import User


def test_valid_data():
    persistence.load_data()
    persistence._all_users = {}
    persistence._all_teams = {}


def test_save_data(tmpdir):

    user1 = User(1, "https://randomuser.me/api/portraits/lego/8.jpg", "Elijah", "Ku")
    amazon_team = Team(1, "IFS", [user1])

    persistence.add_user(user1)
    persistence.add_team(amazon_team)


    persistence.save_data(f"{tmpdir}/bla.json")


