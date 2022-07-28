from PieceColor import PieceColor
from BoardVariant import BoardVariant
import Game
import BoardBuilder
import PlayerBuilder


class GameBuilder:
    def set_player1(self, player1):
        self._player1 = player1

    def set_player2(self, player2):
        self._player2 = player2

    def set_board(self, board):
        self._board = board

    def get_result(self) -> Game.GameState:
        return Game.GameState(self._player1, self._player2, self._board)


class GameDirector:
    _builder: GameBuilder = GameBuilder()

    def build_two_player_nine_men_morris_game(self) -> Game.GameState:
        human_player_builder = PlayerBuilder.HumanPlayerBuilder()
        player_director = PlayerBuilder.PlayerDirector()
        player_director.builder = human_player_builder

        player1 = player_director.build_nine_men_morris_player(PieceColor.WHITE)
        player2 = player_director.build_nine_men_morris_player(PieceColor.BLACK)

        board = BoardBuilder.BoardDirector().build_board(BoardVariant.NINE_MEN_MORRIS)

        self._assign_to_builder(player1, player2, board)

        return self._builder.get_result()

    def build_two_player_five_men_morris_game(self) -> Game.GameState:
        human_player_builder = PlayerBuilder.HumanPlayerBuilder()
        player_director = PlayerBuilder.PlayerDirector()
        player_director.builder = human_player_builder

        player1 = player_director.build_five_men_morris_player(PieceColor.WHITE)
        player2 = player_director.build_five_men_morris_player(PieceColor.BLACK)

        board = BoardBuilder.BoardDirector().build_board(BoardVariant.FIVE_MEN_MORRIS)

        self._assign_to_builder(player1, player2, board)

        return self._builder.get_result()

    def build_two_player_three_men_morris_game(self) -> Game.GameState:
        human_player_builder = PlayerBuilder.HumanPlayerBuilder()
        player_director = PlayerBuilder.PlayerDirector()
        player_director.builder = human_player_builder

        player1 = player_director.build_three_men_morris_player(PieceColor.WHITE)
        player2 = player_director.build_three_men_morris_player(PieceColor.BLACK)

        board = BoardBuilder.BoardDirector().build_board(BoardVariant.THREE_MEN_MORRIS)

        self._assign_to_builder(player1, player2, board)

        return self._builder.get_result()

    def _assign_to_builder(self, player1, player2, board):
        self._builder.set_player1(player1)
        self._builder.set_player2(player2)
        self._builder.set_board(board)

