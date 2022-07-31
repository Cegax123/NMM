import sys
sys.path.append("../Product")

from GameBuilder import GameDirector
from BoardVariant import BoardVariant
from PlayerType import PlayerType
from PlayerState import PlayerState
import State
from PieceColor import PieceColor
import unittest


class RemoveStateTest(unittest.TestCase):
    def setUp(self):
        self.game_state = GameDirector().build_game(BoardVariant.NINE_MEN_MORRIS, PlayerType.HUMAN, PlayerType.HUMAN)
        self.move_handler = State.MoveHandler()
        self.move_handler.apply_move((0, 0), self.game_state)
        self.game_state.turn = 1
        self.game_state.player2.state = PlayerState.REMOVE

    def test_remove_piece(self):
        self.move_handler.apply_move((0, 0), self.game_state)
        self.assertEqual(self.game_state.board.get_color_from_pos((0, 0)), PieceColor.EMPTY)

    def test_remove_piece_from_mill(self):
        self.game_state.board.assign_color_in_pos((0, 3), PieceColor.WHITE)
        self.game_state.board.assign_color_in_pos((0, 6), PieceColor.WHITE)
        self.game_state.board.assign_color_in_pos((3, 0), PieceColor.WHITE)
        self.move_handler.apply_move((0, 0), self.game_state)
        self.assertEqual(self.game_state.board.get_color_from_pos((0, 0)), PieceColor.WHITE)

    def test_remove_piece_from_only_mill(self):
        self.game_state.board.assign_color_in_pos((0, 3), PieceColor.WHITE)
        self.game_state.board.assign_color_in_pos((0, 6), PieceColor.WHITE)
        self.move_handler.apply_move((0, 0), self.game_state)
        self.assertEqual(self.game_state.board.get_color_from_pos((0, 0)), PieceColor.EMPTY)

if __name__ == "__main__":
    unittest.main()
