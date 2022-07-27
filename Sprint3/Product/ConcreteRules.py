from typing import List
from RuleSet import IRuleSet
from State import IState
from Board import IBoard
from InsertState import InsertState
from SelectState import SelectState, SelectWithFlyState
from MoveState import MoveState, FlyState
from RemoveState import RemoveState
from Player import IPlayer


class DefaultRules(IRuleSet):
    def __init__(self, player: IPlayer):
        self.insert_state = InsertState(self, player)
        self.select_state = SelectState(self, player)
        self.move_state = MoveState(self, player)
        self.remove_state = RemoveState(self, player)
        self._current_state = self.insert_state

    @property
    def current_state(self) -> IState:
        return self._current_state

    @current_state.setter
    def current_state(self, state: IState) -> None:
        self._current_state = state

    def make_move(self, pos: tuple, board: IBoard) -> None:
        self._current_state.make_move(pos, board)

    def get_possible_moves(self, board: IBoard) -> List[tuple]:
        return self._current_state.get_possible_moves(board)


class DefaultRulesWithFly(DefaultRules):
    def __init__(self, player: IPlayer):
        super().__init__(player)
        self.select_state = SelectWithFlyState(self, player)
        self.fly_state = FlyState(self, player)

