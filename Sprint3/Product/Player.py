from abc import ABC, abstractmethod
from PieceColor import PieceColor
from State import IState
from InsertState import InsertState
from SelectState import SelectState
from MoveState import MoveState, FlyState
from RemoveState import RemoveState


class IPlayer(ABC):
    @property
    @abstractmethod
    def enemy(self) -> 'IPlayer':
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

    @property
    @abstractmethod
    def state(self) -> IState:
        pass

    @state.setter
    @abstractmethod
    def state(self, state: IState) -> None:
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


class FlyPlayer():
    pass
