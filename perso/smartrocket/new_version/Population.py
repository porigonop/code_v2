
from Rocket import Rocket

class Population:
    def __init__(self):
        self.rockets = Rocket()


if __name__ == "__main__":
    pop = Population()
    pop.rockets.draw()
    pop.rockets.move()
    pop.rockets.draw()
    pop.rockets.move()
    pop.rockets.draw()
