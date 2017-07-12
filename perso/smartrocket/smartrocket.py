"""smart rocket"""
#pan / panning matrice de transformation

import time
import sys
import random
from PyQt5.QtWidgets import QApplication, QScrollArea
from PyQt5.QtCore import QTimer
from GUI import Fenetre
from Sector import Sector
from Population import Population
from Constante import FPS, NB_ITERATION
class Application():
    def __init__(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        #self.scrollarea = QScrollArea()
        self.fenetre = Fenetre()
        #self.scrollarea.setWidget(self.fenetre)
        self.population = Population()
        self.sector = Sector()
        self.fenetre.to_draw(self.sector, self.population)
        self.timer.start(5)
    def move(self):
        self.population.move(self.sector)

    def refresh(self):
        self.move()
        self.fenetre.repaint()






"""
def pointeur(event):
    population.target.move(event.x, event.y)
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    APP = Application()
    sys.exit(app.exec_())
