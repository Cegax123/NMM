import Player
import Board


class GameState:
    def __init__(self, p1: Player.IPlayer, p2: Player.IPlayer, board: Board.IBoard):
        self.player1 = p1
        self.player2 = p2

        self.player1.enemy = self.player2
        self.player2.enemy = self.player1

        self.player1.set_game_state(self)
        self.player2.set_game_state(self)

        self.board = board

        self.turn = 0
        self.running = True

    def end_game(self):
        self.running = False

    def change_turn(self):
        self.turn ^= 1

    @property
    def current_player(self):
        if self.turn == 0:
            return self.player1
        else:
            return self.player2

    def make_move(self, pos):
        self.current_player.make_move(pos, self.board)
