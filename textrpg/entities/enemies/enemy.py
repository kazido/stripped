from __future__ import annotations

import random
from abc import ABC
from enum import Enum

from ...player.player import Player
from textrpg.events.event import EntityDeathEvent, DamageDealtEvent


class Nature(Enum):
    CAREFREE = -2
    SERIOUS = 3
    GIANT = 10


class Enemy(ABC):
    # Default stats, no need to add them to instanced object
    NAME: str
    BASE_HP: int = 0
    BASE_SPEED: int = 0
    DAMAGE: int = 0

    def __init__(self) -> None:
        # Pick a nature
        self.nature = random.choice(list(Nature))

        # Prepare battle state
        self.current_hp = max(1, self.BASE_HP + self.nature.value)
        self.speed = self.BASE_SPEED
    
    def __str__(self) -> str:
        return f"{self.nature.name.capitalize()} {self.NAME}"
    
    @property
    def is_dead(self) -> bool:
        return self.current_hp <= 0
    

    def take_damage(self, attacker: Player) -> None:
        """Returns True if dead."""
        # TODO: FIX FIX FIX
        self.current_hp -= 5
    

    def take_turn(self, players: list[Player]) -> None:
        pass
    

    def pre_battle(self, players: list[Player]) -> None:
        """Anything that needs to happen at the start of battles (special messages)."""
        pass

    def post_battle(self, players: list[Player]) -> None:
        """Anything that needs to happen at the end of battles (special messages)."""
        pass

    def process_status_effects(self) -> None:
        # Write default behavior to process all status effects
        # If an enemy shouldn't, just overwrite this.
        raise NotImplementedError