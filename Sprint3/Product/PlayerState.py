from enum import Enum, auto


class PlayerState(Enum):
    INSERT = auto()
    MOVE = auto()
    REMOVE = auto()
    FLY = auto()

