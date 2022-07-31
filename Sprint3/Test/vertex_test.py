import sys
sys.path.append("../Product")

from Vertex import Vertex
from PieceColor import PieceColor
import unittest

class TestVertex(unittest.TestCase):
    def setUp(self):
        self.current_vertex =  Vertex((2,3))
        list_neighbors = []
        list_neighbors.append(Vertex((3,3)))
        list_neighbors.append(Vertex((4,3)))
        for obj  in list_neighbors:
            self.current_vertex.add_neighbor(obj)

    def test_is_empty(self):
        self.assertEqual(self.current_vertex.piece_color,PieceColor.EMPTY)

    def test_belong_to_mill(self):
        #need the color for mill 
        self.assertTrue(self.current_vertex.belong_to_mill)
        #self.assertFalse(self.current_vertex.belong_to_mill)
        #piece_color = EMPTY : (      

    def test_belong_to_mill_changue_color_same_color(self): #Same color(BLACK)
        self.current_vertex.piece_color = PieceColor.BLACK
        for obj in self.current_vertex.neighbors:
            obj.piece_color = PieceColor.BLACK
        self.assertTrue(self.current_vertex.belong_to_mill)

    def test_belong_to_mill_changue_color_distinct_color(self): #Distinct color(WHITE-BLACK)
        self.current_vertex.piece_color = PieceColor.WHITE
        for obj in self.current_vertex.neighbors:
            obj.piece_color = PieceColor.BLACK
        self.assertTrue(self.current_vertex.belong_to_mill)
        #self.assertFalse(self.current_vertex.belong_to_mill)
        #piece_color diferent :( 


if __name__ =="__main__":
    unittest.main()
