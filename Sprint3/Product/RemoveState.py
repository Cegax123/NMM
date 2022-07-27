from State import State
from typing import List
from PieceColor import PieceColor
from Board import IBoard
from ConcreteRules import DefaultRules
from dataclasses import dataclass


@dataclass
class RemoveState(State):
    _rule_set: DefaultRules

    def get_possible_moves(self, board: IBoard) -> List[tuple]:
        return board.get_positions_with_color(self.player.enemy.color)

    def make_move(self, pos: tuple, board: IBoard) -> None:
        if not self._valid_move(pos, board):
            return

        self.player.enemy.pieces_in_board -= 1
        board.assign_color_in_pos(pos, PieceColor.EMPTY)

        if self.player.enemy.check_lost():
            self.player.won()
        else:
            if self.player.pieces_to_insert > 0:
                self._rule_set.current_state = self._rule_set.insert_state
            else:
                self._rule_set.current_state = self._rule_set.select_state

            self.player.take_turn()

