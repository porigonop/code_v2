import random

class Qbit():
    def __init__(self, axis, value):
        
        if value != 0 and value != 1:
            raise ValueError("value must be 0 or 1 get : ", value)
        self.axis = axis
        self.value = value

    def measure(self, axis):
        if axis == self.axis:
            return self.value

        else:
            self.axis = axis
            if random.random() > 0.5:
                self.value = 0
                return 0
            else:
                self.value = 1
                return 1
    def __repr__(self):
        return str(self.value) + str(self.axis)

