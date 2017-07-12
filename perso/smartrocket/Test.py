from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer, QRect
from Sector import Sector
import sys
from Constante import WIDTH, HEIGHT, FPS
#QScrollarrea
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
        qp = QPainter(self)
        qp.translate(50, 10)
        qp.scale(2, 2)
        qp.rotate(5)
        #qp.begin(self)
        pen = QPen()
        pen.setWidth(1)
        qp.setPen(pen)
        qp.drawRect(self.sector)#self.sector.draw(qp, pen)
        #pen.setWidth(5)
        #qp.setPen(pen)
        #self.pop.draw(qp)
        #qp.end()
    def to_draw(self, obs, pop):

        self.sector = obs
        self.pop = pop


if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = Fenetre()
    f.to_draw(QRect(50, 50, 100, 100), None)
    app.exec_()