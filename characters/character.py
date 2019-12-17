class Character:
    
    def __init__(self, health, attack, defense, agility, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.name = None


    def choose_class(self):
        print ("Voici les nom des personnages que vous pouvez incarner Le Magicien, L'archer ou le Guerrier")
        self.choice_class = ""
        while self.choice_class not in ["warrior", "magician", "archer"]:
            print (" Veuillez entrer les bon elements")
            self.choice_class = imput(" Veuillez choisir le type de personnage que vous souhaiter incarner :")
        return self.choice_class

    def name(self):
        while self.name == None :
            self.name = input("veuillez entrez votre nom ou pseudo :")
        return self.name

