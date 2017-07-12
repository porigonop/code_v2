"""
"""
from PyQt5.QtCore import QPointF
import time
import random
from Rocket import Rocket
from Target import Target
from Constante import WIDTH, HEIGHT, NB_ROCKET, NB_ITERATION
from Helper import succed, mapjs
class Population():
    """
    """
    def __init__(self):
        self.rockets = []
        self.iteration = 0
        self.target = Target(WIDTH / 2, HEIGHT / 8)
        for _ in range(NB_ROCKET):
            self.rockets.append(Rocket(QPointF(WIDTH / 2 + 50, HEIGHT)))
    def move(self, secteur):
        for rocket in self.rockets:
            rocket.move(self.iteration, self.target, secteur)
        self.iteration += 1
        if self.iteration >= NB_ITERATION:
            self.iteration = 0
            self.new_pop()
    def draw(self, qp, pen):
        """
        """
        self.target.draw(qp)
        for rocket in self.rockets:
            rocket.draw(qp, pen)
        time.sleep(.1)
    def new_pop(self):
        """
        """

        score = []
        succed_rate = 0
        for elt in range(len(self.rockets)):
            score.append(succed(self.rockets[elt], self.target))
            if self.rockets[elt].goal:
                succed_rate += 1.
        succed_rate /= NB_ROCKET
        print(str(succed_rate*100) + "%")


        max_score = max(score)
        sum_score = sum(score)

        score = list(map(lambda x:x / sum_score, score))

        new_pop = []
        for _ in range(NB_ROCKET):
            choice = random.random()
            pos = -1
            while choice >= 0.00001:
                choice -= score[pos]
                pos += 1
            parenta = self.rockets[pos]

            choice = random.random()
            pos = -1
            while choice >= 0.00001:
                choice -= score[pos]
                pos += 1
            parentb = self.rockets[pos]

            new_pop.append(parenta.crossover(parentb))
        self.rockets = new_pop
        time.sleep(1)
    def __repr__(self):
        return "je suis la pop"
