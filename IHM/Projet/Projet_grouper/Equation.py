#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Equation(QWidget):

    def __init__(self, parent, mavar, pos):
        super().__init__()
        self.initpos = pos
        self.sourceView = mavar


        self.setGeometry(800, 300, 768, 432)
        self.rect = None
        self.pressPoint = QPoint()
        self.showRect = False
        self.Image = QPixmap("photo/test.png")


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressPoint = QPoint(event.pos())
            self.rect = QRect(self.pressPoint, QSize())
            self.showRect = True
                        
    def mouseMoveEvent(self, event):
        if not self.pressPoint.isNull():
            neworigin = QPoint(min(event.x(), self.pressPoint.x()),min(event.y(), self.pressPoint.y()))
            self.rect.setTopLeft(neworigin)
            (self.rect).setBottomRight(QPoint(max(event.x(), self.pressPoint.x()), max(event.y(), self.pressPoint.y())))
            self.update()
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.sourceView.liste_equation.append((self.Image.copy(self.rect), self.initpos))
            self.sourceView.update()
            self.hide()
            
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.drawPixmap(0, 0, 768, 432, self.Image)
        if self.showRect == True:
            qp.drawRect(self.rect)
            
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    
    
