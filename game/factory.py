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
        self.ennemy = None
    
    def choose_class(self):
        """method to ask the user his class he wants play """
        print ("Voici les nom des personnages que vous pouvez incarner Le Magicien, L'archer ou le Guerrier")       
        while self.choice_class not in ["warrior", "magician", "archer"]:
            print (" Veuillez entrer les bon elements")
            self.choice_class = input(" Veuillez choisir le type de personnage que vous souhaiter incarner :").lower()
        if self.choice_class == "warrior":
            self.choice_class = Warrior()
        elif self.choice_class == "magician":
            self.choice_class = Magician()
        else :
            self.choice_class = Archer()
    

    def choose_enemy(self):
        """method for randomly choosing an enemy """
        self.ennemy=random.choice(["wolf", "zombie", "orc"])
        if self.ennemy == "wolf":
            self.ennemy = Wolf("Fally")
        elif self.ennemy == "zombie":
            self.ennemy = Zombie("Farid")
        else :
            self.ennemy = Orc("Sofiane")
        
