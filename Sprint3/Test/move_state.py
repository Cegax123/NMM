import sys
sys.path.append("../Product")

from GameBuilder import GameDirector
from BoardVariant import BoardVariant
from PlayerType import PlayerType
import State
from PieceColor import PieceColor
import unittest


class MoveStateTest(unittest.TestCase):
    def setUp(self):
        self.game_state = GameDirector().build_game(BoardVariant.NINE_MEN_MORRIS, PlayerType.HUMAN, PlayerType.HUMAN)
        self.game_state.player1.pieces_to_insert = 1
        self.move_handler = State.MoveHandler()
        self.move_handler.apply_move((0, 0), self.game_state)
        self.game_state.turn = 0

    def test_move_piece(self):
        self.move_handler.apply_list_moves([(0, 0), (3, 0)], self.game_state)
        self.assertEqual(self.game_state.board.get_color_from_pos((0, 0)), PieceColor.EMPTY)
        self.assertEqual(self.game_state.board.get_color_from_pos((3, 0)), PieceColor.WHITE)

    def test_move_piece_no_adyacent(self):
        self.move_handler.apply_list_moves([(0, 0), (6, 0)], self.game_state)
        self.assertEqual(self.game_state.board.get_color_from_pos((0, 0)), PieceColor.WHITE)
        self.assertEqual(self.game_state.board.get_color_from_pos((6, 0)), PieceColor.EMPTY)


if __name__ == "__main__":
    unittest.main()
