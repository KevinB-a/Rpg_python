from .factory import Factory

from characters.character import Character

class Arena():
    """this class contains 5 methods
       -character_run()
       -dodge()
       -fighters()
       -player_attacking()
       -opponent_attacking()"""
    
    def __init__(self):
       """initialize arguments  """
        factory = Factory()
        self.character_run = 0
        self.opponent = None 
    
    def character_run(self):
        """method to allow the character to flee the fight with 
        (low chance of succeeding) """
        self.character_run = randint(1,100)
        if  1<= self.character_run <=7 :
            print("vous fuyez le combat ")
            return True
            
        else :
            print("votre adversaire vous a rattrappé le combat continue")
    
    def dodge(self,opponent):
        """methods to dodge in function of agility character """
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
    

    def fighters(self, player, opponent):
        """method for have two fighters """
        self.player = player
        self.opponent = opponent
    
            
    def player_attacking(self, player, opponent):
        """player attack method"""
        if opponent.health >0 :
            if player.attack < opponent.defense:
                hit=(player.attack/opponent.defense)*player.attack
                opponent.health -=hit
                print("l'adversaire possede encore",opponent.health,"points de vie")
            else :
                opponent.health -= player.attack
                print("l'adversaire possede encore",opponent.health,"points de vie")

        else :
            opponent.health ==0 


            
    def opponent_attacking(self, opponent, player):
        """opponent attack method """
        if player.health >0 :
            if opponent.attack < player.defense:
                hit=(opponent.attack/player.defense)*opponent.attack
                player.health -=hit
                print("le joueur possede encore",player.health,"points de vie")
            else :
                player.health -= opponent.attack
                print("le joueur possede encore",player.health,"points de vie")
        else :
            player.health ==0 

    
    