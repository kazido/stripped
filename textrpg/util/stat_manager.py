from enum import Enum, auto

class Stat(Enum):
    HEALTH = auto()
    SPEED = auto()


class StatManager:
    def __init__(self) -> None:
        self._stats: dict[Stat, int] = {}

    def register(self, stat: Stat, default: int):
        """Add a new stat to the manager."""
        self._stats[stat] = default

    def update(self, stat: Stat, value: int):
        """Update an existing stat to a value. Will fail if stat has not been registered already."""
        if stat not in self._stats:
            raise KeyError(f"{stat} is not registered.")
        self._stats[stat] = value

    def modify(self, stat: Stat, delta: int):
        """Modify an existing stat by delta. Will fail if stat has not been registered already."""
        if stat not in self._stats:
            raise KeyError(f"{stat} is not registered.")
        self._stats[stat] += delta

    def get(self, stat: Stat) -> int:
        """Get an existing stat. Will fail if stat has not been registered already."""
        if stat not in self._stats:
            raise KeyError(f"{stat} is not registered.")
        else:
            return self._stats[stat]