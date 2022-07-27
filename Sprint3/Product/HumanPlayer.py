from dataclasses import dataclass
from PieceColor import PieceColor
import Player


@dataclass
class HumanPlayer(Player.IPlayer):
    _color: PieceColor
    _pieces_to_insert: int
    _pieces_in_board: int

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
    def pieces_to_insert(self):
        return self._pieces_to_insert

    @pieces_to_insert.setter
    def pieces_to_insert(self, pieces_to_insert):
        self._pieces_to_insert = pieces_to_insert

    @property
    def pieces_in_board(self):
        return self._pieces_in_board

    @pieces_in_board.setter
    def pieces_in_board(self, pieces_in_board):
        self._pieces_in_board = pieces_in_board

