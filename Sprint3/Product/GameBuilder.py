from PieceColor import PieceColor
from BoardVariant import BoardVariant
from PlayerType import PlayerType
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

    def set_threshold_dly(self, threshold_fly):
        self._threshold_fly = threshold_fly

    def get_result(self) -> Game.GameState:
        return Game.GameState(self._player1, self._player2, self._board, self._threshold_fly)


class GameDirector:
    _builder: GameBuilder = GameBuilder()
    _player_director: PlayerBuilder.PlayerDirector = PlayerBuilder.PlayerDirector()
    _board_director: BoardBuilder.BoardDirector = BoardBuilder.BoardDirector()

    def build_game(self, board_variant: BoardVariant, type_player_1: PlayerType, type_player_2: PlayerType) -> Game.GameState:
        player1 = self._player_director.build_player(board_variant, PieceColor.WHITE, type_player_1)
        player2 = self._player_director.build_player(board_variant, PieceColor.BLACK, type_player_2)

        self._builder.set_player1(player1)
        self._builder.set_player2(player2)

        board = self._board_director.build_board(board_variant)
        self._builder.set_board(board)

        if board_variant == BoardVariant.THREE_MEN_MORRIS:
            self._builder.set_threshold_dly(-1)
        if board_variant == BoardVariant.FIVE_MEN_MORRIS:
            self._builder.set_threshold_dly(-1)
        if board_variant == BoardVariant.NINE_MEN_MORRIS:
            self._builder.set_threshold_dly(3)

        return self._builder.get_result()

