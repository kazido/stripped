from .enemy import Enemy
from textrpg.scenes.battle.util import DamageSource

class UnstableDrone(Enemy):
    NAME = "Unstable Drone"
    HEALTH = 100
    SPEED = 1
    DAMAGE = 100

    def __init__(self, battle) -> None:
        super().__init__(battle)
        self.turns_to_destruct = 3

    def pre_battle(self) -> None:
        self.scene.handler.output(f"{self.NAME} is planning something devious in {self.turns_to_destruct} turns.")

    def take_turn(self) -> None:
        self.turns_to_destruct -= 1
        self.scene.handler.output(f"{self.turns_to_destruct}...")
        if self.turns_to_destruct <= 0:
            for player in self.scene.players:
                player.combat.take_damage(DamageSource.GENERIC, self.DAMAGE)