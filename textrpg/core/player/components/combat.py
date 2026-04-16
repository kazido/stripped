from typing import TYPE_CHECKING

from textrpg.core.stats import Stat
from textrpg.scenes.battle.util import StatusEffect, Status, DamageSource
from textrpg.core.event import EntityDeathEvent
from textrpg.items import ITEM_REGISTRY
from textrpg.items.armor import Armor

if TYPE_CHECKING:
    from textrpg.core.player import Player

class CombatComponent:
    def __init__(self, player: Player) -> None:
        self.p = player
        self.p.data.register(Stat.HEALTH, 10)
        self.p.data.register(Stat.SPEED, 10)

    def _get_gear_hp_bonus(self) -> int:
        bonus = 0
        for item in self.p.account.inventory:
            item_class = ITEM_REGISTRY.get(item.item_id)
            if item_class and issubclass(item_class, Armor):
                bonus += item_class.hp_bonus
        return bonus

    def take_damage(self, source: DamageSource, amount: int) -> None:
        self.p.data.modify(Stat.HEALTH, -amount)
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
        return self.p.data.get(Stat.HEALTH) <= 0
    
    @property
    def can_act(self) -> bool:
        return Status.SILENCED not in self.status_effects
    
    @property
    def is_burning(self) -> bool:
        return any(e in self.status_effects for e in (Status.ON_FIRE, Status.ETERNAL_FIRE))