from State import State
from dataclasses import dataclass
from typing import List
from Board import IBoard
from ConcreteRules import DefaultRules, DefaultRulesWithFly


@dataclass
class SelectState(State):
    _rule_set: DefaultRules
    _start_pos: tuple = (-1, -1)

    @property
    def start_pos(self) -> tuple:
        return self._start_pos

    def get_possible_moves(self, board: IBoard) -> List[tuple]:
        return board.get_positions_with_color(self.player.color)

    def _valid_move(self, pos: tuple, board: IBoard) -> bool:
        if not pos in self.get_possible_moves(board):
            return False

        self._start_pos = pos

        if self.player.color == board.get_color_from_pos(self._start_pos):
            return False

        return True

    def make_move(self, pos: tuple, board: IBoard) -> None:
        if not self._valid_move(pos, board):
            return

        self._rule_set.current_state = self._rule_set.move_state

@dataclass
class SelectWithFlyState(SelectState):
    _rule_set: DefaultRulesWithFly
    _threshold_fly: int = 0

    def make_move(self, pos: tuple, board: IBoard) -> None:
        if not self._valid_move(pos, board):
            return

        if self.player.pieces_in_board <= self._threshold_fly:
            self._rule_set.current_state = self._rule_set.fly_state
        else:
            self._rule_set.current_state = self._rule_set.move_state

