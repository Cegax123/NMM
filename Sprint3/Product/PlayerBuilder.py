from abc import ABC, abstractmethod
from dataclasses import dataclass
from PieceColor import PieceColor
import Player


class IPlayerBuilder(ABC):
    @abstractmethod
    def set_color(self, color: PieceColor) -> None:
        pass

    @abstractmethod
    def set_pieces_to_insert(self, pieces_to_insert: int) -> None:
        pass

    @abstractmethod
    def get_result(self) -> Player.IPlayer:
        pass


class HumanPlayerBuilder(IPlayerBuilder):
    def set_color(self, color: PieceColor) -> None:
        self._color = color

    def set_pieces_to_insert(self, pieces_to_insert: int) -> None:
        self._pieces_to_insert = pieces_to_insert

    def get_result(self) -> Player.IPlayer:
        return Player.HumanPlayer(self._color, self._pieces_to_insert)


@dataclass
class PlayerDirector:
    @property
    def builder(self) -> IPlayerBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder) -> None:
        self._builder = builder

    def build_three_men_morris_player(self, color: PieceColor) -> Player.IPlayer:
        self._builder.set_color(color)
        self._builder.set_pieces_to_insert(3)

        return self._builder.get_result()

    def build_five_men_morris_player(self, color: PieceColor) -> Player.IPlayer:
        self._builder.set_color(color)
        self._builder.set_pieces_to_insert(5)

        return self._builder.get_result()

    def build_nine_men_morris_player(self, color: PieceColor) -> Player.IPlayer:
        self._builder.set_color(color)
        self._builder.set_pieces_to_insert(9)

        return self._builder.get_result()

