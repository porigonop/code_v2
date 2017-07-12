from CarteDestination import CarteDestination
import random
class PiocheCarteDestination:
    def __init__(self, lst_dest):
        self.pioche = lst_dest
        
    def shuffle(self):
        random.shuffle(self.pioche)
    
    def pick(self):
        return self.pioche.pop()
    
    def __repr__(self):
        return str(self.pioche)
