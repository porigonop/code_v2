"""
"""
import time
import random
from Rocket import Rocket
from Target import Target
from Constante import WIDTH, HEIGHT, NB_ROCKET, NB_ITERATION
from Helper import mapjs
class Population():
    """
    Define the population of rocket in the simulation
    """
    nb_iterations = 0
    def __init__(self):
        self.rockets = [Rocket([WIDTH/2, HEIGHT])
                for _ in range(NB_ROCKET)]

        self.iteration = 0
        self.target = Target(WIDTH / 2, HEIGHT / 8)

    def move(self, secteur):
        for rocket in self.rockets:
            rocket.move(self.iteration, self.target, secteur)
        self.iteration += 1
        if self.iteration >= NB_ITERATION:
            print(self.nb_iterations)
            self.nb_iterations+=1
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

        score = []
        succed_rate = 0
        for rocket in self.rockets:
            score.append(rocket.succed(self.target))
            if rocket.goal:
                succed_rate += 1.
        succed_rate /= NB_ROCKET
        print("{}%".format(succed_rate * 100))

        max_score = max(score)
        sum_score = sum(score)

        score = list(map(lambda x:x / sum_score, score))

        new_pop = []
        for _ in range(NB_ROCKET):
            choice = random.random()
            pos = 0
            while choice >= 0:
                choice -= score[pos]
                if choice >= 0:
                    pos += 1
            parenta = self.rockets[pos]

            choice = random.random()
            pos = 0
            while choice >= 0:
                choice -= score[pos]
                if choice >= 0:
                    pos += 1
            parentb = self.rockets[pos]

            new_pop.append(parenta.crossover(parentb))
        self.rockets = new_pop
        time.sleep(1)
