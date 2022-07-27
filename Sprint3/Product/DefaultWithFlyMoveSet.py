from dataclasses import dataclass
from typing import List
import DefaultMoveSet
import Player
import Board


class DefaultRulesWithFly(DefaultMoveSet.DefaultMoveSet):
    def __init__(self, player: Player.IPlayer):
        super().__init__()
        self.select_state = SelectWithFlyState(self)
        self.fly_state = FlyState(self)


@dataclass
class SelectWithFlyState(DefaultMoveSet.SelectState):
    _rule_set: DefaultRulesWithFly
    _threshold_fly: int = 0

    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        if not self._valid_move(pos, player, board):
            return

        if player.pieces_in_board <= self._threshold_fly:
            self._rule_set.current_state = self._rule_set.fly_state
        else:
            self._rule_set.current_state = self._rule_set.move_state


class FlyState(DefaultMoveSet.MoveState):
    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        return board.get_positions_empty_vertexes()

