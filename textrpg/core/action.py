from abc import ABC, abstractmethod

from textrpg.core.entity import Entity
from textrpg.core.scene import Scene

class Action(ABC):
    """An action that a player can take in a scene."""
    label: str  # "Attack", "Cast Net", "Swing Pickaxe"

    @abstractmethod
    def execute(self, actor: Entity, scene: Scene) -> None:
        pass

