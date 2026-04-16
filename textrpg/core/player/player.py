from __future__ import annotations

from textrpg.core.player.save_data import PlayerSaveData
from textrpg.core.scene import Scene
from textrpg.core.entity import Entity
from .components import CombatComponent



class Player(Entity):
    def __init__(self, scene: Scene, account: PlayerSaveData) -> None:
        super().__init__(scene)
        # Load our player's data from the database once
        self.account = account
        self.combat = CombatComponent(self)
    
    def __str__(self) -> str:
        return f"{self.account.name}"