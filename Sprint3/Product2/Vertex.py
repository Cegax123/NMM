from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum


class PieceTurn(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = 2


@dataclass
class ICell(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def get_piece_turn(self) -> int:
        pass

    @abstractmethod
    def assign_piece_turn(self, turn: int) -> None:
        pass

    @abstractmethod
    def add_neighbor(self, neighbor: 'ICell') -> None:
        pass

    

# @dataclass
# class Vertex:
    # _pos: tuple
    # _piece: Piece = Piece.EMPTY
    # _neighbors: List['Vertex'] = field(default_factory=list)

    # def is_empty(self):
        # return self._player == None

    # def remove_player(self):
        # self._player = None

    # def get_neighbors_with_same_player(self) -> List['Vertex']:
        # return [neighbor for neighbor in self._neighbors
                # if self.player == neighbor.player]

    # def get_pos_empty_neighbors(self) -> List[tuple]:
        # return [neighbor.pos for neighbor in self._neighbors
                # if neighbor.is_empty()]

    # def add_neighbor(self, neighbor: 'Vertex') -> None:
        # self._neighbors.append(neighbor)

    # @staticmethod
    # def are_collinear(v1: 'Vertex' , v2: 'Vertex' , v3: 'Vertex'):
        # """Verificar si tres vertices son colineares"""

        # if (v1 not in v2._neighbors) or (v2 not in v3._neighbors):
            # return False

        # check_row = v2._pos[0]-v1._pos[0] == v3._pos[0]-v2._pos[0]
        # check_col = v2._pos[1]-v1._pos[1] == v3._pos[1]-v2._pos[1]

        # return check_row and check_col

    # def belongs_to_mill(self) -> bool:
        # if self.is_empty() == None:
            # return False

        # for v1 in self.get_neighbors_with_same_player():
            # for v3 in self.get_neighbors_with_same_player():
                # if v1 == v3:
                    # continue

                # if Vertex.are_collinear(v1, self, v3):
                    # return True

        # for v2 in self.get_neighbors_with_same_player():
            # for v3 in v2.get_neighbors_with_same_player():
                # if self == v3:
                    # continue

                # if Vertex.are_collinear(self, v2, v3):
                    # return True

        # return False
