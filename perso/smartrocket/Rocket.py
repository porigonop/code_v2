import random
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QPointF
from Constante import THRUST, NB_ITERATION, WIDTH, HEIGHT, NB_SECTEUR
from Helper import  distsq, mapjs
class Rocket():
    """
    """
    def __init__(self, pos,\
     genes=[QPointF(random.randint(-1, 1), random.randint(-1, 1)) for _ in range(NB_ITERATION)],\
     mut=random.random() * 0.1):
        self.genes = genes
        #self.genes = [QPointF(0, -1) for _ in range(NB_ITERATION)]

        self.pos = pos
        self.initpos = self.pos
        self.speed = QPointF(0, 0)
        self.mutation_rate = mut
        self.crashed = False
        self.goal = False
        self.iter = NB_ITERATION
        self.max_iter = NB_ITERATION
    def move(self, iteration, target, secteur):
        """
        """
        #print(self.posx, self.posy)
        #print(int((self.posy/HEIGHT)*NB_SECTEUR), int((self.posx/WIDTH)*NB_SECTEUR))
        if secteur.collide(self.pos.toPoint()):
            self.crashed = True
        if distsq(self, target) < 100 and not self.goal:
            self.goal = True
            self.iter = iteration
        if not self.crashed and not self.goal:
            self.speed += self.genes[iteration] * THRUST
            self.pos += self.speed
    def draw(self, qp, pen):
        """
        """
        sec_x = mapjs(self.pos.x(), 0, WIDTH, 0, NB_SECTEUR, 1)
        sec_y = mapjs(self.pos.y(), 0, HEIGHT, 0, NB_SECTEUR, 1)
        #print("rock : ", QColor(self.pos.x() * NB_SECTEUR/WIDTH, self.pos.y() * NB_SECTEUR/HEIGHT, 0))
        pen.setColor(QColor((sec_x %2) * 255, (sec_y %2) * 255, 0))
        qp.setPen(pen)
        qp.drawPoint(self.pos)

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
        if random.random() > 0.5:
            mut = self.mutation_rate
        else:
            mut = otherrocket.mutation_rate

        return Rocket(self.initpos,\
                      self.mutate(new_genes), \
                      mut)

    def mutate(self, genes):
        """
        """
        for index, _ in enumerate(genes):
            if random.random() < self.mutation_rate:
                genes[index] = QPointF(random.randint(-1, 1), random.randint(-1, 1))
        if random.random() < self.mutation_rate:
            self.mutation_rate = random.random() * 0.1
        return genes
    def __repr__(self):
        return "je suis un missile"
