import sys
sys.path.append('../Product')

from Vertex import Vertex
from PieceColor import PieceColor
import unittest

class TestVertex(unittest.TestCase):
    def test_is_empty(self):
        v = Vertex((2, 3))
        self.assertEqual(v.piece_color, PieceColor.EMPTY)

if __name__ == "__main__":
    unittest.main()
