from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass
from Player import IPlayer
from Board import IBoard


class IState(ABC):
    @abstractmethod
    def get_possible_moves(self) -> List[tuple]:
        pass

    @abstractmethod
    def make_move(self, pos: tuple) -> None:
        pass

    @property
    @abstractmethod
    def player(self) -> IPlayer:
        pass

    @property
    @abstractmethod
    def board(self) -> IBoard:
        pass


@dataclass
class State(IState, ABC):
    _player: IPlayer
    _board: IBoard

    @abstractmethod
    def get_possible_moves(self) -> List[tuple]:
        pass

    @abstractmethod
    def make_move(self, pos: tuple) -> None:
        pass

    @property
    def player(self) -> IPlayer:
        return self._player

    @property
    def board(self) -> IBoard:
        return self._board

    @abstractmethod
    def _valid_move(self, pos: tuple) -> bool:
        return pos in self.get_possible_moves()


