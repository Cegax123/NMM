from State import State
from typing import List
from PieceColor import PieceColor


class RemoveState(State):
    def get_possible_moves(self) -> List[tuple]:
        return self.board.get_positions_with_color(self.player.enemy.color)

    def make_move(self, pos) -> None:
        if not self._valid_move(pos):
            return

        self.player.enemy.pieces_in_board -= 1
        self.board.assign_color_in_pos(pos, PieceColor.EMPTY)

        if self.player.enemy.check_lost():
            self.player.won()
        else:
            self.player.take_turn()

