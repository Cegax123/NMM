from abc import ABC, abstractmethod
from dataclasses import dataclass
from Board import IBoard
from Player import IPlayer


class IAnalyzer(ABC):
    @abstractmethod
    def get_movement_insert_piece(self, current_player: IPlayer, enemy_player: IPlayer, board: IBoard):
        pass

    @abstractmethod
    def get_movement_move_piece(self, current_player: IPlayer, enemy_player: IPlayer, board: IBoard):
        pass

    @abstractmethod
    def get_movement_remove_piece(self, current_player: IPlayer, enemy_player: IPlayer, board: IBoard):
        pass


@dataclass
class AnalyzerNineMenMorris(IAnalyzer):
    depth: int

    def get_movement_insert_piece(self, current_player: IPlayer, enemy_player: IPlayer, board: IBoard):
        pass

    def get_movement_move_piece(self, current_player: IPlayer, enemy_player: IPlayer, board: IBoard):
        pass

    def get_movement_remove_piece(self, current_player: IPlayer, enemy_player: IPlayer, board: IBoard):
        pass