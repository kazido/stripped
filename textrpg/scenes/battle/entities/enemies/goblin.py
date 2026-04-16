from .enemy import Enemy
from textrpg.scenes.battle.util import DamageSource

class Goblin(Enemy):
    NAME = "Goblin"
    HEALTH = 10
    SPEED = 8
    DAMAGE = 3

    def __init__(self, battle) -> None:
        super().__init__(battle)
        self.target = None

    def on_scene_start(self) -> None:
        self.target = max(self.scene.players, key=lambda p: p.account.gold)
        self.scene.handler.output(f"The goblin is targeting {self.target}...")

    def on_turn(self) -> None:
        # Goblins always attack the player with the most gold.
        self.target = max(self.scene.players, key=lambda p: p.account.gold)
        self.target.combat.take_damage(DamageSource.GENERIC, self.DAMAGE)