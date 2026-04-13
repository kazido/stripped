from abc import ABC
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from textrpg.player.player import Player
    from textrpg.entities.enemies.enemy import Enemy


class Event(ABC):
    """Base class for all game events that can be outputted."""
    pass


class MessageEvent(Event):
    """A simple text message event."""
    def __init__(self, message: str) -> None:
        self.message = message


class LevelUpEvent(Event):
    """Event fired when a player levels up."""
    def __init__(self, player: "Player", skill_name: str, new_level: int) -> None:
        self.player = player
        self.skill_name = skill_name
        self.new_level = new_level


class DamageDealtEvent(Event):
    """Event fired when damage is dealt."""
    def __init__(self, attacker: Any, target: Any, damage: int) -> None:
        self.attacker = attacker
        self.target = target
        self.damage = damage


class EntityDeathEvent(Event):
    """Event fired when an entity dies."""
    def __init__(self, entity: Any) -> None:
        self.entity = entity


class TurnStartedEvent(Event):
    """Event fired when an entity's turn starts."""
    def __init__(self, entity: Any) -> None:
        self.entity = entity


class ActionPerformedEvent(Event):
    """Event fired when an action is performed."""
    def __init__(self, entity: Any, action_description: str) -> None:
        self.entity = entity
        self.action_description = action_description