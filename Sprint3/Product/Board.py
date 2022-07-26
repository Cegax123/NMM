from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
from PieceColor import PieceColor
from Vertex import IVertex, Vertex


class IBoard(ABC):
    @abstractmethod
    def get_positions_adyacent_neighbors_of_pos(self, pos: tuple) -> List[tuple]:
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


@dataclass
class Board(IBoard, ABC):
    _rows: int = 0
    _cols: int = 0
    _positions: List[tuple] = field(default_factory=list)
    _edges: List[tuple] = field(default_factory=list)
    _vertexes: List[IVertex] = field(default_factory=list)

    @abstractmethod
    def _define_positions(self) -> None:
        """ Añade todas las posibles posiciones del tablero """

    @abstractmethod
    def _define_edges(self) -> None:
        """ Añade todos los vecinos de cada 'vertex' """

    def __post_init__(self) -> None:
        self._define_positions()
        self._define_edges()

        if self._rows < 0:
            raise Exception('Invalid number of rows')

        if self._cols < 0:
            raise Exception('Invalid number of columns')

        for vertex in self._vertexes:
            pos = vertex.pos

            if pos[0] < 0 or pos[0] >= self._rows or pos[1] < 0 or pos[1] >= self._cols:
                raise Exception('Invalid position ' + str(pos) + ' in board')

    def get_positions_adyacent_neighbors_of_pos(self, pos: tuple) -> List[tuple]:
        positions = []
        current_vertex = self._get_vertex_by_pos(pos)

        for vertex in current_vertex.neighbors:
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
            if vertex == piece_color:
                positions.append(vertex.pos)

        return positions

    def assign_color_in_pos(self, pos: tuple, piece_color: PieceColor) -> None:
        self._get_vertex_by_pos(pos).piece_color = piece_color

    def remove_piece_in_pos(self, pos: tuple) -> None:
        self._get_vertex_by_pos(pos).piece_color = PieceColor.EMPTY

    def get_color_from_pos(self, pos: tuple) -> PieceColor:
        return self._get_vertex_by_pos(pos).piece_color

    def valid_position(self, pos: tuple) -> bool:
        return pos in self._positions

    def check_mill_in_pos(self, pos: tuple) -> bool:
        return self._get_vertex_by_pos(pos).belong_to_mill()

    def _get_vertex_by_pos(self, pos: tuple) -> IVertex:
        result = self._vertexes[0]

        for vertex in self._vertexes:
            if pos == vertex.pos:
                result = vertex

        return result

    def _add_vertexes_from_positions(self) -> None:
        for pos in self._positions:
            self._vertexes.append(Vertex(pos))

    def _add_neighbors_from_edges(self) -> None:
        for v1, v2 in self._edges:
            self._vertexes[v1].add_neighbor(self._vertexes[v2])
            self._vertexes[v2].add_neighbor(self._vertexes[v1])


class BoardThreeMenMorris(Board):
    def _define_positions(self) -> None:
        self._rows = 3
        self._cols = 3

        self._positions = [(0, 0), (0, 1), (0, 2),
                           (1, 0), (1, 1), (1, 2),
                           (2, 0), (2, 1), (2, 2)]

        self._add_vertexes_from_positions()

    def _define_edges(self) -> None:
        self._edges = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8),
                       (0, 3), (0, 6), (1, 4), (4, 7), (2, 5), (5, 6),
                       (0, 4), (4, 8), (2, 4), (4, 6)]

        self._add_neighbors_from_edges()


class BoardNineMenMorris(Board):
    def _define_positions(self) -> None:
        self._rows = 5
        self._cols = 5

        self._positions = [(0, 0), (0, 2), (0, 4), (1, 1), (1, 2), (1, 3),
                           (2, 0), (2, 1), (2, 3), (2, 4),
                           (3, 1), (3, 2), (3, 3), (4, 0), (4, 2), (4, 4)]

        self._add_vertexes_from_positions()

    def _define_edges(self) -> None:
        self._edges = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (8, 9),
                       (10, 11), (11, 12), (13, 14), (14, 15),
                       (0, 6), (6, 13), (3, 7), (7, 10), (1, 4),
                       (11, 14), (5, 8), (8, 12), (2, 9), (9, 15)]

        self._add_neighbors_from_edges()


