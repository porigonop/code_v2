from Matrix import Matrix
from Rational import Rational as R


class Identity(Matrix):
    def __init__(self, size):
        """
        return 1 if i == j
        return 0 if i != j
        """
        self.matrix = []
        for i in range(size):
            self.matrix.append([])
            for j in range(size):
                
                if i == j:
                    self.matrix[i].append(R(1.))
                else:
                    self.matrix[i].append(R(0.))

if __name__ == "__main__":
    id_3 = Identity(3)
    print(id_3)
