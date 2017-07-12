from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QRect, QLine, QPoint
import sys
import time
from Grid import Grid
from Player import Player
from Computer import Computer


class GUI(QWidget):
    name_to_color = {"." : QColor(0, 0, 0),
                     "x" : QColor(255, 0, 0),
                     "o" : QColor(0, 255, 255),
                     "+" : QColor(0, 0, 255),
                     "*" : QColor(125, 125, 125)
                    }
    def __init__(self, p1, p2, grid_lenght):
        super().__init__()
        #self.init_game()
        self.grid = Grid(grid_lenght)
        self.player1 = p1
        self.current_player = self.player1
        self.player2 = p2
        self.player1.set_adversary(self.player2)
        self.player2.set_adversary(self.player1)
        #self.grid.add_a_pawn(p1, 1, 1)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Virus Game")
        self.show()
    def paintEvent(self, e):
        qp = QPainter()
        self.drawgame(qp)

    def drawgame(self, qp):
        qp.begin(self)
        pen = QPen()
        pen.setColor(QColor("black"))
        pen.setWidth(3)
        qp.setPen(pen)
        for index_x in range(len(self.grid.grid)):
            qp.drawLine(QPoint(int(index_x * float(self.width())/self.grid.grid_length),
                               0),
                        QPoint(int(index_x * float(self.width())/self.grid.grid_length),
                               self.height()))
            for index_y in range(len(self.grid.grid[index_x])):
                qp.drawLine(QPoint(0,
                                   int(index_y * float(self.height())/self.grid.grid_length)),
                            QPoint(self.width(),
                                   int(index_y * float(self.height())/self.grid.grid_length)))
                if self.grid.grid[index_x][index_y].color is None:
                    continue
                pen.setColor(QColor(self.grid.grid[index_x][index_y].color))
                qp.fillRect(QRect(QPoint(int(index_x * float(self.width()) / self.grid.grid_length + 1),
                                   int(index_y * float(self.height()) / self.grid.grid_length + 1)),
                            QPoint(int(index_x * float(self.width()) / self.grid.grid_length + float(self.width())/self.grid.grid_length),
                                   int(index_y * float(self.height()) / self.grid.grid_length + float(self.height())/self.grid.grid_length))),
                                   QColor(self.grid.grid[index_x][index_y].color))
                pen.setColor(QColor("black"))
        qp.end()


    def mousePressEvent(self, event):
        pos_x = int(event.x() / self.width() * self.grid.grid_length)
        pos_y = int(event.y() / self.height() * self.grid.grid_length)
        if pos_x < 0 or pos_x >= self.grid.grid_length:
            return
        if pos_y < 0 or pos_y >= self.grid.grid_length:
            return
        if not self.grid.add_a_pawn(self.current_player, pos_x, pos_y):
            return
        self.current_player = self.current_player.adversary
        self.repaint()
        if type(self.current_player) is Computer:

            pos = self.current_player.play(self.grid)
            self.grid.add_a_pawn(self.current_player, pos[0], pos[1])
            self.current_player = self.current_player.adversary
            self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI(Player("a", "red"), Computer("j", "blue"), 7)
    gui.show()
    app.exec_()
