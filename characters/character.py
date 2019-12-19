import os 

from random import randint

class Character():
    
    def __init__(self, health, attack, defense, agility, name):
        """arguments for initialize the Character class  """
        self.health = health
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.name = None

    def player_name(self):
        """method to ask the user his name""" 
        while self.name == None :
            self.name = input("veuillez entrez votre nom ou pseudo :")
        return self.name

    def attacking(self,opponent):
        """method to attacking the opponent"""
        if self.opponent.defense > self.attack :
            self.opponent.defense -= self.attack
        return self.opponent.defense

        if self.opponent.defense < self.attack and self.defense > 0 :
            self.attack -= self.opponent.defense
            self.opponent.health -= self.attack
            self.opponent.defense == 0
        return self.opponent.health
        
        if self.opponent.defense == 0 :
            self.opponent.health -= self.attack
        return self.opponent.health 
    
    def clear(self):
        """method to clear the terminal"""
        os.system('cls' if os.name =='nt' else 'clear')

    def dodge(self,opponent):
        """methods to dodge in function of agility player """
        if self.agility == 5 :
            n = randint (1, 200)
            if n == 1:
                self.opponent.attack = 0
        
        if self.agility == 10:
            n = randint (1, 100)
            if n == 1:
                self.opponent.attack = 0
        
        
        if self.agility == 20 :
            n = randint (1, 100)
            if 1 <= n <= 2:
                self.opponent.attack = 0
        
            
        if self.agility == 25:
            n = randint (1, 200)
            if 1 <= n <= 5:
                self.opponent.attack = 0
        
        
        if self.agility == 40 :
            n = randint (1, 100)
            if 1 <= n <= 4:
                self.opponent.attack = 0
        
        
        if  self.agility == 50:
            n = randint (1, 100)
            if 1 <= n <= 5:
                self.opponent.attack = 0
        

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
            
         