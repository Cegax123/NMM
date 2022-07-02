import sys
sys.path.append("../Product")

import unittest
from random import shuffle
from random import seed
from random import randint
from Board import Board
from Game import Game
import json



class TestWinner(unittest.TestCase):

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
        self.game.board.insert_piece(self.game.current_player(),11)
        self.game.board.insert_piece(self.game.other_player(),21)
        self.game.board.insert_piece(self.game.other_player(),22)
        self.game.board.insert_piece(self.game.other_player(),23)
        self.game.board.insert_piece(self.game.other_player(),17)
    def tearDown(self):
        pass
    
    def test_secondWin(self):
        self.game.current_player().pieces_to_insert=0
        self.game.current_player().pieces_in_board=2
        self.assertEqual(self.game.current_player().lost_game(),True)

    def test_firstWin(self):
        self.game.other_player().pieces_to_insert=0
        self.game.other_player().pieces_in_board=2
        self.assertEqual(self.game.other_player().lost_game(),True)



if __name__ == '__main__':
    unittest.main()
