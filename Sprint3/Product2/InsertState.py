from dataclasses import dataclass
from PlayerState import PlayerState

@dataclass
class InsertState(PlayerState):
    def valid_movement(self):
        return self.board.get_player_of(self.pos) == None

    def execute_movement(self):
        self.board.insert_piece_in(self.pos, self.player)
        self.player.minus_one_piece_to_insert()

        if self.board.check_new_mill(self.pos):
            self.player.set_state(self.player.get_remove_state())

        elif self.player.get_num_pieces_to_insert() == 0:
            self.player.set_state(self.player.get_select_state())

