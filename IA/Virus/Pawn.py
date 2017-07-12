"""
describe the pawn
"""

class Pawn:
    """
    define the Pawn object
    """
    color_name = {}
    lst_of_name = [".", "x", "o", "+", "*"]
    iteration = 0
    def __init__(self, color):
        """
        constructor of the pawn
        """
        self.color = color
        self.last_pawn = []
        if self.color not in Pawn.color_name:
            Pawn.color_name[color] = Pawn.lst_of_name[Pawn.iteration]
            Pawn.iteration += 1
    def change_color(self, color):
        """
        allow the user to change the color of the pawn
        """
        self.last_pawn.append(self.color)
        self.color = color
    def cancel(self):
        """
        allow user to cancel a move
        """
        #
        # print(self.last_pawn)
        if self.last_pawn == []:
            return
        self.color = self.last_pawn.pop()
    def __repr__(self):
        if self.color is None:
            return "."
        elif self.color == "rouge":
            return "x"
        else:
            return "o"
