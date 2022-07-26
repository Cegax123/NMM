from State import State
from typing import List
from PieceColor import PieceColor


class InsertState(State):
    def get_possible_moves(self) -> List[tuple]:
        return self.board.get_positions_empty_vertexes()

    def make_move(self, pos) -> None:
        if not self._valid_move(pos):
            return

        self.board.assign_color_in_pos(pos, self.player.color)
        self.player.pieces_to_insert -= 1

        if self.board.check_mill_in_pos(pos):
            self.player.state = self.player.remove_state

        elif self.player.pieces_to_insert == 0:
            self.player.state = self.player.select_state
            self.player.take_turn()
