from enum import Enum, auto, unique


@unique
class GameStates(Enum):
    PLAYERS_TURN = auto()
    ENEMY_TURN = auto()
