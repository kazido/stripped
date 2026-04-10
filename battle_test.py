from game.battles.battle import Battle
from game.entities.player import Player
from game.entities.enemies.enemies import Goblin, Centaur, UnstableDrone

from game.save.save_data import PlayerSaveData


def run_battle_test():

    bry_data = PlayerSaveData("Bry")
    bry = Player(bry_data)

    jim_data = PlayerSaveData("Jim")
    jim_data.gold = 500
    jim = Player(jim_data)

    battle = Battle(log_func=print)
    battle.enemies.extend((UnstableDrone(),))
    battle.players.extend((bry, jim))

    battle.process_turn()
    battle.process_turn()
    battle.process_turn()
    print()


if __name__ == "__main__":
    run_battle_test()