from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
from PieceColor import PieceColor


class IVertex(ABC):
    @property
    @abstractmethod
    def pos(self) -> tuple:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @property
    @abstractmethod
    def piece_color(self) -> PieceColor:
        pass

    @piece_color.setter
    @abstractmethod
    def piece_color(self, piece_color) -> None:
        pass

    @abstractmethod
    def add_neighbor(self, neighbor: 'IVertex') -> None:
        pass

    @property
    @abstractmethod
    def neighbors(self) -> List['IVertex']:
        pass

    @abstractmethod
    def belong_to_mill(self) -> bool:
        pass


@dataclass
class Vertex(IVertex):
    _pos: tuple
    _piece_color: PieceColor = PieceColor.EMPTY
    _neighbors: List[IVertex] = field(default_factory=list)

    @property
    def pos(self) -> tuple:
        return self._pos

    def is_empty(self) -> bool:
        return self._piece_color == PieceColor.EMPTY

    @property
    def piece_color(self) -> PieceColor:
        return self._piece_color

    @piece_color.setter
    def piece_color(self, piece_color) -> None:
        self._piece_color = piece_color

    def add_neighbor(self, neighbor: IVertex) -> None:
        self._neighbors.append(neighbor)

    @property
    def neighbors(self) -> List[IVertex]:
        return self._neighbors

    @staticmethod
    def are_collinear(v1: IVertex, v2: IVertex, v3: IVertex):
        check_0 = v2.pos[0] - v1.pos[0] == v3.pos[0] - v2.pos[0]
        check_1 = v2.pos[1] - v1.pos[1] == v3.pos[1] - v2.pos[1]

        return check_0 and check_1

    def belong_to_mill(self) -> bool:
        if self.is_empty():
            return False

        for v1 in self.neighbors:
            for v2 in self.neighbors:
                if v1 == v2: continue
                if not self.piece_color == v1.piece_color == v2.piece_color:
                    continue

                if Vertex.are_collinear(v1, self, v2):
                    return True

        for v1 in self.neighbors:
            for v2 in v1.neighbors:
                if v2 == self: continue
                if not self.piece_color == v1.piece_color == v2.piece_color:
                    continue

                if Vertex.are_collinear(self, v1, v2):
                    return True

        return False


