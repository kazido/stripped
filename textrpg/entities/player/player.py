from __future__ import annotations

from textrpg.items.armor import Armor
from textrpg.entities.player.save_data import PlayerSaveData
from textrpg.scenes.battle.util.stat_manager import Stat
from textrpg.core.entity import Entity
from textrpg.items import ITEM_REGISTRY

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from textrpg.scenes.battle.battle import Battle



class Player(Entity):
    def __init__(self, battle: Battle, account: PlayerSaveData) -> None:
        super().__init__(battle)
        # Load our player's data from the database once
        self.account = account
        self.data.register(Stat.HEALTH, 10)
        self.data.register(Stat.SPEED, 10)


    def take_turn(self) -> None:
        pass


    def _get_gear_hp_bonus(self) -> int:
        bonus = 0
        for item in self.account.inventory:
            item_class = ITEM_REGISTRY.get(item.item_id)
            if item_class and issubclass(item_class, Armor):
                bonus += item_class.hp_bonus
        return bonus

    
    def gain_skill_xp(self, skill_name: str, amount: int) -> None:
        skill = getattr(self.account, skill_name)
    
    def __str__(self) -> str:
        return f"{self.account.name}"