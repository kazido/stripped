from textrpg.core.io import IOHandler
from textrpg.core.event import Event, MessageEvent, LevelUpEvent, DamageDealtEvent, EntityDeathEvent, TurnStartedEvent, ActionPerformedEvent
from textrpg.core.action import Action
from textrpg.scenes.battle.entities.enemies.enemy import Enemy

class TextualIOHandler(IOHandler):
    """Stub for Textual-based IOHandler. TODO: Implement with Textual widgets."""

    def output(self, message: str) -> None:
        # TODO: Output to Textual UI
        pass

    def output_event(self, event: Event) -> None:
        # TODO: Render event in Textual UI with formatting/colors
        pass

    def select_action(self, options: list[Action]) -> Action:
        # TODO: Show action selection in Textual UI
        raise NotImplementedError

    def select_target(self, targets: list[Enemy]) -> Enemy:
        # TODO: Show target selection in Textual UI
        raise NotImplementedError