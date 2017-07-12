from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class ZoneDessin(QWidget):
    def __init__(self, color = QColor(0, 0, 0), width = 1):
        super().__init__()
        self.init(color, width)
    def init(self, color, width):
        self.setMinimumSize(200, 200)
        self.color = color
        self.width = width
        self.lines = []
        self.point1 = QPoint(0, 0)
        self.point2 = QPoint(0, 0)
    def paintEvent(self, e):
        qp = QPainter()
        pen = QPen()
        qp.begin(self)

        for line in self.lines:
            pen.setColor(line[1])
            pen.setWidth(line[2])
            qp.setPen(pen)
            qp.drawLine(line[0])

        if not self.point1 is None and not self.point2 is None:
            pen.setColor(self.color)
            pen.setWidth(self.width)
            qp.setPen(pen)
            qp.drawLine(self.point1, self.point2)
        qp.end()
    def mousePressEvent(self, e):
        self.point1 = e.pos()
        self.point2 = e.pos()
        self.update()
    def mouseMoveEvent(self, e):
        self.point2 = e.pos()
        self.update()
    def mouseReleaseEvent(self, event):
        self.lines.append((QLine(self.point1, self.point2),\
                          self.color,\
                          self.width))