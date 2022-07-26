from State import State
from dataclasses import dataclass
from typing import List
from Player import IPlayer, FlyPlayer


@dataclass
class SelectState(State):
    _start_pos: tuple = (-1, -1)

    @property
    def start_pos(self) -> tuple:
        return self._start_pos

    def get_possible_moves(self) -> List[tuple]:
        return self.board.get_positions_with_color(self.player.color)

    def _valid_move(self, pos) -> bool:
        if not pos in self.get_possible_moves():
            return False

        self._start_pos = pos

        if self.player.color == self.board.get_color_from_pos(self._start_pos):
            return False

        return True

    def make_move(self, pos) -> None:
        if not self._valid_move(pos):
            return

        self.player.state = self.player.move_state

@dataclass
class SelectWithFlyState(SelectState):
    _player: FlyPlayer
    _threshold_fly: int = 0

    @property
    def player(self) -> FlyPlayer:
        return self._player

    def make_move(self, pos) -> None:
        if not self._valid_move(pos):
            return

        if self.player.pieces_in_board <= self._threshold_fly:
            self.player.state = self.player.fly_state
        else:
            self.player.state = self.player.move_state

