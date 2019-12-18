from characters.character import Character

from characters.archer import Archer

from characters.warrior import Warrior

from characters.magician import Magician

if __name__ == "__main__":

    character = Character(600, 20, 50, 25, None )
    character.choose_class()
    character.player_name()
    character.__repr__()
    

