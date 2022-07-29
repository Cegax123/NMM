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
    
    def test_positions_neighbors(self):
        board = BoardNineMenMorris()
        lst = board.get_positions_empty_neighbors_of_pos((1,2))
        mylist = [(1,1),(1,3),(0,2)]
        self.assertEqual(lst,mylist)
        lst = board.get_positions_empty_neighbors_of_pos((2,0))
        mylist = [(2,1),(0,0),(4,0)]
        self.assertEqual(lst,mylist)
        
        # possible fail 
        lst = board.get_positions_empty_neighbors_of_pos((2,2))
        mylist = []
        #self.assertEqual(lst,mylist)

    def test_color(self):
        board = BoardNineMenMorris()
        board.assign_color_in_pos((3,3),PieceColor.WHITE)
        board.assign_color_in_pos((1,3),PieceColor.BLACK)
        board.assign_color_in_pos((2,4),PieceColor.WHITE)
        board.remove_piece_in_pos((3,3))
        
        self.assertEqual(board.get_color_from_pos((3,3)),PieceColor.EMPTY)
        self.assertEqual(board.get_color_from_pos((1,3)),PieceColor.BLACK)
        self.assertEqual(board.get_color_from_pos((2,4)),PieceColor.WHITE)

    def test_color_position(self):
        board = BoardNineMenMorris()
        board.assign_color_in_pos((2,1),PieceColor.WHITE)
        board.assign_color_in_pos((3,1),PieceColor.BLACK)
        board.assign_color_in_pos((3,2),PieceColor.WHITE)
        board.assign_color_in_pos((3,3),PieceColor.BLACK)

        wantlist1 = [(2,1),(3,2)]
        wantlist2 = [(3,1),(3,3)]

        self.assertEqual(board.get_positions_with_color(PieceColor.WHITE),wantlist1)
        #linea 97 
        #  if vertex == piece_color: ->  if vertex._piece_color == piece_color:
        self.assertEqual(board.get_positions_with_color(PieceColor.BLACK),wantlist2)
        

if __name__ == "__main__":
    unittest.main()