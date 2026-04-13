import time

from textrpg.events.io import IOHandler
from textrpg.events.event import Event, MessageEvent, LevelUpEvent, DamageDealtEvent, EntityDeathEvent, TurnStartedEvent, ActionPerformedEvent
from textrpg.events.action import Action
from textrpg.entities.enemies.enemy import Enemy


class TerminalIOHandler(IOHandler):
    """Terminal-based IOHandler for testing. Prints events to console."""

    def output(self, message: str) -> None:
        print(message)
        time.sleep(0.5)

    def output_event(self, event: Event) -> None:
        if isinstance(event, MessageEvent):
            print(event.message)
        elif isinstance(event, LevelUpEvent):
            print(f"{event.player} leveled up {event.skill_name} to level {event.new_level}!")
        elif isinstance(event, DamageDealtEvent):
            print(f"{event.attacker} dealt {event.damage} damage to {event.target}!")
        elif isinstance(event, EntityDeathEvent):
            print(f"{event.entity} has died!")
        elif isinstance(event, TurnStartedEvent):
            print(f"It's {event.entity}'s turn.")
        elif isinstance(event, ActionPerformedEvent):
            print(f"{event.entity} {event.action_description}")
        else:
            print(f"Unknown event: {event}")
        time.sleep(0.5)
        

    def select_action(self, options: list[Action]) -> Action:
        for i, action in enumerate(options):
            print(f"{i+1}. {action}")
        while True:
            try:
                choice = int(input("Choose an action: ")) - 1
                if 0 <= choice < len(options):
                    return options[choice]
            except ValueError:
                pass
            print("Invalid choice. Try again.")

    def select_target(self, targets: list[Enemy]) -> Enemy:
        for i, target in enumerate(targets):
            print(f"{i+1}. {target}")
        while True:
            try:
                choice = int(input("Choose a target: ")) - 1
                if 0 <= choice < len(targets):
                    return targets[choice]
            except ValueError:
                pass
            print("Invalid choice. Try again.")


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