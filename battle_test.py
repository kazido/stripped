from textrpg.events.battle import Battle
from textrpg.entities.player.player import Player
from textrpg.entities.enemy.goblin import Goblin
from textrpg.entities.enemy.centaur import Centaur
from textrpg.entities.enemy.unstable_drone import UnstableDrone
from textrpg.events.handlers import TerminalIOHandler

from textrpg.entities.player.save_data import PlayerSaveData


def run_battle_test():
    battle = Battle(TerminalIOHandler())
    battle.set_enemies([Centaur(battle)])
    battle.set_players([Player(battle, PlayerSaveData("Bry"))])

    battle.run()

if __name__ == "__main__":
    run_battle_test()