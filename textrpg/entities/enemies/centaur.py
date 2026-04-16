from textrpg.entities.enemy.enemy import Enemy

class Centaur(Enemy):
    NAME = "Centaur"
    HEALTH = 50
    SPEED = 25
    DAMAGE = 15

    def take_turn(self) -> None:
        pass