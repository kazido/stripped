from abc import ABC
from textrpg.core.entity import Entity
from textrpg.scenes.battle.util.stat_manager import Stat

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from textrpg.scenes.battle.battle import Battle
    

class Enemy(Entity, ABC):
    NAME: str
    HEALTH: int
    SPEED: int
    DAMAGE: int

    def __init__(self, battle: Battle) -> None:
        super().__init__(battle)
        self.data.register(Stat.HEALTH, self.HEALTH)
        self.data.register(Stat.SPEED, self.SPEED)
    