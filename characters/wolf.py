from .character import Character

class Wolf(Character) :
    """this class inherit from Character we define his attributes  """
    def __init__(self,name) :
        """ """
        super().__init__(400,40,15,20, None)
    