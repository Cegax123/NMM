import sys
sys.path.append("../Product")

from GameBuilder import GameDirector
from BoardVariant import BoardVariant
from PlayerType import PlayerType
from PlayerState import PlayerState
import State
from PieceColor import PieceColor
import unittest


class InsertStateTest(unittest.TestCase):
    def setUp(self):
        self.game_state = GameDirector().build_game(BoardVariant.NINE_MEN_MORRIS, PlayerType.HUMAN, PlayerType.HUMAN)
        self.move_handler = State.MoveHandler()

    def test_insert_piece(self):

        self.move_handler.apply_move((0, 0), self.game_state)

        self.assertEqual(self.game_state.board.get_color_from_pos((0, 0)), PieceColor.WHITE)
        self.assertEqual(self.game_state.player1.pieces_to_insert, 8)
        self.assertEqual(self.game_state.player1.state, PlayerState.INSERT)

    def test_insert_last_piece(self):
        self.game_state.player1.pieces_to_insert = 1

        self.move_handler.apply_move((0, 0), self.game_state)
        self.assertEqual(self.game_state.player1.pieces_to_insert, 0)
        self.assertEqual(self.game_state.player1.state, PlayerState.MOVE)


if __name__ == "__main__":
    unittest.main()

