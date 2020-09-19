import abc
import json

from utils import default_serialize


class JsonSerializable(abc.ABC):

    def to_json(self):
        return json.dumps(self, default=default_serialize)

    @staticmethod
    @abc.abstractmethod
    def from_json(elem: dict):
        raise NotImplementedError
