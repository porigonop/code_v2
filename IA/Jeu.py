from Graph import Graph
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRect, QLine, QPoint
import sys
H = 500
W = 500
nb = 50
w = W/nb
h = H / nb

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0, 0, W, H)
        self.setWindowTitle('jeu')
        self.show()
        
    def paintEvent(self, e):
        #pos1 = input()
        #pos2 = input()
        game.jouer([1, 1])
        qp = QPainter()
        qp.begin(self)
        self.drawGame(qp)
        qp.end()
        
    def drawGame(self, qp):
        for node in game.node:
            qp.setBrush(QColor(255, 255, 255))
            qp.drawEllipse(QRect(node[0] * w +w/4,\
                                node[1] * h + h/4 ,\
                                 w/2 , h/2))
            

class Game:
    def __init__(self, taille):
        self.G = Graph()
        for i in range(taille):
            for j in range(taille):
                self.G.add_a_node((i, j, 0))
    
    def jouer(self, pos):
        self.G.nodes.remove(set(pos + [0]))
        self.G.nodes.add(pos + [1])

if __name__ == "__main__":
    game = Game(3)
    app = QApplication(sys.argv)
    ap = Application()
    sys.exit(app.exec_())
