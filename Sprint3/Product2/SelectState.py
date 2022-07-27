from dataclasses import dataclass
from PlayerState import PlayerState
from abc import abstractmethod


@dataclass
class SelectState(PlayerState):
    def valid_movement(self):
        return self.board.get_player_of(self.pos) == self.player

    @abstractmethod
    def execute_movement(self):
        pass

@dataclass
class SelectStateWithoutFly(SelectState):
    def execute_movement(self):
        self.player.set_state(self.player.get_move_state())

@dataclass
class SelectStateWithFly(SelectState):
    threshold_to_fly: int = 0

    def execute_movement(self):
        if self.player.get_num_pieces_to_insert() <= self.threshold_to_fly:       
            self.player.set_state(self.player.get_fly_state())
        else:
            self.player.set_state(self.player.get_move_state())

