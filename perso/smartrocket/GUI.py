from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsView
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer
from Constante import WIDTH, HEIGHT, FPS

class Fenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.sector = None
        self.pop = None
    def initUI(self):
        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.setWindowTitle('test')
        self.show()
        
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        pen = QPen()
        pen.setWidth(1)
        self.sector.draw(qp, pen)
        #pen.setColor(QColor("Black"))
        pen.setWidth(5)
        qp.setPen(pen)
        self.pop.draw(qp, pen)
        qp.end()
        
    def to_draw(self, obs, pop):

        self.sector = obs
        self.pop = pop
