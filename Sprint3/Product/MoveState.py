from State import State
from typing import List
from PieceColor import PieceColor
from Board import IBoard
from dataclasses import dataclass
from ConcreteRules import DefaultRules


@dataclass
class MoveState(State):
    _rule_set: DefaultRules

    def get_possible_moves(self, board: IBoard) -> List[tuple]:
        start_pos = self._rule_set.select_state.start_pos
        return board.get_positions_empty_neighbors_of_pos(start_pos)

    def make_move(self, pos: tuple, board: IBoard) -> None:
        if not self._valid_move(pos, board):
            return

        start_pos = self._rule_set.select_state.start_pos
        board.assign_color_in_pos(start_pos, PieceColor.EMPTY)
        board.assign_color_in_pos(pos, self.player.color)

        if board.check_mill_in_pos(pos):
            self._rule_set.current_state = self._rule_set.remove_state
        else:
            self.player.take_turn()

class FlyState(MoveState):
    def get_possible_moves(self, board: IBoard) -> List[tuple]:
        return board.get_positions_empty_vertexes()

