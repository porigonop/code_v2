from Graph import Graph
import random
from pprint import pprint
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRect, QLine, QPoint
import sys
H = 500
W = 500
nb = 30
w = W/nb
h = H / nb

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, W, H)
        self.setWindowTitle('Maze')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangle(qp)
        qp.end()

    def drawRectangle(self, qp):

        for node in maze.G.nodes:
            qp.setBrush(QColor(255, 255, 255))
            #qp.drawEllipse(QRect(node[0] * w +w/4,\
            #                    node[1] * h + h/4 ,\
            #                     w/2 , h/2))
            for other_node in maze.G.nodes:
                if other_node in maze.G.adjency_list[str(node)]:
                    if [other_node, node, True] in maze.G.edges:
                        line = QLine(QPoint(node[0] * w +w/2,\
                                            node[1] * h + h/2),
                                    QPoint(other_node[0] * w +w/2,\
                                           other_node[1] * h + h/2))
                        qp.drawLine(line)
            #qp.drawEllipse(QRect(1 * W / nb, 0 * H / nb,\
            #            (1 ) * W/nb, (0 + 1) * H/nb))
            
class Maze:
    def __init__(self, height, width):
        self.G = Graph()
        self.h = height
        self.w = width
        self.start = (0,0)
        self.end = (0,0)
        for i in range(height):
            for j in range(width):
                self.G.add_a_node((i, j))
        for node in self.G.nodes:
            for ot_node in self.G.nodes:
                if (ot_node[0] + 1 == node[0]\
                and ot_node[1] == node[1])\
                or (ot_node[1] + 1 == node[1]\
                and ot_node[0] == node[0]):
                    self.G.add_an_edge(node, ot_node, False)
    
    def create_maze(self):
        unvisited = [node for node in self.G.nodes]
        
        current = self.start
        unvisited.remove(current)
        stack = []

        while unvisited != []:  
            unvisitedneighboor = [node \
                    for node in self.G.adjency_list[str(current)]\
                                if node in unvisited]
            if unvisitedneighboor != []:
                
                neigh = random.choice(unvisitedneighboor)
                stack.append(current)

                index = self.G.edges.index([current, neigh, False])
                index1 = self.G.edges.index([neigh, current, False])
                self.G.edges[index][2] = True
                self.G.edges[index1][2] = True
                current = neigh
                unvisited.remove(current)

                
            elif stack != []:
                current = stack.pop()
                
            
    def __repr__(self):
        return str(self.G)




if __name__ == "__main__":
    maze = Maze(nb, nb)
    maze.create_maze()
    app = QApplication(sys.argv)
    ap = Application()
    sys.exit(app.exec_())
