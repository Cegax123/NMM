import PlayerBuilder
import BoardBuilder
from PieceColor import PieceColor
from BoardVariant import BoardVariant

class Game:
    def __init__(self):
        player_builder = PlayerBuilder.HumanPlayerBuilder()
        player_director = PlayerBuilder.PlayerDirector()
        player_director.builder = player_builder

        self.p1 = player_director.build_three_men_morris_player(PieceColor.WHITE, self)
        self.p2 = player_director.build_three_men_morris_player(PieceColor.BLACK, self)

        self.p1.enemy = self.p2
        self.p2.enemy = self.p1

        self.board = BoardBuilder.BoardDirector().build_board(BoardVariant.THREE_MEN_MORRIS)

        self.turn = 0
        self.running = True

    def end_game(self):
        self.running = False

    def change_turn(self):
        self.turn ^= 1

    @property
    def current_player(self):
        if self.turn == 0:
            return self.p1
        else:
            return self.p2


