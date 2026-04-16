from abc import ABC, abstractmethod

from textrpg.core.io import IOHandler

class Scene(ABC):
    """Any interactive game scene: battle, mining node, fishing spot, etc."""
    def __init__(self, handler: IOHandler) -> None:
        self.handler = handler

    @abstractmethod
    def run(self) -> None:
        pass