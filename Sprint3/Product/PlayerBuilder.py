from abc import ABC, abstractmethod
from dataclasses import dataclass
from PieceColor import PieceColor
import Player
import DefaultMoveSet
import DefaultWithFlyMoveSet


class IPlayerBuilder(ABC):
    @abstractmethod
    def set_color(self, color: PieceColor) -> None:
        pass

    @abstractmethod
    def set_pieces_to_insert(self, pieces_to_insert: int) -> None:
        pass

    @abstractmethod
    def set_move_set(self, move_set) -> None:
        pass

    @abstractmethod
    def get_result(self) -> Player.IPlayer:
        pass


class HumanPlayerBuilder(IPlayerBuilder):
    def set_color(self, color: PieceColor) -> None:
        self._color = color

    def set_pieces_to_insert(self, pieces_to_insert: int) -> None:
        self._pieces_to_insert = pieces_to_insert

    def set_move_set(self, move_set) -> None:
        self._move_set = move_set

    def get_result(self) -> Player.IPlayer:
        return Player.HumanPlayer(self._color, self._pieces_to_insert, self._move_set)


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
        self._builder.set_move_set(DefaultMoveSet.DefaultMoveSet())

        return self._builder.get_result()

    def build_five_men_morris_player(self, color: PieceColor) -> Player.IPlayer:
        self._builder.set_color(color)
        self._builder.set_pieces_to_insert(5)
        self._builder.set_move_set(DefaultMoveSet.DefaultMoveSet())

        return self._builder.get_result()

    def build_nine_men_morris_player(self, color: PieceColor) -> Player.IPlayer:
        self._builder.set_color(color)
        self._builder.set_pieces_to_insert(9)
        self._builder.set_move_set(DefaultWithFlyMoveSet.DefaultRulesWithFly(3))

        return self._builder.get_result()

