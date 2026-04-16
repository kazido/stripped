from abc import ABC, abstractmethod

from textrpg.core.entity import Entity
from textrpg.core.stats import Stat
from textrpg.scenes.battle.util import StatusEffect, Status, DamageSource

from textrpg.core.event import EntityDeathEvent

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from textrpg.scenes.battle.battle import Battle


class CombatEntity(Entity, ABC):
    scene: Battle

    def __init__(self, scene: Battle) -> None:
        super().__init__(scene)
        self.status_effects: list[StatusEffect] = []

    def take_damage(self, source: DamageSource, amount: int) -> None:
        self.data.modify(Stat.HEALTH, -amount)
        if self.is_dead:
            self.scene.handler.output_event(EntityDeathEvent(self))
        if source.is_fire_damage:
            self.apply_status_effect(Status.ON_FIRE)
    
    def apply_status_effect(self, effect: Status) -> None:
        self.status_effects.append(StatusEffect(effect))

    def process_statuses(self) -> None:
        for se in self.status_effects:
            # TODO: Figure out a way to scale the damage of statuses
            s = se.status
            if s is Status.ON_FIRE:
                self.take_damage(DamageSource.FIRE, 3)
            elif s is Status.ETERNAL_FIRE:
                self.take_damage(DamageSource.FIRE, 5)

            # Slowly remove all non-permanent status effects
            se.tick()

        # Rebuild the list of effects, removing any expired effects
        self.status_effects = [s for s in self.status_effects if not s.is_expired]


    @property
    def is_dead(self) -> bool:
        return self.data.get(Stat.HEALTH) <= 0
    
    @property
    def can_act(self) -> bool:
        return Status.SILENCED not in self.status_effects
    
    @property
    def is_burning(self) -> bool:
        return any(e in self.status_effects for e in (Status.ON_FIRE, Status.ETERNAL_FIRE))

