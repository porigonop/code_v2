from PyQt5.QtCore import QPoint 
class Target():
    """
    Define the rocket target
    """
    def __init__(self, posx, posy, radius = 10):
        self.posx = posx
        self.posy = posy
        self.radius = radius
    def move(self, posx, posy):
        """
        move the target to a new position
        """
        self.posx = posx
        self.posy = posy
    def draw(self, qp):
        """
        Draw the target to the designated position
        """
        qp.drawEllipse(QPoint(self.posx, self.posy), self.radius, self.radius)


