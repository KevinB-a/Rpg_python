import os 

from random import randint

class Character:
    
    def __init__(self, health, attack, defense, agility, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.name = None


    def choose_class(self):
        """method to ask the user his class he wants play """
        print ("Voici les nom des personnages que vous pouvez incarner Le Magicien, L'archer ou le Guerrier")
        self.choice_class = ""
        while self.choice_class not in ["warrior", "magician", "archer"]:
            print (" Veuillez entrer les bon elements")
            self.choice_class = input(" Veuillez choisir le type de personnage que vous souhaiter incarner :")
        return self.choice_class

    def player_name(self):
        """method to ask the user his name""" 
        while self.name == None :
            self.name = input("veuillez entrez votre nom ou pseudo :")
        return self.name

    def attacking(self):
        """method to attacking """
        if self.defense > self.attack :
            self.defense = self.defense -self.attack
        return self.defense

        if self.defense < self.attack and self.defense > 0 :
            self.attack -= self.defense
            self.health -= self.attack
            self.defense == 0
        return self.health
        
        if self.defense == 0 :
            self.health -= self.attack
        return self.health 
    
    def clear(self):
        """method to clear the terminal"""
        os.system('cls' if os.name =='nt' else 'clear')

    def dodge(self):
        if self.agility == 5 or self.agility == 10:
            n = randint (1, 100)
            if n == 1:
                self.attack = 0
        if self.agility == 20 or self.agility == 25:
            n = randint (1, 100)
            if 1 <= n <= 2:
                self.attack = 0
        if self.agility == 40 or self.agility == 50:
            n = randint (1, 100)
            if 1 <= n <= 5:
                self.attack = 0

    
    
