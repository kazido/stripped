from abc import ABC, abstractmethod

from textrpg.scenes.battle.util.damage_source import DamageSource
from textrpg.scenes.battle.util.status_effect import Status, StatusEffect
from textrpg.scenes.battle.util.stat_manager import Stat, StatManager
from textrpg.core.event import EntityDeathEvent

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from textrpg.scenes.battle.battle import Battle

class Entity(ABC):
    def __init__(self, battle: Battle) -> None:
        self.battle_in = battle
        self.data = StatManager()
        self.status_effects: list[StatusEffect] = []

    @property
    def is_dead(self) -> bool:
        return self.data.get(Stat.HEALTH) <= 0
    
    @property
    def can_act(self) -> bool:
        return Status.SILENCED not in self.status_effects
    
    @property
    def is_burning(self) -> bool:
        return any(e in self.status_effects for e in (Status.ON_FIRE, Status.ETERNAL_FIRE))
    

    def take_turn(self) -> None:
        pass

    def pre_battle(self) -> None:
        pass

    def post_battle(self) -> None:
        pass
    
    
    def apply_status_effect(self, effect: Status):
        self.status_effects.append(StatusEffect(effect))

    def process_statuses(self):
        for s in self.status_effects:
            # TODO: Figure out a way to scale the damage of statuses
            if s is Status.ON_FIRE:
                self.take_damage(DamageSource.FIRE, 3)
            elif s is Status.ETERNAL_FIRE:
                self.take_damage(DamageSource.FIRE, 5)

            # Slowly remove all non-permanent status effects
            s.tick()

        # Rebuild the list of effects, removing any expired effects
        self.status_effects = [s for s in self.status_effects if not s.is_expired]

    def take_damage(self, source: DamageSource, amount: int):
        self.data.modify(Stat.HEALTH, -amount)
        if self.is_dead:
            self.battle_in.handler.output_event(EntityDeathEvent(self))
        if source.is_fire_damage:
            self.apply_status_effect(Status.ON_FIRE)
