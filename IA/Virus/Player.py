"""
contain Player object
"""

class Player(object):
    """
    Takes 2 arguments :
        The name of the player
        The color he chooses
    It defines two methods :
        get_adversary()
        set_adversary()
    """
    def __init__(self, player_name, player_color):
        """ Is the constructor of the class player"""
        self.adversary = None
        self.name = player_name
        self.color = player_color

    def get_adversary(self):
        """ Returns the adversary of the player """
        return self.adversary

    def set_adversary(self, adversary):
        """ Returns the adversary entered by the player"""
        if self.adversary is None:
            self.adversary = adversary

    def play(self, grid):
        """ Takes the inputs of the player and makes him play"""
        while True:
            pos = input("What is the position " + self.name + " want to conquer : ")
            pos = pos.split(" ")
            try:
                pos_x = int(pos[0])
                pos_y = int(pos[1])
            except ValueError:
                print('you must type "x y" where x and y is the pos you want to play')
                continue
            if (pos_x, pos_y) in grid.get_empty_square():
                return (pos_x, pos_y)

    def __repr__(self):
        return self.name
            