from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Tracking(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
    def init(self):
        self.right = 15
        self.left = 37
        self.x = 0
        self.y = 0
        self.lastx = 0
        self.lasty = 0
    def mouseMoveEvent(self, event):   
        self.lastx, self.lasty = self.x, self.y
        self.x, self.y = event.x(), event.y()

        self.update(self.x-self.right, self.y-self.right, self.left, self.left)
        self.update(self.lastx-self.right, self.lasty-self.right, self.left, self.left)
    def paintEvent(self, event):
        qp = QPainter()
        pen = QPen(Qt.black)
        pen.setWidth(5)
        qp.begin(self)
        qp.setPen(pen)
        qp.drawEllipse(self.x-12, self.y-10, 30, 30)
        qp.end()
app = QApplication(sys.argv)
tr = Tracking()
tr.show()
app.exec_()