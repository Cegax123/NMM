from dataclasses import dataclass
from PlayerState import PlayerState



@dataclass
class MoveState(PlayerState):
    def valid_movement(self):
        if self.board.verify_neighborhood(self.pos, self.player.get_selected_pos()) == False:
            return False

        player = self.board.get_player_of(self.pos)
        if player != None and player != self.player:
            return False

        return True

    def execute_movement(self):
        player = self.board.get_player_of(self.pos)

        if player == self.player:
            self.player.set_state(self.player.get_select_state())
        else:
            self.board.remove_player_of(self.player.get_selected_pos())
            self.board.insert_piece_in(self.pos, self.player)

            if self.board.check_new_mill(self.pos):
                self.player.set_state(self.player.get_remove_state())
            elif:
                self.player.set_
