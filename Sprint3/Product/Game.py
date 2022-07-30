import Player
import Board


class GameState:
    def __init__(self, p1: Player.IPlayer, p2: Player.IPlayer, board: Board.IBoard):
        self.player1 = p1
        self.player2 = p2

        self.board = board

        self.turn = 0
        self.running = True

    def end_game(self):
        self.running = False

    def change_turn(self):
        self.turn ^= 1

    def evaluate(self):
        return self.current_player.pieces_in_board - self.player2.pieces_in_board

    @property
    def current_player(self) -> Player.IPlayer:
        if self.turn == 0:
            return self.player1
        else:
            return self.player2

    @property
    def enemy_player(self) -> Player.IPlayer:
        if self.turn % 2 == 0:
            return self.player2
        else:
            return self.player1
