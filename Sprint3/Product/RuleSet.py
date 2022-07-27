from abc import ABC, abstractmethod
from typing import List
from State import IState
from Board import IBoard


class IRuleSet(ABC):
    @property
    @abstractmethod
    def current_state(self) -> IState:
        pass

    @current_state.setter
    @abstractmethod
    def current_state(self, state: IState) -> None:
        pass

    @abstractmethod
    def make_move(self, pos: tuple, board: IBoard) -> None:
        pass

    @abstractmethod
    def get_possible_moves(self, board: IBoard) -> List[tuple]:
        pass


