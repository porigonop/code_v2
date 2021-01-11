from Constante import NB_SECTEUR, NB_OBS, WIDTH, HEIGHT, OBS_SCALE
from PyQt5.QtCore import QRect, QPoint, Qt
from PyQt5.QtGui import QColor
import random
from Helper import mapjs
from Obstacle import Obstacle
class Sector():
    def __init__(self):

        # self.highlighted = []

        self.sec_width = WIDTH/NB_SECTEUR
        self.sec_height = HEIGHT/NB_SECTEUR
        self.color = [[QColor((i/NB_SECTEUR)*255, (j/NB_SECTEUR) *255, 255)\
                         for i in range(NB_SECTEUR)]\
                         for j in range(NB_SECTEUR)]
        # actual sector w/ obstacle
        self.sectors = []
        # retangle representation arround sector, mostly debug
        self.rect = []
        for i in range(NB_SECTEUR):
            self.sectors.append([])
            self.rect.append([])
            for j in range(NB_SECTEUR):
                self.sectors[i].append([])
                self.rect[i].append(QRect(QPoint(self.sec_width * i, self.sec_height * j),
                                          QPoint((self.sec_width) + self.sec_width *i, (self.sec_height) + self.sec_height * j)))
                for _ in range(NB_OBS):
                    posy = random.random() * (self.sec_width) + self.sec_width * i
                    posx = random.random() * (self.sec_height) + self.sec_height * j
                    width = random.random() * OBS_SCALE
                    height = random.random() * OBS_SCALE
                    self.sectors[i][j].append(Obstacle(posx, posy, height, width))

    def draw(self, qp, pen):
        for i in range(NB_SECTEUR):
            for j in range(NB_SECTEUR):
                #if not QColor(i * WIDTH/NB_SECTEUR, j * HEIGHT/NB_SECTEUR, 0).isValid():
                #    print(i * WIDTH/NB_SECTEUR, j * HEIGHT/NB_SECTEUR, 0)
                #else:
                #print("sec : ", (i % 2) * 255, (j% 2) * 255, 0)
                # ii, jj = self.highlighted[1][0], self.highlighted[1][1]
                # pen.setColor(QColor((ii % 2) * 255, (jj% 2) * 255, 0))
                # qp.setPen(pen)
                # qp.drawRect(self.highlighted[0])
                pen.setColor(self.color[j][i])
                qp.setPen(pen)
                # qp.drawText(self.rect[i][j], Qt.AlignCenter, "test")
                # qp.drawRect(QRect(i * self.sec_width, j * self.sec_height, self.sec_width, self.sec_height))
                for obs in self.sectors[i][j]:
                    obs.draw(qp)
    def collide(self, rocketpos):
        """
        """
        if rocketpos[0] < 0 or rocketpos[0] > WIDTH\
            or rocketpos[1] < 0 or rocketpos[1] > HEIGHT:
            return True
        sec_x = int(mapjs(rocketpos[0], 0, WIDTH, 0, NB_SECTEUR-1, 1))
        sec_y = int(mapjs(rocketpos[1], 0, HEIGHT, 0, NB_SECTEUR-1, 1))
        # self.highlighted = [self.rect[sec_x][sec_y], (sec_x, sec_y)]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (sec_x + i >= NB_SECTEUR or sec_y + j >= NB_SECTEUR)\
                    or sec_x + i < 0 or sec_y + j < 0:
                    continue
                for obs in self.sectors[sec_x + i][sec_y + j]:
                    if obs.collide(rocketpos):
                        return True
        return False

if __name__ == "__main__":
    s = Sector()
