from abc import ABC, abstractmethod

from textrpg.util.damage_source import DamageSource
from textrpg.util.status_effect import StatusEffect

class Entity(ABC):
    def __init__(self) -> None:
        self.health: int = 0
        self.status_effects: list[StatusEffect] = []

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def is_dead(self) -> bool:
        return self.health <= 0
    
    @property
    def can_act(self) -> bool:
        return StatusEffect.SILENCED not in self.status_effects
    
    def apply_status(self, effect: StatusEffect):
        self.status_effects.append(effect)

    def process_statuses(self):
        for status in self.status_effects:
            # TODO: Figure out a way to scale the damage of statuses
            if status is StatusEffect.ON_FIRE:
                self.take_damage(DamageSource.FIRE, 3)
            elif status is StatusEffect.ETERNAL_FIRE:
                self.take_damage(DamageSource.FIRE, 5)

            # Slowly remove all non-permanent status effects
            if not status.is_permanent:
                status.turns_left -= 1

        # Rebuild the list of effects, removing any expired effects
        self.status_effects = [s for s in self.status_effects if not s.is_expired]

    def take_damage(self, source: DamageSource, amount: int):
        self.health -= amount
        if source.is_fire_damage:
            self.apply_status(StatusEffect.ON_FIRE)
