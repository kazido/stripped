from textrpg.core.action import Action
from textrpg.core.entity import Entity
from textrpg.core.scene import Scene


class Attack(Action):
    label = "Attack"

    def execute(self, actor: Entity, scene: Scene) -> None:
        raise NotImplementedError
        # Note: players should gain skill xp in the body of an Action's execute method