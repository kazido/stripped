from textrpg.entities.enemy.enemy import Enemy
from textrpg.events.battle import Battle
from textrpg.util.damage_source import DamageSource

class Goblin(Enemy):
    NAME = "Goblin"
    HEALTH = 10
    SPEED = 8
    DAMAGE = 3

    def __init__(self, battle: Battle) -> None:
        super().__init__(battle)
        self.target = None


    def pre_battle(self) -> None:
        self.target = max(self.battle_in.players, key=lambda p: p.account.gold)
        self.battle_in.handler.output(f"The goblin is targeting {self.target}...")

    def take_turn(self) -> None:
        # Goblins always attack the player with the most gold.
        self.target = max(self.battle_in.players, key=lambda p: p.account.gold)
        self.target.take_damage(DamageSource.GENERIC, self.DAMAGE)