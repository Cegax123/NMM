from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
from PieceColor import PieceColor
from Vertex import IVertex, Vertex


class IBoard(ABC):
    @abstractmethod
    def get_positions_empty_neighbors_of_pos(self, pos: tuple) -> List[tuple]:
        pass

    @abstractmethod
    def get_positions_empty_vertexes(self) -> List[tuple]:
        pass

    @abstractmethod
    def get_positions_with_color(self, piece_color: PieceColor) -> List[tuple]:
        pass

    @abstractmethod
    def assign_color_in_pos(self, pos: tuple, piece_color: PieceColor) -> None:
        pass

    @abstractmethod
    def remove_piece_in_pos(self, pos: tuple) -> None:
        pass

    @abstractmethod
    def get_color_from_pos(self, pos: tuple) -> PieceColor:
        pass

    @abstractmethod
    def valid_position(self, pos: tuple) -> bool:
        pass

    @abstractmethod
    def check_mill_in_pos(self, pos: tuple) -> bool:
        pass

    @property
    @abstractmethod
    def rows(self) -> int:
        pass

    @property
    @abstractmethod
    def cols(self) -> int:
        pass

    @property
    @abstractmethod
    def positions(self) -> List[tuple]:
        pass

    @property
    @abstractmethod
    def edges(self) -> List[tuple]:
        pass

@dataclass
class Board(IBoard, ABC):
    def __init__(self, rows, cols, positions, edges):
        self._rows = rows
        self._cols = cols
        self._positions = positions
        self._edges = edges

        self._vertexes: List[IVertex] = []

        self._add_vertexes_from_positions(positions)
        self._add_neighbors_from_edges(edges)

    @property
    def positions(self) -> List[tuple]:
        return self._positions

    @property
    def edges(self) -> List[tuple]:
        return self._edges

    def get_positions_empty_neighbors_of_pos(self, pos: tuple) -> List[tuple]:
        positions = []
        current_vertex = self._get_vertex_by_pos(pos)

        for vertex in current_vertex.neighbors:
            if vertex.is_empty():
                positions.append(vertex.pos)

        return positions

    def get_positions_empty_vertexes(self) -> List[tuple]:
        positions = []

        for vertex in self._vertexes:
            if vertex.is_empty():
                positions.append(vertex.pos)

        return positions

    def get_positions_with_color(self, piece_color: PieceColor) -> List[tuple]:
        positions = []

        for vertex in self._vertexes:
            if vertex.piece_color == piece_color:
                positions.append(vertex.pos)

        return positions

    def assign_color_in_pos(self, pos: tuple, piece_color: PieceColor) -> None:
        self._get_vertex_by_pos(pos).piece_color = piece_color

    def remove_piece_in_pos(self, pos: tuple) -> None:
        self._get_vertex_by_pos(pos).piece_color = PieceColor.EMPTY

    def get_color_from_pos(self, pos: tuple) -> PieceColor:
        return self._get_vertex_by_pos(pos).piece_color

    def valid_position(self, pos: tuple) -> bool:
        for vertex in self._vertexes:
            if pos == vertex.pos:
                return True

        return False

    def check_mill_in_pos(self, pos: tuple) -> bool:
        return self._get_vertex_by_pos(pos).belong_to_mill()

    def _get_vertex_by_pos(self, pos: tuple) -> IVertex:
        result = self._vertexes[0]

        for vertex in self._vertexes:
            if pos == vertex.pos:
                result = vertex

        return result

    def _add_vertexes_from_positions(self, positions) -> None:
        for pos in positions:
            self._vertexes.append(Vertex(pos))

    def _add_neighbors_from_edges(self, edges) -> None:
        for v1, v2 in edges:
            self._vertexes[v1].add_neighbor(self._vertexes[v2])
            self._vertexes[v2].add_neighbor(self._vertexes[v1])

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

