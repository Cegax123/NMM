from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass
import Board
import Player

class IMoveSet(ABC):
    @property
    @abstractmethod
    def current_state(self):
        pass

    @current_state.setter
    @abstractmethod
    def current_state(self, state) -> None:
        pass

    @abstractmethod
    def make_move(self, pos: tuple, board: Board.IBoard) -> None:
        pass

    @abstractmethod
    def get_possible_moves(self, board: Board.IBoard) -> List[tuple]:
        pass


class IState(ABC):
    @abstractmethod
    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        pass

    @abstractmethod
    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        pass


@dataclass
class State(IState, ABC):
    _rule_set = IMoveSet

    @abstractmethod
    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        pass

    @abstractmethod
    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        pass

    def _valid_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> bool:
        return pos in self.get_possible_moves(player, board)


