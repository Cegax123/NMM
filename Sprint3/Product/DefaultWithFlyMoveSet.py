from dataclasses import dataclass
from typing import List
import DefaultMoveSet
import Game


class DefaultRulesWithFly(DefaultMoveSet.DefaultMoveSet):
    def __init__(self, threshold_fly: int):
        super().__init__()
        self.select_state = SelectWithFlyState(self, threshold_fly)
        self.fly_state = FlyState(self)


@dataclass
class SelectWithFlyState(DefaultMoveSet.SelectState):
    def __init__(self, move_set: DefaultRulesWithFly, threshold_fly: int):
        self._move_set: DefaultRulesWithFly = move_set
        self._threshold_fly: int = threshold_fly

    def make_move(self, pos: tuple, game_state: Game.GameState) -> None:
        if not self._valid_move(pos, game_state):
            return

        game_state.current_player.start_pos = pos

        if game_state.current_player.pieces_in_board <= self._threshold_fly:
            self._move_set.current_state = self._move_set.fly_state
        else:
            self._move_set.current_state = self._move_set.move_state


class FlyState(DefaultMoveSet.MoveState):
    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        return game_state.board.get_positions_empty_vertexes() + game_state.board.get_positions_with_color(game_state.current_player.color)

