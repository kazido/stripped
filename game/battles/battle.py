from typing import Callable
from ..entities.player import Player
from ..entities.enemy import Enemy


class Battle:
    def __init__(self, log_func: Callable[[str], None]) -> None:
        self.players: list[Player] = []
        self.enemies: list[Enemy] = []
        self.log = log_func


    def pre_battle(self) -> None:
        """Handles any actions that should happen before a battle."""
        pass


    def process_turn(self) -> None:
        """Process a turn for each entity in the battle."""
        for entity in self.get_turn_order():
            self.log(f"It's {entity}'s turn.")
            if isinstance(entity, Player):
                entity.take_turn(self.enemies, self.log)
            elif isinstance(entity, Enemy):
                entity.take_turn(self.enemies, self.log)



    def post_battle(self) -> None:
        """Handles any actions that should happen after a battle."""
        pass


    def get_turn_order(self) -> list[Player | Enemy]:
        """Returns a list of all entities sorted by their speed."""
        p = self.players + self.enemies
        return sorted(p, key=lambda e: e.speed, reverse=True)
    

    def players_won(self) -> bool:
        """Returns True if all enemies are dead."""
        return all(enemy.is_dead for enemy in self.enemies)

