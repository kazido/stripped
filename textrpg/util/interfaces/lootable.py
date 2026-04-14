from abc import ABC, abstractmethod
from textrpg.items.base import Item


class LootTable:
    def add_item(self, item: Item, probability: float):
        pass


class Lootable(ABC):

    @property
    @abstractmethod
    def loot_table(self) -> LootTable:
        pass