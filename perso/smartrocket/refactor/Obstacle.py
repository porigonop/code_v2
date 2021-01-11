

class Obstacle():

    def __init__(self, posx, posy, height, width):
        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width


    def collide(self, rocketpos):
        # rocket is left to the obstacle
        if self.posx > rocketpos[0]:
            return False
        # rocket is upper than obstacle
        if self.posy > rocketpos[1]:
            return False
        # rocket is rigth to the obstacle
        if self.posx + self.width < rocketpos[0]:
            return False
        # rocket is lower than obstacle
        if self.posy + self.height < rocketpos[1]:
            return False
        return True

    def draw(self, qp):
        qp.drawRect(self.posx, self.posy, self.height, self.width)
