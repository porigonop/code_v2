from Constante import NB_SECTEUR, NB_OBS, WIDTH, HEIGHT, OBS_SCALE
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QColor
import random
from Helper import mapjs
class Sector():
    def __init__(self):
        self.sec_width = WIDTH/NB_SECTEUR
        self.sec_height = HEIGHT/NB_SECTEUR
        self.color = [[QColor(random.random()*255, random.random()*255, random.random()*255)\
                         for _ in range(NB_SECTEUR)]\
                         for _i in range(NB_SECTEUR)]
        self.sectors = []
        for i in range(NB_SECTEUR):
            self.sectors.append([])
            for j in range(NB_SECTEUR):
                self.sectors[i].append([])
                for _ in range(NB_OBS):
                    posy = random.random() * (self.sec_width) + self.sec_width * j
                    posx = random.random() * (self.sec_height) + self.sec_height * i
                    width = random.random() * OBS_SCALE
                    height = random.random() * OBS_SCALE
                    self.sectors[i][j].append(QRect(posx, posy, width, height))

    def draw(self, qp, pen):
        for i in range(NB_SECTEUR):
            for j in range(NB_SECTEUR):
                #if not QColor(i * WIDTH/NB_SECTEUR, j * HEIGHT/NB_SECTEUR, 0).isValid():
                #    print(i * WIDTH/NB_SECTEUR, j * HEIGHT/NB_SECTEUR, 0)
                #else:
                #print("sec : ", (i % 2) * 255, (j% 2) * 255, 0)
                pen.setColor(QColor((i % 2) * 255, (j% 2) * 255, 0))
                qp.setPen(pen)
                #qp.drawRect(QRect(i * self.sec_width, j * self.sec_height, self.sec_width, self.sec_height))
                for obs in self.sectors[i][j]:
                    qp.drawRect(obs)
    def collide(self, rocketpos):
        """
        a finir
        """
        sec_x = int(mapjs(rocketpos.x(), 0, WIDTH, 0, NB_SECTEUR, 1))
        sec_y = int(mapjs(rocketpos.y(), 0, HEIGHT, 0, NB_SECTEUR, 1))
        for i in range(-1, 2):
            for j in range(-1, 2):
                if sec_x + i >= NB_SECTEUR or sec_y + j >= NB_SECTEUR:
                    continue
                for obs in self.sectors[sec_x + i][sec_y + j]:
                    if obs.contains(rocketpos):
                        return True
        return False

if __name__ == "__main__":
    s = Sector()