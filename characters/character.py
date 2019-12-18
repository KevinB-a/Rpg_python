import os 

from random import randint

class Character:
    
    def __init__(self, health, attack, defense, agility, name):
        """arguments for initialize the Character class  """
        self.health = health
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.name = None
        self.computer_choose = None

    def choose_class(self):
        """method to ask the user his class he wants play """
        print ("Voici les nom des personnages que vous pouvez incarner warrior, archer ou magician")
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
        """methods to dodge in function of agility player """
        if self.agility == 5 :
            n = randint (1, 200)
            if n == 1:
                self.attack = 0
        
        if self.agility == 10:
            n = randint (1, 100)
            if n == 1:
                self.attack = 0
        
        if self.agility == 20 :
            n = randint (1, 100)
            if 1 <= n <= 2:
                self.attack = 0
            
        if self.agility == 25:
            n = randint (1, 200)
            if 1 <= n <= 5:
                self.attack = 0
        
        if self.agility == 40 :
            n = randint (1, 100)
            if 1 <= n <= 4:
                self.attack = 0
        
        if  self.agility == 50:
            n = randint (1, 100)
            if 1 <= n <= 5:
                self.attack = 0

    def __repr__(self):
        """method to show employee informations"""
        text=" {}'s informations \n\
        health : {} \n\
        attack : {} \n\
        defense : {} \n\
        agility : {} \n"
        print(text.format(self.name, self.health, self.attack, self.defense, self.agility))
    
    def player_run(self):
        """method to allow the player to flee the fight with 
        (low chance of succeeding) """
        self.player_run = randint(1,100)
        if  1<= self.player_run <=7 :
            print("vous fuyez le combat ")
            
        else :
            print("votre adversaire vous a rattrappé le combat continue")

    def choose_enemy(self):
        self.computer_choose = ["wolf", "zombie", "orc"]
        return self.computer_choose[randint(self.computer_choose)]

            
         