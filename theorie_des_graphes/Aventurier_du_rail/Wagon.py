#usr/bin/env python3
##############################################
# Authors: Antoine Lièvre et Lauren Vaitanaki#
# Last Modification: 01/25/2017              #
##############################################

class Wagon:
    """ Class to construct class Wagon """
    
    def __init__(self, color):
        """ Class constructor which has one attribute
            color : atttribute representing the color of a wagon """
        self.color = color

    def __repr__(self):
        """ method to have an easy visual representation"""
        return self.color
