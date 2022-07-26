import sys
sys.path.append("../Product")

import unittest
from Board import Board
import json



class TestInsertPiece(unittest.TestCase):

    def setUp(self):
        with open('../Product/conf.json') as f:
            settings=json.load(f)
            self.game_options = settings['game']
            self.board_options = settings['board']
            f.close()
        self.game = Game('nine', None, 'Player 1', 'Player 2', self.board_options['first_color'], self.board_options['second_color'] )
    
    def tearDown(self):
        pass
    
    def test_empty_cell(self):
        id = randint(0,len(self.game.board.V))
        self.game.board.insert_piece(self.game.current_player(),id)
        self.assertEqual(self.game.board.V[id].status,self.game.current_player().turn)

    def test_ocuped_cell(self):
        id = randint(0,len(self.game.board.V))
        self.game.board.insert_piece(self.game.current_player(),id)
        self.game.board.insert_piece(self.game.other_player(),id)
        self.assertNotEqual(self.game.board.V[id].status,self.game.other_player().turn)

if __name__ == '__main__':
    unittest.main()
