from .factory import Factory

from characters.character import Character

class Arena():
    
    def __init__(self):
        factory = Factory()
        self.character_run = 0
        self.opponent = None 
    
    def character_run(self):
        """method to allow the character to flee the fight with 
        (low chance of succeeding) """
        self.character_run = randint(1,100)
        if  1<= self.character_run <=7 :
            print("vous fuyez le combat ")
            
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
    
    """def attacking(self, character, opponent):
        method to attacking the opponent
        
        self.fighters(character, opponent)
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
    def fighters(self, player, opponent):
        """method for create  """
        self.player = player
        self.opponent = opponent
    
    """def attacking(self, player, opponent):
        self.fighters(player, opponent)
        if opponent.defense > 0:
            if opponent.defense < player.attack:
                opponent.health -= (player.attack - opponent.defense)
                opponent.defense = 0
            else:
                opponent.defense -= player.attack
                print(opponent.defense)
        else:
            if opponent.defense == 0:
                opponent.health -= player.attack
                if opponent.health <= 0:
                    opponent.health = 0
            else:
                opponent.health -= (player.attack - opponent.defense)
            return(opponent.health)"""
            
    def player_attacking(self, player, opponent):
        if opponent.health >0 :
            if player.attack < opponent.defense:
                hit=(player.attack/opponent.defense)*player.attack
                opponent.health -=hit
                print("l'adversaire possede encore ",opponent.health)
            else :
                opponent.health -= player.attack
                print("l'adversaire possede encore ",opponent.health)

        else :
            opponent.health ==0 


            
    def opponent_attacking(self, opponent, player):
        if player.health >0 :
            if opponent.attack < player.defense:
                hit=(opponent.attack/player.defense)*opponent.attack
                player.health -=hit
                print("le joueur possede encore ",player.health)
            else :
                player.health -= opponent.attack
                print("le joueur possede encore ",player.health)
        else :
            player.health ==0 

    
    