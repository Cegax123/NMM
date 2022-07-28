from abc import ABC, abstractmethod
from typing import List
from PieceColor import PieceColor
from dataclasses import dataclass
from PlayerType import PlayerType
import Board


@dataclass
class IPlayer(ABC):
    @property
    @abstractmethod
    def enemy(self) -> 'IPlayer':
        pass

    @enemy.setter
    def enemy(self, enemy: 'IPlayer') -> None:
        pass

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
    def make_move(self, pos: tuple, board: Board.IBoard) -> None:
        pass

    @abstractmethod
    def get_possible_moves(self, board: Board.IBoard) -> List[tuple]:
        pass

    @abstractmethod
    def take_turn(self) -> None:
        pass

    @abstractmethod
    def check_lost(self) -> bool:
        pass

    @abstractmethod
    def won(self) -> None:
        pass


class HumanPlayer(IPlayer):
    def __init__(self, color: PieceColor, pieces_to_insert: int, move_set, game_state):
        self._color = color
        self._pieces_in_board = 0
        self._pieces_to_insert = pieces_to_insert
        self._move_set = move_set
        self._game_state = game_state
        self._start_pos = (-1, -1)

        self._type = PlayerType.HUMAN

    @property
    def type(self) -> PlayerType:
        return self._type

    @property
    def enemy(self):
        return self._enemy

    @enemy.setter
    def enemy(self, enemy):
        self._enemy = enemy

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

    def make_move(self, pos, board):
        self._move_set.make_move(pos=pos, player=self, board=board)

    def get_possible_moves(self, board):
        return self._move_set.get_possible_moves(self, board)

    def check_lost(self) -> bool:
        return self._pieces_to_insert + self._pieces_in_board < 3

    def won(self) -> None:
        self._game_state.end_game()

    def take_turn(self):
        self._game_state.change_turn()

    def print_state(self):
        self._move_set.current_state.print_state()


