from .factory import Factory

from characters.character import Character

class Arena():
    
    def __init__(self):
        factory = Factory()
        self.player_run = 0
        self.opponent = None 
    
    def player_run(self):
        """method to allow the player to flee the fight with 
        (low chance of succeeding) """
        self.player_run = randint(1,100)
        if  1<= self.player_run <=7 :
            print("vous fuyez le combat ")
            
        else :
            print("votre adversaire vous a rattrappé le combat continue")
    
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
    
    """def attacking(self, player, opponent):
        method to attacking the opponent
        
        self.fighters(player, opponent)
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
    """
    def fighters(self,player, opponent):
        self.player = player
        self.opponent = opponent
        
        
    

    
    