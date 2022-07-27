import sys
sys.path.append("../Product")

from Vertex import Vertex
from PieceColor import PieceColor
import unittest

class TestVertex(unittest.TestCase):
    def test_is_empty(self):
        v = Vertex((2,3))
        self.assertEqual(v.piece_color,PieceColor.EMPTY)
    
    def test_neighbors(self):
        v = Vertex((2,3))
        
        list_neighbors = []
        list_neighbors.append(Vertex(1,1))
        list_neighbors.append(Vertex(5,4))
        list_neighbors.append(Vertex(1,1))

        for obj  in list_neighbors:
            v.add_neighbor(obj)
        
        self.assertEqual(v.neighbors,list_neighbors)
    
    def test_belong_to_mill(self):
        v = Vertex((2,3))
        
        list_neighbors = []
        list_neighbors.append(Vertex(1,3))
        list_neighbors.append(Vertex(3,3))
        
        for obj  in list_neighbors:
            v.add_neighbor(obj)
        
        self.assertTrue(v.belong_to_mill)


        
if __name__ =="__main__":
    unittest.main()
        