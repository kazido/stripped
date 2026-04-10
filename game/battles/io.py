from abc import ABC, abstractmethod
from game.entities.base import Entity


class IOHandler(ABC):
    @abstractmethod
    def output(self, message: str) -> None:
        """Display some text to the player."""
        pass

    @abstractmethod
    def select_action(self, options: list[str]) -> str:
        """Player must choose an action from a list of options."""
        pass

    @abstractmethod
    def select_target(self, targets: list[Entity]) -> Entity:
        """Ask the player who to hit."""
        pass