import random
from Constante import *
from Helper import  distsq, mapjs, constrain

class Rocket():
    """
    """
    crashed = False
    goal = False
    def __init__(self, pos,\
            genes=[(random.randint(-1, 1), random.randint(-1, 1))
                for _ in range(NB_ITERATION)],\
            mut=random.random() * 0.1):
        # gene is actually the acceleration of the rocket
        self.genes = genes

        self.posx = pos[0]
        self.posy = pos[1]
        self.initpos = (self.posx, self.posy)

        # initial speed of the rocket
        self.speedx = 0
        self.speedy = 0

        self.mutation_rate = mut

        # the number where the rocket find the target
        self.iter = NB_ITERATION
        self.max_iter = NB_ITERATION

    def move(self, iteration, target, secteur):
        """
        """
        #print(self.posx, self.posy)
        #print(int((self.posy/HEIGHT)*NB_SECTEUR), int((self.posx/WIDTH)*NB_SECTEUR))
        if self.crashed or self.goal:
            return
        if secteur.collide((self.posx, self.posy)):
            self.crashed = True
        elif distsq(self, target) < 100:
            self.goal = True
            self.iter = iteration
        else:
            self.speedx += self.genes[iteration][0] * THRUST
            self.speedy += self.genes[iteration][1] * THRUST

            self.posx += self.speedx
            self.posy += self.speedy

    def draw(self, qp, pen):
        """
        """
        qp.drawEllipse(self.posx, self.posy, 100, 100)

    def crossover(self, otherrocket):
        """
        """
        mid = random.randrange(0, self.max_iter)
        new_genes = []
        for index in range(self.max_iter):
            if index > mid:
                new_genes.append(otherrocket.genes[index])
            else:
                new_genes.append(self.genes[index])
        if random.random() < 0.5:
            mut = self.mutation_rate
        else:
            mut = otherrocket.mutation_rate

        new_rocket = Rocket(self.initpos,\
                      new_genes,\
                      mut)
        new_rocket.mutate()
        return new_rocket

    def mutate(self):
        """
        """
        for index in range(len(self.genes)):
            if random.random() < self.mutation_rate:
                self.genes[index] = (random.randint(-1, 1),
                        random.randint(-1, 1))
        if random.random() < self.mutation_rate:
            self.mutation_rate = random.random() * 0.1

    def succed(self, target):
        # will not == 0 in practice since target is a ball
        dist = 1 / distsq(self, target)
        if self.crashed:
            dist *= TOUCH_OBS
        elif self.goal:
            dist *= TOUCH_TARGET
            dist /= mapjs(self.iter, 0, self.max_iter, 0, 100)# + 0.1
        return dist * SUCCED_SCALE

if __name__ == "__main__":
    roca = Rocket((0,0), [(0,0) for _ in range(NB_ITERATION)], 0)
    rocb = Rocket((0,0), [(0,0) for _ in range(NB_ITERATION)], 0)
    roca.mutate()
    rocb.mutate()
    assert roca.genes == rocb.genes
    rocc = roca.crossover(rocb)
    assert rocc.genes == rocb.genes
    assert roca.genes == rocc.genes
    roca.mutation_rate = 1
    roca.mutate()
    assert roca.genes != rocb.genes
