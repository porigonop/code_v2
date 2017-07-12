from PyQt5.QtCore import QPoint 
class Target():
    """
    """
    def __init__(self, posx, posy, radius = 10):
        self.posx = posx
        self.posy = posy
        self.radius = radius
    def move(self, posx, posy):
        """
        """
        self.posx = posx
        self.posy = posy
    def draw(self, qp):
        qp.drawEllipse(QPoint(self.posx, self.posy), self.radius, self.radius)


