#pylint: disable=E0611
#pylint: disable=I0011
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPolygon, QColor, QPainter, QPen
from pprint import pprint
# pylint: disable=W0201
class Feuille(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.paths = []
        self.current = QPolygon()
        self.select = QPolygon()
        self.ctrl = False
        self.color = QColor("black")
        self.width = 1
        self.buttonpressed = -1
        self.selected_poly = []
    def paintEvent(self, event):
        qp = QPainter()
        pen = QPen()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)


        for path in self.paths:
            pen.setColor(path[1])
            pen.setWidth(path[2])
            qp.setPen(pen)
            qp.drawPolyline(path[0])

        pen.setColor(self.color)
        pen.setWidth(self.width)
        qp.setPen(pen)
        qp.drawPolyline(self.current)

        pen.setColor(QColor("orange"))
        qp.setPen(pen)
        for path in self.selected_poly:
            qp.drawPolyline(path[0])
        pen.setStyle(Qt.DashDotLine)
        pen.setColor(QColor("black"))
        pen.setWidth(2)
        qp.setPen(pen)
        qp.drawPolygon(self.select)

        qp.end()
    def mousePressEvent(self, event):
        self.select = QPolygon()
        self.selected_poly = []
        self.buttonpressed = event.button()
        if self.buttonpressed == Qt.RightButton:
            self.selected = QPolygon()

            self.select.append(event.pos())
        else:
            self.current = QPolygon()
            self.current.append(event.pos())
        self.update()
    def mouseReleaseEvent(self, event):
        if self.buttonpressed == Qt.RightButton:
            pass # appeller le menu
        #self.current.remove(self.current.size()-1)
        self.paths.append((self.current, self.color, self.width))
        self.current = QPolygon()
        self.buttonpressed = -1
        self.update()
    def mouseMoveEvent(self, event):
        if self.buttonpressed == Qt.RightButton:
            self.select.append(event.pos())
            self.selected_poly = []
            for index, path in enumerate(self.paths):
                if containspoly(self.select, path[0]):
                    self.selected_poly.append((path[0], index))
        else:
            self.current.append(event.pos())
        self.update()

def containspoly(poly1: QPolygon, poly2: QPolygon):
    for point_index in range(poly2.size()-1):
        if not poly1.containsPoint(poly2.point(point_index), Qt.OddEvenFill):
            return False
    return True

