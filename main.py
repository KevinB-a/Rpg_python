from characters.character import Character

from characters.archer import Archer

from characters.warrior import Warrior

from characters.magician import Magician

from game.narrator import Narrator

from characters.character import Character

if __name__ == "__main__":

    # narrator = Narrator()
    # narrator.story_1()
    # narrator.clear()
    # character = Character(600, 20, 50, 25, None )
    # character.choose_class()
    # character.player_name()
    # character.__repr__()
    character = Character()
    character.choose_enemy()
    print(character.choose.enemy)
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

    

