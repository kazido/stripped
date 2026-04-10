from abc import ABC


class Item(ABC):
    item_id: str
    name: str
    description: str = "No description provided."
    value: int
    
    def __repr__(self):
        return f"<{getattr(self, 'name', 'Unknown')}> ({getattr(self, 'item_id', 'none')})"