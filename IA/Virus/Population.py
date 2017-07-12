"""
contain population
"""
import random
from time import sleep
from VirusGame import VirusGame
from computer_evolve import ComputerEvolve as CE

GRID = 4

def mapjs(value: int, mini: int, maxi: int, newmin: int, newmax: int) -> float:
    """
    make a scale fom mini, maxi to newmin, newmax of the value
    """
    return (value / (maxi - mini))*(newmax-newmin)
def mean(numbers: list)-> float:
    """
    return the mean of the list in parameter
    """
    return sum(numbers)/len(numbers)
class Population(object):
    """
    define the Population of computer evolve
    """
    def __init__(self, pop_number: int=10):
        self.population = [CE("", "") for _ in range(pop_number)]
        self.pop_number = pop_number

    def next_generation(self):
        """
        create a nex generation of computer
        """
        breedingpool = []
        score = []
        for comp in self.population:
            score.append(comp.score)


        max_score = max(score)
        for comp_index in range(len(self.population)):
            for _ in range(int(mapjs(score[comp_index],\
                                    0, max_score, 1, 100))):
                breedingpool.append(self.population[comp_index])
        new_pop = []
        for _ in range(self.pop_number):
            parent1 = random.choice(breedingpool)
            parent2 = random.choice(breedingpool)
            new_pop.append(parent1.crossover(parent2))
        self.population = new_pop

    def evolve(self, number_of_generation: int):
        """
        evolve the population over a certain number of generation
        """
        for _ in range(number_of_generation):
            for comp1 in self.population:
                scores = []
                for comp2 in self.population:
                    game = VirusGame(GRID, \
                                    comp1, comp2)#,\
                                    #no_print=True)
                    while game.play():
                        sleep(1)
                        #pass
                    score1, dummy_score2 = game.get_score()
                    scores.append(score1)
                comp1.score = mean(scores)
            self.next_generation()

if __name__ == "__main__":
    POP = Population()
    POP.evolve(5)



