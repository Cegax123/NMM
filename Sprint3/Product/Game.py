import Player
import Board


class GameState:
    def __init__(self, p1: Player.IPlayer, p2: Player.IPlayer, board: Board.IBoard, threshold_fly: int):
        self._player1 = p1
        self._player2 = p2

        self.board = board
        self.threshold_fly = threshold_fly

        self.turn = 0
        self.winner = False
        self.name_winner = ''

    @property
    def player1(self):
        return self._player1

    @property
    def player2(self):
        return self._player2

    @player1.setter
    def player1(self, player):
        self._player1 = player

    @player2.setter
    def player2(self, player):
        self._player2 = player

    def end_game(self):
        self.winner = True

    def change_turn(self):
        self.turn ^= 1

    def evaluate(self, turn):
        return (1-2*turn)*(self._player1.evaluate()-self._player2.evaluate())

    @property
    def current_player(self) -> Player.IPlayer:
        if self.turn % 2 == 0:
            return self._player1
        else:
            return self._player2

    @property
    def enemy_player(self) -> Player.IPlayer:
        if self.turn % 2 == 0:
            return self._player2
        else:
            return self._player1

