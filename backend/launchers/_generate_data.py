from data_model.team import Team
from data_model.user import User
from persistence import save_data, add_user, add_team, load_data, get_team

load_data()

at = get_team(1)
at.add_connection(1, 2)

save_data()
