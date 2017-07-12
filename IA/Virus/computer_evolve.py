"""
contain the computer who evolve
"""
import random

from Computer import Computer

class ComputerEvolve(Computer):
    """
    define the evolving comupter
    """
    def __init__(self, player_name, player_color, depth=1,\
                genes=[random.randrange(-100, 100) for _ in range(8)],\
                mutation_rate=random.random() * 0.1):

        Computer.__init__(self, player_name, player_color)
        self.depth = depth
        self.genes = genes

        self.player_pawn = genes[0]
        self.opponent_pawn = genes[1]
        self.player_win = genes[2]
        self.opponent_win = genes[3]
        self.player_locked = genes[4]
        self.opponent_locked = genes[5]
        self.depth_player = genes[6]
        self.depth_opponent = genes[7]

        self.mutation_rate = mutation_rate
        self.score = None

    def crossover(self, other_computer: "ComputerEvolve")-> "ComputerEvolve":
        """
        cross 2 computer by genes
        """
        mid = random.random() * len(self.genes)
        new_genes = []
        for i in range(len(self.genes)):
            if i > mid:
                new_genes.append(other_computer.genes[i])
            else:
                new_genes.append(self.genes[i])
        if random.random() > 0.5:
            mut = self.mutation_rate
        else:
            mut = other_computer.mutation_rate

        return ComputerEvolve("",\
                              "",\
                              genes=self.mutate(new_genes), \
                              mutation_rate=mut)

    def mutate(self, genes: list)-> list:
        """
        make random mutation in the genes
        :Param genes: List

        :return Value: List
        """
        for index, _ in enumerate(genes):
            if random.random() < self.mutation_rate:
                genes[index] = random.randrange(-100, 100)
        if random.random() < self.mutation_rate:
            self.mutation_rate = random.random() * 0.1
        return genes
