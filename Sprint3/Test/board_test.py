import sys
sys.path.append("../Product")

from Vertex import Vertex
from PieceColor import PieceColor
from Board import  BoardNineMenMorris,Board
import unittest

class TestBoard(unittest.TestCase):

    def test_init_board(self):
        board = BoardNineMenMorris()

        self.assertEqual(board._rows,board._cols)
        num_vertex = 16
        self.assertEqual(num_vertex,len(board._vertexes))
        
    def test_vertex_in_board(self):
        board = BoardNineMenMorris()
        vertex1 = Vertex((0,0))
        vertex2 = Vertex((0,3))
        
        self.assertFalse(board._vertexes.count(vertex1))
        self.assertFalse(board._vertexes.count(vertex2))
        self.assertEqual(Vertex((0,0))._pos,board._vertexes[0]._pos)
        self.assertEqual(Vertex((0,2))._pos,board._vertexes[1]._pos)    
        self.assertEqual(Vertex((0,4))._pos,board._vertexes[2]._pos)    
        self.assertEqual(Vertex((1,1))._pos,board._vertexes[3]._pos)     
    
    def test_pos_in_board(self):
        board = BoardNineMenMorris()
        pos0 = (0,0)  
        pos1 = (1,1)
        pos2 = (-2,101203)
        pos3 = (0,1)
        
        self.assertIn(pos0,board._positions)
        self.assertIn(pos1,board._positions)
        self.assertFalse(board.valid_position(pos2))
        self.assertFalse(board.valid_position(pos3))
if __name__ == "__main__":
    unittest.main()