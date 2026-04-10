from typing import Callable

from game.entities.base import Entity
from game.entities.enemy import Enemy


class Goblin(Enemy):
    name = "Goblin"
    base_hp = 10
    base_speed = 8
    damage = 3

    def take_turn(self, targets: list[Entity], log: Callable[[str], None]) -> None:
        # Goblins always attack the player with the most gold.
        players = self.get_players(targets)
        richest = max(players, key=lambda p: p.gold)
        log(f"{self.name} is eyeing {richest.name}...")


class Centaur(Enemy):
    name = "Centaur"
    base_hp = 50
    base_speed = 25
    damage = 15

    def take_turn(self, targets: list[Entity], log: Callable[[str], None]) -> None:
        players = self.get_players(targets)


class UnstableDrone(Enemy):
    """After three turns, the Mazhinx will self-destruct"""
    name = "Unstable Drone"
    base_hp = 100
    base_speed = 1
    damage = 100

    def __init__(self) -> None:
        super().__init__()
        self.turns_to_destruct: int = 3

    def take_turn(self, targets: list[Entity], log: Callable[[str], None]) -> None:
        players = self.get_players(targets)
        self.turns_to_destruct -= 1
        if self.turns_to_destruct <= 0:
            for player in players:
                if player.take_damage(self.damage):
                    log(f"{str(player)} has died.")

