import sys
sys.path.append("../Product")

from Vertex import Vertex
from PieceColor import PieceColor
import unittest

list_neighbors = []

class TestVertex(unittest.TestCase):

    def setUp(self):
        self.current_vertex =  Vertex((2,3))     
    
        list_neighbors.append(Vertex((1,2)))
        list_neighbors.append(Vertex((3,454)))
        
        
    def test_is_empty(self):
        self.assertEqual(self.current_vertex.piece_color,PieceColor.EMPTY)
    
    def test_neighbors(self):
            
        for obj  in list_neighbors:
            self.current_vertex.add_neighbor(obj)

        self.assertEqual(self.current_vertex.neighbors,list_neighbors)
    
    def test_belong_to_mill(self):
         
        for obj  in list_neighbors:
            self.current_vertex.add_neighbor(obj)
        



        
        self.assertTrue(self.current_vertex.belong_to_mill)
    
if __name__ =="__main__":
    unittest.main()