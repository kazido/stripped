from .base import Entity
from game.items.armor import Armor
from game.save.save_data import PlayerSaveData
from game.items import ITEM_REGISTRY

class Player(Entity):
    def __init__(self, save_data: PlayerSaveData) -> None:
        self.data = save_data
        super().__init__()


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
    
    @property
    def name(self) -> str:
        return self.data.name
    
    @property
    def gold(self) -> int:
        return self.data.gold
    

    def take_turn(self, targets: list[Entity], log) -> None:
        pass

    def take_damage(self, amount: int) -> bool:
        """Returns True if dead."""
        self.current_hp -= amount
        return self.is_dead