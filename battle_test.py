from textrpg.events.battle import Battle
from textrpg.player.player import Player
from textrpg.entities.enemies.enemy import Goblin, Centaur, UnstableDrone
from textrpg.events.handlers import TerminalIOHandler
from textrpg.events.io import set_handler

from textrpg.player.save_data import PlayerSaveData


def run_battle_test():
    # Set up global handler
    handler = TerminalIOHandler()
    set_handler(handler)

    bry_data = PlayerSaveData("Bry")
    bry = Player(bry_data)

    jim_data = PlayerSaveData("Jim")
    jim_data.gold = 500
    jim = Player(jim_data)
    jim.current_hp = 500

    battle = Battle(handler)
    battle.set_enemies([UnstableDrone()])
    battle.set_players([bry, jim])

    battle.run()

    # Test level up
    bry.gain_skill_xp("combat", 1000)
    print("Done.")


if __name__ == "__main__":
    run_battle_test()