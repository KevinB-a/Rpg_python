from characters.character import Character

from characters.archer import Archer

from characters.warrior import Warrior

from characters.magician import Magician

from characters.orc import Orc

from characters.wolf import Wolf

from characters.zombie import Zombie

import random
class Factory():
    """ """
    def __init__(self):
        self.choice_class = None
        self.opponent = None
    
    def choose_class(self):
        """method to ask the user his class he wants play """
        print ("Voici les nom des personnages que vous pouvez incarner Le Magicien, L'archer ou le Guerrier")       
        while self.choice_class not in ["warrior", "magician", "archer"]:
            print (" Veuillez entrer les bon elements")
            self.choice_class = input(" Veuillez choisir le type de personnage que vous souhaiter incarner :").lower()
        if self.choice_class == "warrior":
            warrior = Warrior()
            return warrior
        elif self.choice_class == "magician":
            magician = Magician()
            return magician
        else :
            archer = Archer()
            return archer

    def choose_enemy(self):
        """method for randomly choosing an enemy """
        self.opponent = random.choice(["wolf", "zombie", "orc"])
        if self.opponent == "wolf":
            wolf=Wolf("Fally")
            return wolf   
        elif self.opponent == "zombie":
            zombie = Zombie("Farid")
            return zombie 
        else :
            self.opponent == "orc"
            orc = Orc("Sofiane")
            return orc  
