from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass
from Player import IPlayer
from Board import IBoard
from RuleSet import IRuleSet


class IState(ABC):
    @abstractmethod
    def get_possible_moves(self, board: IBoard) -> List[tuple]:
        pass

    @abstractmethod
    def make_move(self, pos: tuple, board: IBoard) -> None:
        pass

    @property
    @abstractmethod
    def player(self) -> IPlayer:
        pass


@dataclass
class State(IState, ABC):
    _rule_set: IRuleSet
    _player: IPlayer

    @abstractmethod
    def get_possible_moves(self, board: IBoard) -> List[tuple]:
        pass

    @abstractmethod
    def make_move(self, pos: tuple, board: IBoard) -> None:
        pass

    @property
    def player(self) -> IPlayer:
        return self._player

    def _valid_move(self, pos: tuple, board: IBoard) -> bool:
        return pos in self.get_possible_moves(board)


