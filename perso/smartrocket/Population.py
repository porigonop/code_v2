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
            self.rockets.append(Rocket(QPointF(WIDTH / 2 + 10, HEIGHT)))
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
    def new_pop(self):
        """
        """
        breedingpool = []
        score = []
        succed_rate = 0
        for elt in range(len(self.rockets)):
            score.append(succed(self.rockets[elt], self.target))
            if self.rockets[elt].goal:
                succed_rate += 1.
        succed_rate /= NB_ROCKET
        print(str(succed_rate*100) + "%")
        max_score = max(score)
        for elt in range(len(self.rockets)):
            for _ in range(int(mapjs(score[elt], 0, max_score, 1, 100))):
                breedingpool.append(self.rockets[elt])
        new_pop = []
        for _ in range(NB_ROCKET):
            parenta = random.choice(breedingpool)
            parentb = random.choice(breedingpool)
            new_pop.append(parenta.crossover(parentb))
        self.rockets = new_pop
        time.sleep(1)
    def __repr__(self):
        return "je suis la pop"
