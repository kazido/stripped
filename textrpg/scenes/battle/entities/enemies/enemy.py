from abc import ABC
from textrpg.scenes.battle.entities.combat_entity import CombatEntity
from textrpg.core.stats import Stat

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from textrpg.scenes.battle.battle import Battle
    

class Enemy(CombatEntity, ABC):
    NAME: str
    HEALTH: int
    SPEED: int
    DAMAGE: int

    def __init__(self, battle: Battle) -> None:
        super().__init__(battle)
        self.data.register(Stat.HEALTH, self.HEALTH)
        self.data.register(Stat.SPEED, self.SPEED)
    