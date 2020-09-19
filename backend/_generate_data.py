from data_model.team import Team
from data_model.user import User
from persistence import save_data, add_user, add_team

user1 = User(1, "https://randomuser.me/api/portraits/lego/8.jpg", "Elijah", "Ku")
amazon_team = Team(1, "IFS", [user1])

add_user(user1)
add_team(amazon_team)

save_data()
