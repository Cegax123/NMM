from abc import ABC, abstractmethod
from dataclasses import dataclass
from PieceColor import PieceColor
from PlayerType import PlayerType
from BoardVariant import BoardVariant
import Player


class IPlayerBuilder(ABC):
    @abstractmethod
    def set_color(self, color: PieceColor) -> None:
        pass

    @abstractmethod
    def set_pieces_to_insert(self, pieces_to_insert: int) -> None:
        pass

    @abstractmethod
    def set_type_player(self, type_player: PlayerType) -> None:
        pass

    @abstractmethod
    def get_result(self) -> Player.IPlayer:
        pass


class PlayerBuilder(IPlayerBuilder):
    def set_color(self, color: PieceColor) -> None:
        self._color = color

    def set_pieces_to_insert(self, pieces_to_insert: int) -> None:
        self._pieces_to_insert = pieces_to_insert

    def set_type_player(self, type_player: PlayerType) -> None:
        self._type_player = type_player

    def get_result(self) -> Player.IPlayer:
        return Player.Player(self._color, self._pieces_to_insert, self._type_player)


@dataclass
class PlayerDirector:
    _builder: PlayerBuilder = PlayerBuilder()

    def build_three_men_morris_player(self) -> Player.IPlayer:
        self._builder.set_pieces_to_insert(3)
        return self._builder.get_result()

    def build_five_men_morris_player(self) -> Player.IPlayer:
        self._builder.set_pieces_to_insert(5)
        return self._builder.get_result()

    def build_nine_men_morris_player(self) -> Player.IPlayer:
        self._builder.set_pieces_to_insert(4)
        return self._builder.get_result()

    def build_player(self, board_variant: BoardVariant, color: PieceColor, type_player: PlayerType) -> Player.IPlayer:
        self._builder.set_color(color)
        self._builder.set_type_player(type_player)

        if board_variant == BoardVariant.THREE_MEN_MORRIS:
            return self.build_three_men_morris_player()
        elif board_variant == BoardVariant.FIVE_MEN_MORRIS:
            return self.build_five_men_morris_player()
        if board_variant == BoardVariant.NINE_MEN_MORRIS:
            return self.build_nine_men_morris_player()


