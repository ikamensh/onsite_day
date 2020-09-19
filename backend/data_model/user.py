from data_model.json_serializable import JsonSerializable
from data_model.like_levels import LikeLevel

_all_users = {}


def get_user(user_id: int):
    return _all_users[user_id]


class Weekdays:
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"

    all_days = [monday, tuesday, wednesday, thursday, friday]


class User(JsonSerializable):

    def __new__(cls, user_id: int, *args, **kwargs):
        would_be_result = super(User, cls).__new__(cls)
        would_be_result.__init__(user_id, *args, **kwargs)

        if user_id in _all_users:
            existing = _all_users[user_id]
            if existing != would_be_result:
                raise Exception(
                    f"User ID {user_id} is already in use. Tried to create a non-identical instance.")
            return existing
        else:
            _all_users[user_id] = would_be_result
            return would_be_result

    def __init__(
            self,
            user_id: int,
            img_url: str,
            first_name: str,
            last_name: str,
            monday=LikeLevel.NO_PREF,
            tuesday=LikeLevel.NO_PREF,
            wednesday=LikeLevel.NO_PREF,
            thursday=LikeLevel.NO_PREF,
            friday=LikeLevel.NO_PREF,
    ):
        self.user_id = user_id
        self.img_url = img_url
        self.first_name = first_name
        self.last_name = last_name

        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.__dict__ == other.__dict__

    @staticmethod
    def from_json(elem):
        uid = int(elem["user_id"])
        return _all_users[uid]
