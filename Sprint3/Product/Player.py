from abc import ABC, abstractmethod
from PieceColor import PieceColor
from dataclasses import dataclass
from PlayerType import PlayerType


@dataclass
class IPlayer(ABC):
    @property
    @abstractmethod
    def start_pos(self) -> tuple:
        pass

    @start_pos.setter
    @abstractmethod
    def start_pos(self, start_pos: tuple) -> None:
        pass

    @property
    @abstractmethod
    def color(self) -> PieceColor:
        pass

    @property
    @abstractmethod
    def pieces_to_insert(self) -> int:
        pass

    @pieces_to_insert.setter
    @abstractmethod
    def pieces_to_insert(self, int) -> None:
        pass

    @property
    @abstractmethod
    def pieces_in_board(self) -> int:
        pass

    @pieces_in_board.setter
    @abstractmethod
    def pieces_in_board(self, int) -> None:
        pass

    @abstractmethod
    def get_type(self) -> PlayerType:
        pass

    @abstractmethod
    def set_type(self, player_type: PlayerType) -> None:
        pass

    @abstractmethod
    def check_lost(self) -> bool:
        pass


class HumanPlayer(IPlayer):
    def __init__(self, color: PieceColor, pieces_to_insert: int):
        self._color = color
        self._pieces_in_board = 0
        self._pieces_to_insert = pieces_to_insert
        self._start_pos = (-1, -1)

        self._type = PlayerType.HUMAN

    @property
    def type(self) -> PlayerType:
        return self._type

    @property
    def color(self):
        return self._color

    @property
    def start_pos(self) -> tuple:
        return self._start_pos

    @start_pos.setter
    def start_pos(self, start_pos) -> None:
        self._start_pos = start_pos

    @property
    def pieces_in_board(self) -> int:
        return self._pieces_in_board

    @pieces_in_board.setter
    def pieces_in_board(self, pieces_in_board) -> None:
        self._pieces_in_board = pieces_in_board

    @property
    def pieces_to_insert(self) -> int:
        return self._pieces_to_insert

    @pieces_to_insert.setter
    def pieces_to_insert(self, pieces_to_insert) -> None:
        self._pieces_to_insert = pieces_to_insert

    def get_type(self):
        return self._type

    def set_type(self, player_type):
        self._type = player_type

    def check_lost(self) -> bool:
        return self._pieces_to_insert + self._pieces_in_board < 3

