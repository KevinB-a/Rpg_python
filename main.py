from characters.character import Character

from characters.archer import Archer

from characters.warrior import Warrior

from characters.magician import Magician

from game.factory import Factory

from game.arena import Arena

if __name__ == "__main__":

    character = Archer()
    factory=Factory()
    player=factory.choose_class()
    player.character_name()
    player.__repr__()
    opponent=factory.choose_enemy()
    opponent.__repr__()
    arena = Arena()
    while player.health > 0 and opponent.health > 0 :
        answer = input("quel action voulez vous effectuer attaquer ou fuir ? a pour attaquer f pour fuir")
        if answer == "a":
            arena.player_attacking(player, opponent)
            arena.opponent_attacking(opponent,player)
        if answer == "f":
            if arena.character_run() == True :
                break
            else :
                arena.opponent_attacking(opponent,player)
                continue
            
            
            
             