from __future__ import annotations

from textrpg.items.armor import Armor
from textrpg.util.damage_source import DamageSource
from textrpg.entities.player.save_data import PlayerSaveData
from textrpg.items import ITEM_REGISTRY



class Player:
    def __init__(self, save_data: PlayerSaveData) -> None:
        # Load our player's data from the database once
        self.data = save_data
        self.current_hp = self.max_hp


    def _get_gear_hp_bonus(self) -> int:
        bonus = 0
        for item in self.data.inventory:
            item_class = ITEM_REGISTRY.get(item.item_id)
            if item_class and issubclass(item_class, Armor):
                bonus += item_class.hp_bonus
        return bonus

    @property
    def max_hp(self) -> int:
        return 25 + (self.data.combat.level * 5) + self._get_gear_hp_bonus()
    
    @property
    def speed(self) -> int:
        level_bonus = self.data.level
        return 10 + level_bonus
    
    def gain_skill_xp(self, skill_name: str, amount: int) -> None:
        skill = getattr(self.data, skill_name)


    def take_damage(self, source: DamageSource, amount: int) -> None:
        """Returns True if dead."""
        self.current_hp -= amount
    
    @property
    def is_dead(self) -> bool:
        return self.current_hp <= 0
    
    def __str__(self) -> str:
        return f"{self.data.name}"