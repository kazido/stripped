from textrpg.entities.player.player import Player
from textrpg.entities.enemy.enemy import Enemy
from textrpg.entities.entity import Entity
from textrpg.util.stat_manager import Stat
from textrpg.events.io import IOHandler


class Battle:
    def __init__(self, handler: IOHandler) -> None:
        self._players: list[Player] = []
        self._enemies: list[Enemy] = []
        self.handler = handler


    @property
    def players(self) -> list[Player]:
        # TODO: Change if a dead player can be targeted (revives)
        return [p for p in self._players if not p.is_dead]
    
    @property
    def enemies(self) -> list[Enemy]:
        # TODO: Change if a dead enemy can be targeted
        return [e for e in self._enemies if not e.is_dead]
    
    def set_players(self, players: list[Player]) -> None:
        self._players = players

    def set_enemies(self, enemies: list[Enemy]) -> None:
        self._enemies = enemies


    def run(self) -> None:
        # Run pre battle hooks
        self.pre_battle()

        # Process turns until all players or enemies are defeated
        while not (self.players_won() or self.enemies_won()):
            self.process_turns()

        # Run post battle hooks
        self.post_battle()


    def pre_battle(self) -> None:
        """Handles any actions that should happen before a battle."""
        self.handler.output("Battle start!")
        for entity in self.get_turn_order():
            entity.pre_battle()



    def process_turns(self) -> None:
        """Process a turn for each entity in the battle."""
        for entity in self.get_turn_order():
            entity.take_turn()



    def post_battle(self) -> None:
        """Handles any actions that should happen after a battle."""
        for entity in self.get_turn_order():
            entity.post_battle()

        self.handler.output("Battle has finished!")


    def get_turn_order(self) -> list[Entity]:
        """Returns a list of all entities sorted by their speed."""
        p = self.players + self.enemies
        return sorted(p, key=lambda e: e.data.get(Stat.SPEED), reverse=True)
    

    def players_won(self) -> bool:
        """Returns True if all enemies are dead."""
        return all(enemy.is_dead for enemy in self.enemies)
    
    def enemies_won(self) -> bool:
        """Returns True if all players are dead."""
        return all(player.is_dead for player in self.players)

