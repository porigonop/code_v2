from Qbit import Qbit
import random
class Message():
    def __init__(self, message):
        self.message = message
        self.binarie = [bin(ord(c))[2:]for c in message]
        self.crashed = []
        
    def encode(self, nb_rep: int, percent_crash: float):
        index = -2
        Qcode = []
        for _ in range(nb_rep):
            for bin_letter in self.binarie:
                for binarie in bin_letter:
                    index += 1
                    if random.random() > 0.5:
                        axis = "z"
                    else:
                        axis = "x"


                    if random.random() < percent_crash:
                        index += 1
                        if random.random() > 0.5:
                            Qcode.append(Qbit(axis, 0))
                            self.crashed.append((index, (axis, 0)))
                        else:
                            Qcode.append(Qbit(axis, 1))
                            self.crashed.append((index, (axis, 1)))

                    Qcode.append(Qbit(axis, int(binarie)))
        return Qcode

    def get_crashed(self):
        return self.crashed

if __name__ == "__main__":
    m = Message("a")
    print(bin(ord("a"))[2:])
    print()
    print(m.get_crashed())
    print(m)