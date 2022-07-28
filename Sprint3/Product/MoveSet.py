from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass
import Board
import Player
import Game


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
    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        pass

    @abstractmethod
    def make_move(self, pos: tuple, game_state: Game.GameState) -> None:
        pass


class IState(ABC):
    @abstractmethod
    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        pass

    @abstractmethod
    def make_move(self, pos: tuple, game_state: Game.GameState) -> None:
        pass


@dataclass
class State(IState, ABC):
    _move_set = IMoveSet

    @abstractmethod
    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        pass

    @abstractmethod
    def make_move(self, pos: tuple, game_state: Game.GameState) -> None:
        pass

    def _valid_move(self, pos: tuple, game_state: Game.GameState) -> bool:
        return pos in self.get_possible_moves(game_state)


