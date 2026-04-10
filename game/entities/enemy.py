import random
from abc import ABC
from enum import Enum

from .player import Player
from game.battles.io import IOHandler


# region Enemy Base Class

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
        return self.nature.name.capitalize() + self.NAME
    

    def take_turn(self, players: list[Player], handler: IOHandler) -> None:
        pass
    

    def pre_battle(self) -> None:
        """Anything that needs to happen at the start of battles (special messages)."""
        pass

    def post_battle(self) -> None:
        """Anything that needs to happen at the end of battles (special messages)."""
        pass
    
# endregion


# region Enemies


class Goblin(Enemy):
    NAME = "Goblin"
    BASE_HP = 10
    BASE_SPEED = 8
    DAMAGE = 3

    def take_turn(self, players, handler) -> None:
        # Goblins always attack the player with the most gold.
        richest = max(players, key=lambda p: p.gold)
        handler.output(f"{self} is eyeing {richest}...")


class Centaur(Enemy):
    NAME = "Centaur"
    BASE_HP = 50
    BASE_SPEED = 25
    DAMAGE = 15

    def take_turn(self, players, handler) -> None:
        pass


class UnstableDrone(Enemy):
    """After three turns, the Mazhinx will self-destruct."""
    name = "Unstable Drone"
    BASE_HP = 100
    BASE_SPEED = 1
    DAMAGE = 100

    def __init__(self) -> None:
        super().__init__()
        self.turns_to_destruct: int = 3

    def take_turn(self, players, handler) -> None:
        self.turns_to_destruct -= 1
        if self.turns_to_destruct <= 0:
            for player in players:
                if player.take_damage(self.DAMAGE):
                    handler.output(f"{str(player)} has died.")


# endregion