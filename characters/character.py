import os 

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
        
    
    
