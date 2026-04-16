from textrpg.core.player import Player
from textrpg.scenes.battle.battle import Battle
from textrpg.scenes.battle.entities.enemies import Goblin, Centaur, UnstableDrone

from textrpg.core.player.save_data import PlayerSaveData
from textrpg.io import TerminalIOHandler


def run_battle_test():

    battle = Battle(TerminalIOHandler())
    battle.set_enemies([Goblin(battle)])
    battle.set_players([Player(battle, PlayerSaveData("Bry"))])

    battle.run()

if __name__ == "__main__":
    run_battle_test()