from abc import ABC, abstractmethod
from game.entities.enemy import Enemy
from game.battles.action import Action


class IOHandler(ABC):
    @abstractmethod
    def output(self, message: str) -> None:
        """Display some text to the player."""
        pass

    @abstractmethod
    def select_action(self, options: list[Action]) -> Action:
        """Player must choose an action from a list of options."""
        pass

    @abstractmethod
    def select_target(self, targets: list[Enemy]) -> Enemy:
        """Ask the player who to hit."""
        pass