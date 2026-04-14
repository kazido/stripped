from ..entities.player.player import Player
from ..entities.enemies.enemy import Enemy
from textrpg.events.io import IOHandler, handler
from textrpg.events.event import TurnStartedEvent


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
        for entity in self.get_turn_order():
            if isinstance(entity, Player):
                entity.pre_battle(self.enemies)
            elif isinstance(entity, Enemy):
                entity.pre_battle(self.players)



    def process_turns(self) -> None:
        """Process a turn for each entity in the battle."""
        for entity in self.get_turn_order():
            handler().output_event(TurnStartedEvent(entity))
            if isinstance(entity, Player):
                entity.take_turn(self.enemies)
            elif isinstance(entity, Enemy):
                entity.take_turn(self.players)



    def post_battle(self) -> None:
        """Handles any actions that should happen after a battle."""
        for entity in self.get_turn_order():
            if isinstance(entity, Player):
                entity.post_battle(self.enemies)
            elif isinstance(entity, Enemy):
                entity.post_battle(self.players)


    def get_turn_order(self) -> list[Player | Enemy]:
        """Returns a list of all entities sorted by their speed."""
        p = self.players + self.enemies
        return sorted(p, key=lambda e: e.speed, reverse=True)
    

    def players_won(self) -> bool:
        """Returns True if all enemies are dead."""
        return all(enemy.is_dead for enemy in self.enemies)
    
    def enemies_won(self) -> bool:
        """Returns True if all players are dead."""
        return all(player.is_dead for player in self.players)

