from .enemy import Enemy
from textrpg.scenes.battle.util import DamageSource

class Centaur(Enemy):
    NAME = "Centaur"
    HEALTH = 50
    SPEED = 25
    DAMAGE = 15

    def take_turn(self) -> None:
        pass