from typing import List
from BoardVariant import BoardVariant
import Board


class BoardBuilder:
    def set_rows(self, rows: int):
        self._rows = rows

    def set_cols(self, cols: int):
        self._cols = cols

    def set_positions(self, positions: List[tuple]):
        self._positions = positions

    def set_edges(self, edges: List[tuple]):
        self._edges = edges

    def get_result(self) -> Board.IBoard:
        return Board.Board(self._rows, self._cols, self._positions, self._edges)


class BoardDirector:
    @property
    def builder(self) -> BoardBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: BoardBuilder):
        self._builder = builder

    def build_board(self, game_variant: BoardVariant) -> None:
        if game_variant == BoardVariant.THREE_MEN_MORRIS:
            self.build_three_men_morris_board()

        elif game_variant == BoardVariant.NINE_MEN_MORRIS:
            self.build_nine_men_morris()

    def build_three_men_morris_board(self):
        self._builder.set_rows(3)
        self._builder.set_cols(3)

        positions = [(0, 0), (0, 1), (0, 2),
                     (1, 0), (1, 1), (1, 2),
                     (2, 0), (2, 1), (2, 2)]

        self._builder.set_positions(positions)

        edges = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8),
                 (0, 3), (0, 6), (1, 4), (4, 7), (2, 5), (5, 6),
                 (0, 4), (4, 8), (2, 4), (4, 6)]

        self._builder.set_edges(edges)

    def build_nine_men_morris(self):
        self._builder.set_rows(5)
        self._builder.set_cols(5)

        positions = [(0, 0), (0, 2), (0, 4), (1, 1), (1, 2), (1, 3),
                     (2, 0), (2, 1), (2, 3), (2, 4),
                     (3, 1), (3, 2), (3, 3), (4, 0), (4, 2), (4, 4)]

        self._builder.set_positions(positions)

        edges = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (8, 9),
                 (10, 11), (11, 12), (13, 14), (14, 15),
                 (0, 6), (6, 13), (3, 7), (7, 10), (1, 4),
                 (11, 14), (5, 8), (8, 12), (2, 9), (9, 15)]

        self._builder.set_edges(edges)


