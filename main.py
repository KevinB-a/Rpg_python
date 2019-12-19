from characters.character import Character

from characters.archer import Archer

from characters.warrior import Warrior

from characters.magician import Magician

from game.factory import Factory

from game.arena import Arena

if __name__ == "__main__":

    character = Warrior()
    factory=Factory()
    player=factory.choose_class()
    character.player_name()
    character.__repr__()
    opponent=factory.choose_enemy()
    arena = Arena()
    arena.attacking(player, opponent)

