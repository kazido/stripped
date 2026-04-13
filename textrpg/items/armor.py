from .base import Item
from abc import ABC

class Armor(Item, ABC):
    hp_bonus: int = 0
    

class LeatherBoots(Armor):
    item_id = "leather_boots"
    name = "Leather Boots"
    description = "An old pair of leather boots. They're a little scuffed, but they look good."
    hp_bonus = 5