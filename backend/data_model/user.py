from data_model.json_serializable import JsonSerializable
from data_model.like_levels import LikeLevel


class Weekdays:
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"

    all_days = [monday, tuesday, wednesday, thursday, friday]
    to_int = {
        x: i  for i, x in enumerate(all_days)
    }


class User(JsonSerializable):

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
        elem = dict(elem)
        assert elem["class"] == User.__name__
        del elem["class"]
        for day in Weekdays.all_days:
            json_val = elem[day]
            val = LikeLevel(json_val)
            elem[day] = val

        return User(**elem)
