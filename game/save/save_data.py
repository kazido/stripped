import math
from dataclasses import dataclass, field


#region SKILLS
@dataclass
class Skill:
    xp: int = 0

    def add_xp(self, amount: int) -> bool:
        """Returns True if a level-up occurred."""
        old_level = self.level
        self.xp += amount
        return self.level > old_level

    @property
    def level(self) -> int:
        # 0.1 is the speed of leveling
        return int(0.1 * math.sqrt(self.xp)) + 1


@dataclass
class Combat(Skill):
    pass


@dataclass
class Mining(Skill):
    pass


@dataclass
class Foraging(Skill):
    pass


@dataclass
class Fishing(Skill):
    pass


@dataclass
class Farming(Skill):
    pass
#endregion


@dataclass
class InventoryItem:
    item_id: str
    quantity: int


@dataclass
class Equipment:
    equipped_weapon_id:         str | None = None
    equipped_helmet_id:         str | None = None
    equipped_chestplate_id:     str | None = None
    equipped_leggings_id:       str | None = None
    equipped_boots_id:          str | None = None


@dataclass
class Mementos:
    memento1: str | None = None
    memento2: str | None = None
    memento3: str | None = None
    memento4: str | None = None


@dataclass
class PlayerSaveData:
    name:   str
    level:  int = 1
    xp:     int = 0
    gold:   int = 0
    zone:   str = "zone1"

    inventory: list[InventoryItem] = field(default_factory=list)
    equipment: Equipment = field(default_factory=Equipment)

    # SKILLS
    combat:     Combat = field(default_factory=Combat)
    mining:     Mining = field(default_factory=Mining)
    foraging:   Foraging = field(default_factory=Foraging)
    fishing:    Fishing = field(default_factory=Fishing)
    farming:    Farming = field(default_factory=Farming)