#!usr/bin/env python3
######################################
#Authors: A. LIEVRE et L. VAITANAKI  #
#Last Modification: 01/25/2017       #
######################################

from pprint import pprint
from CarteWagon import CarteWagon
import random
COLOR = ["Bleu", "Rose", "Orange", "Blanc",\
 "Vert", "Jaune", "Noir", "Rouge", "multicolor"]


class PiocheCarteWagon:
    """ Class to model a stack of Wagon Card"""
    def __init__(self):
        """ Class constructor to initiate the following attributes:
        pioche: attribute for modeling a stack of wagon cards
        defausse : attribute representing a discard
        """
        self.pioche = [CarteWagon(COLOR[i]) \
                        for i in range(len(COLOR)-1)\
                        for j in range(22)]+\
                        [CarteWagon(COLOR[-1]) for i in range(14)]

        self.defaus = []
        
        
    def shuffle(self):
        """ method to mix up the stack """
        random.shuffle(self.pioche)
    
    def pick(self):
        """ method to draw a card"""
        return self.pioche.pop()
    
    def defausse(self, carte):
        """ method to discard"""
        self.defaus.append(carte)
    
    def __repr__(self):
        """ method that allows to print the object """
        return str(self.pioche)
    
if __name__ == "__main__":
    P = PiocheCarteWagon()
    P.shuffle()
    print(P.pick())
    
    salut = [i for i in range(10)]
    print(salut)
    print(salut.pop())
    print(salut)
