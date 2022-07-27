from State import State
from typing import List
from Board import IBoard
from ConcreteRules import DefaultRules
from dataclasses import dataclass


@dataclass
class InsertState(State):
    _rule_set: DefaultRules

    def get_possible_moves(self, board: IBoard) -> List[tuple]:
        return board.get_positions_empty_vertexes()

    def make_move(self, pos: tuple, board: IBoard) -> None:
        if not self._valid_move(pos, board):
            return

        board.assign_color_in_pos(pos, self.player.color)
        self.player.pieces_to_insert -= 1

        if board.check_mill_in_pos(pos):
            self._rule_set.current_state = self._rule_set.remove_state

        elif self.player.pieces_to_insert == 0:
            self._rule_set.current_state = self._rule_set.select_state
            self.player.take_turn()
