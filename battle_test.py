from textrpg.scenes.battle.battle import Battle
from textrpg.entities.player import Player
from textrpg.entities.enemies import Goblin, Centaur, UnstableDrone

from textrpg.entities.player.save_data import PlayerSaveData


def run_battle_test():
    battle = Battle(TerminalIOHandler())
    battle.set_enemies([Centaur(battle)])
    battle.set_players([Player(battle, PlayerSaveData("Bry"))])

    battle.run()

if __name__ == "__main__":
    run_battle_test()