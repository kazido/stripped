from textrpg.entities.enemy.enemy import Enemy
from textrpg.events.battle import Battle
from textrpg.util.damage_source import DamageSource

class UnstableDrone(Enemy):
    NAME = "Unstable Drone"
    HEALTH = 100
    SPEED = 1
    DAMAGE = 100

    def __init__(self, battle: Battle) -> None:
        super().__init__(battle)
        self.turns_to_destruct = 3

    def pre_battle(self) -> None:
        self.battle_in.handler.output(f"{self.NAME} is planning something devious in {self.turns_to_destruct} turns.")

    def take_turn(self) -> None:
        self.turns_to_destruct -= 1
        self.battle_in.handler.output(f"{self.turns_to_destruct}...")
        if self.turns_to_destruct <= 0:
            for player in self.battle_in.players:
                player.take_damage(DamageSource.GENERIC, self.DAMAGE)