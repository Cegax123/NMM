import sys
sys.path.append("../Product")

import unittest
from random import shuffle
from random import seed
from random import randint
from Board import Board
from Game import Game
import json



class TestRemovePiece(unittest.TestCase):

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
    
    def test_notMill_cell(self):
        self.game.board.remove_piece(self.game.current_player(),self.game.other_player(),17)
        self.assertEqual(self.game.board.V[17].status,0)

    def test_mill_cell(self):
        self.game.board.remove_piece(self.game.current_player(),self.game.other_player(),22)
        self.assertEqual(self.game.board.V[22].status,self.game.other_player().turn)



if __name__ == '__main__':
    unittest.main()
