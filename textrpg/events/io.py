from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from textrpg.events.action import Action
from textrpg.events.event import Event

if TYPE_CHECKING:
    from textrpg.entities.enemy.enemy import Enemy


class IOHandler(ABC):
    @abstractmethod
    def output(self, message: str) -> None:
        """Display some text to the player."""
        pass

    @abstractmethod
    def output_event(self, event: Event) -> None:
        """Display an event to the player."""
        pass

    @abstractmethod
    def select_action(self, options: list[Action]) -> Action:
        """Player must choose an action from a list of options."""
        pass

    @abstractmethod
    def select_target(self, targets: list[Enemy]) -> Enemy:
        """Ask the player who to hit."""
        pass