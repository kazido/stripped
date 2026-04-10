import random
from abc import ABC
from enum import Enum
from .base import Entity
from .player import Player


class Nature(Enum):
    CAREFREE = -2
    SERIOUS = 3
    GIANT = 10


class Enemy(Entity, ABC):
    # Default stats, no need to add them to instanced object
    base_hp: int = 0
    base_speed: int = 0
    damage: int = 0

    def __init__(self) -> None:
        self.nature = random.choice(list(Nature))
        super().__init__()

    @property
    def max_hp(self) -> int:
        # TODO: Handle any HP modifiers (like nature)
        return self.base_hp + self.nature.value
    
    @property
    def speed(self) -> int:
        # TODO: Handle any speed modifiers (like nature)
        return self.base_speed
    
    def __str__(self) -> str:
        return self.nature.name.capitalize()

    def get_players(self, targets: list[Entity]) -> list[Player]:
        """Get a list of all alive player targets in the battle."""
        return [t for t in targets if isinstance(t, Player) and not t.is_dead]