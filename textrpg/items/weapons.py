from .base import Item
from abc import ABC

class Weapon(Item, ABC):
    base_damage: int = 0
    

class GunShapedStick(Weapon):
    item_id = "gun_shaped_stick"
    name = "Gun-Shaped Stick"
    description = "Perfect stick gun."
    base_damage = 5