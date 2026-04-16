from abc import ABC, abstractmethod

from textrpg.core.scene import Scene
from textrpg.core.stats import StatManager


class Entity(ABC):
    def __init__(self, scene: Scene) -> None:
        self.scene = scene
        self.data = StatManager()

    def on_scene_start(self) -> None: pass
    def on_turn(self) -> None: pass
    def on_scene_end(self) -> None: pass

