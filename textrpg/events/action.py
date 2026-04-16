from abc import ABC, abstractmethod

class Action(ABC):
    """An action that a player can take in battle, depending on circumstances (weapons, enemies, etc)"""

    @abstractmethod
    def followup(self) -> None:
        pass


class Attack(Action):
    def followup(self) -> None:
        pass


class Leave(Action):
    pass