from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from Board import IBoard
from Player import IPlayer


class IPlayerState(ABC):
    @abstractmethod
    def valid_movement(self, pos):
        pass

    @abstractmethod
    def execute_movement(self, pos):
        pass


@dataclass
class PlayerState(IPlayerState):
    player: IPlayer
    board: IBoard
    pos: Optional[tuple] = None

    @abstractmethod
    def valid_movement(self):
        pass

    @abstractmethod
    def execute_movement(self):
        pass

