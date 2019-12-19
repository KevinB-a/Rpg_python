from characters.character import Character

from characters.archer import Archer

from characters.warrior import Warrior

from characters.magician import Magician

if __name__ == "__main__":

    character = Character(None, None, None, None, None )
    value=character.choose_class()
    if value == "warrior" :
        warrior = Warrior()
    elif value == "magician" :
        magician=Magician()
    else :
        archer = Archer()
    
    character.player_name()
    character.__repr__()
    

