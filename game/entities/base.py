from __future__ import annotations
from typing import Callable
from abc import ABC, abstractmethod


class Entity(ABC):
    NAME: str
    BASE_HP: int
    SPEED: int

    def __init__(self) -> None:
        # Need this to track the entity's HP
        self.current_hp = self.BASE_HP
        self.speed = self.SPEED

    @property  # Property here let's us calculate our value and it's also read-only
    def is_dead(self) -> bool:
        return self.current_hp <= 0
    
    @abstractmethod
    def take_turn(self, targets: list[Entity], log: Callable[[str], None]) -> None:
        pass

    def __str__(self) -> str:
        return  f"{self.NAME}"