import sys
sys.path.append("../Product")

import unittest
from random import shuffle
from random import seed
from random import randint
from Board import Board
from Game import Game
import json



class TestCheckMill(unittest.TestCase):

    def setUp(self):
        with open('../Product/conf.json') as f:
            settings=json.load(f)
            self.game_options = settings['game']
            self.board_options = settings['board']
            f.close()
        self.game = Game('nine', None, 'Player 1', 'Player 2', self.board_options['first_color'], self.board_options['second_color'] )
        self.game.board.insert_piece(self.game.current_player(),0)
        self.game.board.insert_piece(self.game.current_player(),3)
        self.game.board.insert_piece(self.game.current_player(),4)
        self.game.board.insert_piece(self.game.current_player(),2)
        self.game.board.insert_piece(self.game.other_player(),21)
        self.game.board.insert_piece(self.game.other_player(),23)
        self.game.board.insert_piece(self.game.other_player(),17)
    def tearDown(self):
        pass
    
    def test_insertMill(self):
        self.game.current_player().pieces_to_insert=1
        self.game.board.insert_piece(self.game.current_player(),1)
        self.assertEqual(self.game.current_player().status,'remove')

    def test_moveMill(self):
        self.game.current_player().pieces_to_insert=0
        self.game.board.select_piece(self.game.current_player(),4)
        self.game.board.move_piece(self.game.current_player(),1)
        self.assertEqual(self.game.current_player().status,'remove')

    def test_flyMill(self):
        self.game.other_player().pieces_to_insert=0
        self.game.board.select_piece(self.game.other_player(),17)
        self.game.board.fly_piece(self.game.other_player(),22)
        self.assertEqual(self.game.other_player().status,'remove')



if __name__ == '__main__':
    unittest.main()
