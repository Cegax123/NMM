from State import State
from typing import List
from PieceColor import PieceColor


class MoveState(State):
    def get_possible_moves(self) -> List[tuple]:
        start_pos = self.player.select_state.start_pos
        return self.board.get_positions_adyacent_neighbors_of_pos(start_pos)

    def make_move(self, pos: tuple) -> None:
        if not self._valid_move(pos):
            return

        start_pos = self.player.select_state.start_pos
        self.board.assign_color_in_pos(start_pos, PieceColor.EMPTY)
        self.board.assign_color_in_pos(pos, self.player.color)

        if self.board.check_mill_in_pos(pos):
            self.player.state = self.player.remove_state
        else:
            self.player.take_turn()

class FlyState(MoveState):
    def get_possible_moves(self) -> List[tuple]:
        return self.board.get_positions_empty_vertexes()
