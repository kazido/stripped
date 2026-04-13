from textrpg.entities.enemies.enemy import Enemy
from textrpg.events.io import handler
from textrpg.events.event import ActionPerformedEvent



class Goblin(Enemy):
    NAME = "Goblin"
    BASE_HP = 10
    BASE_SPEED = 8
    DAMAGE = 3

    def pre_battle(self, players) -> None:
        richest = max(players, key=lambda p: p.gold)
        handler().output_event(ActionPerformedEvent(self, f"is eyeing {richest}..."))

    def take_turn(self, players) -> None:
        # Goblins always attack the player with the most gold.
        richest = max(players, key=lambda p: p.gold)
        richest.take_damage(self)



class Centaur(Enemy):
    NAME = "Centaur"
    BASE_HP = 50
    BASE_SPEED = 25
    DAMAGE = 15

    def take_turn(self, players) -> None:
        pass



class UnstableDrone(Enemy):
    """After three turns, the Mazhinx will self-destruct."""
    NAME = "Unstable Drone"
    BASE_HP = 100
    BASE_SPEED = 1
    DAMAGE = 100

    def __init__(self) -> None:
        super().__init__()
        self.turns_to_destruct: int = 3

    def take_turn(self, players) -> None:
        self.turns_to_destruct -= 1
        if self.turns_to_destruct <= 0:
            for player in players:
                player.take_damage(self)