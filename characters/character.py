import os 

from random import randint

class Character():
    """this class is mother class,  """
    def __init__(self, health, attack, defense, agility, name):
        """arguments for initialize the Character class  """
        self.health = health
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.name = None

    def character_name(self):
        """method to ask the user his name""" 
        while self.name == None :
            self.name = input("veuillez entrez votre nom ou pseudo :")
        return self.name
    
    def clear(self):
        """method to clear the terminal"""
        os.system('cls' if os.name =='nt' else 'clear')

    def __repr__(self):
        """method to show employee informations"""
        text=" {}'s informations \n\
        health : {} \n\
        attack : {} \n\
        defense : {} \n\
        agility : {} \n"
        print(text.format(self.name, self.health, self.attack, self.defense, self.agility))
    
    
         