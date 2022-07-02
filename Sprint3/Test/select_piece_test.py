import sys
sys.path.append("../Product")

import unittest
from random import shuffle
from random import seed
from random import randint
from Board import Board
from Game import Game
import json



class TestSelectPiece(unittest.TestCase):

    def setUp(self):
        with open('../Product/conf.json') as f:
            settings=json.load(f)
            self.game_options = settings['game']
            self.board_options = settings['board']
            f.close()
        self.game = Game('nine', None, 'Player 1', 'Player 2', self.board_options['first_color'], self.board_options['second_color'] )
        self.game.board.insert_piece(self.game.current_player(),0)
        self.game.board.insert_piece(self.game.current_player(),3)
        self.game.board.insert_piece(self.game.current_player(),6)
        self.game.board.insert_piece(self.game.current_player(),15)
        self.game.board.insert_piece(self.game.other_player(),2)
        self.game.board.insert_piece(self.game.other_player(),5)
        self.game.board.insert_piece(self.game.other_player(),8)
        self.game.board.insert_piece(self.game.other_player(),17)
        self.game.current_player().status='select'
    def tearDown(self):
        pass
    
    def test_valid_cell(self):
        self.game.board.select_piece(self.game.current_player(),0)
        self.assertEqual(self.game.current_player().status,'move')

    def test_opponent_cell(self):
        self.game.board.select_piece(self.game.current_player(),2)
        self.assertEqual(self.game.current_player().status,'select')

if __name__ == '__main__':
    unittest.main()
