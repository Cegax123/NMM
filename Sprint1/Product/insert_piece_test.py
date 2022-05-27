#import sys
#sys.path.append("..\Product")
import unittest
from random import shuffle
from random import seed
from random import randint
from Board import Board
from Game import Game
import json

class TestInsertPiece(unittest.TestCase):
    
    def test_nine(self):
        with open('conf.json') as f:
            data=json.load(f)
            game_options = data['game']
            board_options = data['board']
            f.close()
        for k in range(10):
            g=Game('nine',None,None,None,board_options['first_color'],board_options['second_color'])
            x=[i for i in range(len(g.board.V))]
            shuffle(x)
            for i in x:
                r=board_options['radius_empty_vertex']
                m=board_options['total']//g.n-2*r
                x,y=g.board.V[i].pos_screen
                for j in range(100):
                    g.make_move((x+randint(2*r,m),y+randint(2*r,m)))
                    self.assertEqual(g.board.V[i].status,0)
                    g.make_move((x+randint(-m,-2*r),y+randint(-m,-2*r)))
                    self.assertEqual(g.board.V[i].status,0)
                g.make_move((x+randint(-r,r),y+randint(-r,r)))
                self.assertNotEqual(g.board.V[i].status,(int)(g.turn_player().pieces_to_insert==0))
            
        

if __name__ == '__main__':
    unittest.main()
