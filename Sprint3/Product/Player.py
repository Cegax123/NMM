from abc import ABC, abstractmethod
from PieceColor import PieceColor
from dataclasses import dataclass
from PlayerType import PlayerType
from PlayerState import PlayerState


@dataclass
class IPlayer(ABC):
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

    @property
    @abstractmethod
    def state(self) -> PlayerState:
        pass

    @state.setter
    @abstractmethod
    def state(self, state) -> None:
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

    @property
    @abstractmethod
    def start_pos(self) -> tuple:
        pass

    @start_pos.setter
    @abstractmethod
    def start_pos(self, start_pos: tuple) -> None:
        pass

    @abstractmethod
    def start_selected(self) -> bool:
        pass

    @abstractmethod
    def unselect_start(self) -> None:
        pass

    @abstractmethod
    def evaluate(self) -> int:
        pass

class Player(IPlayer):
    def __init__(self, color: PieceColor, pieces_to_insert: int, type_player: PlayerType):
        self._color = color
        self._pieces_in_board = 0
        self._pieces_to_insert = pieces_to_insert
        self._state = PlayerState.INSERT

        self._type = type_player

        self.DUMMY_POS = (-1, -1)
        self._start_pos = self.DUMMY_POS

    @property
    def type(self) -> PlayerType:
        return self._type

    @property
    def color(self):
        return self._color

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

    @property
    def state(self) -> PlayerState:
        return self._state

    @state.setter
    def state(self, state) -> None:
        self._state = state

    def get_type(self):
        return self._type

    def set_type(self, player_type):
        self._type = player_type

    def check_lost(self) -> bool:
        return self._pieces_to_insert + self._pieces_in_board < 3

    @property
    def start_pos(self) -> tuple:
        return self._start_pos

    @start_pos.setter
    def start_pos(self, start_pos) -> None:
        self._start_pos = start_pos

    def start_selected(self) -> bool:
        return self._start_pos != self.DUMMY_POS

    def unselect_start(self) -> None:
        self._start_pos = self.DUMMY_POS

    def evaluate(self) -> int:
        eval = self.pieces_in_board
        if self.check_lost():
            eval -= 1000

        return eval
