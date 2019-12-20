from .character import Character

class Magician(Character):
    """this class has a constructor init, a method call healing and a class attribute mana """
    mana = 200
    def __init__(self):
        super().__init__(600,20,50,25, None)
    
    def healing(self):
        """method to recover health points """
        if 0 < self.health <= 600 :
            self.heath += 30
            Magician.mana -= 50
            return self.heath                
        
        elif Magician.mana < 50 :
            print("votre mana est trop basse pour utiliser le sort de soin")

        else :
            print("vous vous soigniez mais votre health est au maximum ")
            Magician.mana -=50 
            self.health == self.health
            return self.health

