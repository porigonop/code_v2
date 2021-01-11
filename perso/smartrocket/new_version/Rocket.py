



class Rocket:
    def __init__(self):
        self.initial_position = (0, 0)
        self.position = [0, 0]
        self.speed = [0, 0]
        self.acceleration = [0, 1]
        self.genes = [(0, 1), (0, 2), (1, 0)]
        self.iteration = 0

    def draw(self):
        print(self.position)

    def move(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

        self.speed[0] += self.acceleration[0]
        self.speed[1] += self.acceleration[1]

        self.acceleration = self.genes[self.iteration]


