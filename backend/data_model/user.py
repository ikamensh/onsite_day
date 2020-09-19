from data_model.like_levels import LikeLevel

all_users = {}


class Weekdays:
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"

    all_days = [monday, tuesday, wednesday, thursday, friday]


class User:

    def __init__(self, user_id: int, img_url: str, first_name: str, last_name: str):
        if user_id in all_users:
            raise Exception(f"User ID {user_id} is already in use.")

        self.user_id = user_id
        self.img_url = img_url
        self.first_name = first_name
        self.last_name = last_name
        all_users[user_id] = self

        self.monday = LikeLevel.NO_PREF
        self.tuesday = LikeLevel.NO_PREF
        self.wednesday = LikeLevel.NO_PREF
        self.thursday = LikeLevel.NO_PREF
        self.friday = LikeLevel.NO_PREF
