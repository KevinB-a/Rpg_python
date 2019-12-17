class Character:
    
    def __init__(self, health, attack, defense, agility, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.name = None


    def name ():
        print ("Voici les nom des personnages que vous pouvez incarner Le Magicien, L'archer ou le Guerrier")
        userName = imput(" Veuillez choisir le type de personnage que vous souhaiter incarner ")
        while checkName (userName)is False:
            print (" Veuillez entrer les bon elements")
            userName = imput(" Veuillez choisir le type de personnage que vous souhaiter incarner ")
        retur userName

    def chekName ():
        
    
