from abc import ABC, abstractmethod


class ObserverPlayer(ABC):
    @abstractmethod
    def update_selected_pos(self):
        pass