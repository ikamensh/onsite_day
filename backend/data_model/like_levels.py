from enum import IntEnum


class LikeLevel(IntEnum):
    DISLIKE = 0
    MINOR_DISLIKE = 1
    NO_PREF = 2
    MINOR_LIKE = 3
    LIKE = 4

    def __str__(self):
        return self.name.lower()


if __name__ == '__main__':
    print(LikeLevel.LIKE)
