from Matrix import Matrix
from Matrix import Identity
from Rational import Rational as R

class LinearSystem():
    def __init__(self, A, Y):

        self.A = A
        self.Y = Y
        self.U = A.upper()
        self.L = A.lower()

    def ChangeY(self, Y):
        self.Y = Y
        
    def Jacobi(self, iteration = 5):
        """
        iterate throught the jacobi method to solve the system
        """
        Id = Identity(len(self.A.matrix))
        #exctract the Diagonal from the matrix
        Diag = [[self.A[i][j] \
                if i == j else 0 \
                for j in range(len(self.A.matrix))] \
                for i in range(len(self.A.matrix))]
        Diag = Matrix(Diag) 
        inv_diag = Diag.reverse_diag()
        X_k = Matrix([[0]\
                      for i in range(len(self.A.matrix)) ])

        # Id check
        # inv_diag check
        # A check
        # Y check
        for i in range(iteration):
            B = (Id - (inv_diag * self.A))
            X_k = ( B * X_k) + (inv_diag * self.Y)
            # x = Bx + (ID - B) A^-1 * Y
            # B = Id - D^-1A
            # pour avoir (Id - B) A^-1 * Y
            # sans le A^-1
            # soit x = Bx + D^-1 * Y
            # (I - D^-1 * A) * X_k + D^-1 * Y
            #erreur potentielle de calcul, ou systeme insolvable.
            
        return(X_k)


    def LUResolution(self):
        B = []
        for yindex in range(len(self.Y.matrix)):
            y = self.Y[yindex][0]
            b = y/self.L[yindex][yindex]
            for i in range(len(B)):
                b = b - (self.L[yindex][i] * B[i][0]) / self.L[yindex][yindex]
            B.append([b])
        B = Matrix(B)
        X = []
        for bindex in range(len(B.matrix)-1, -1, -1):
            b = B[bindex][0]
            x = b/ self.U[bindex][bindex]
            for xindex in range(len(X)):
                x = x - (self.U[bindex][-xindex-1] * X[xindex][0])/ self.U[bindex][bindex]
            X.append([x])
        X.reverse()
        return Matrix(X)

if __name__ == "__main__":
    A = Matrix([    [R(2),    R(3),   R(3), R(1)],
                    [R(-1),   R(1),   R(1), R(1)],
                    [R(-4),   R(-6),  R(3), R(2)],
                    [R(-2),   R(-1),  R(1), R(1)]])

    Y = Matrix([    [R(21)], 
                    [R(8)],
                    [R(1)],
                    [R(3)]])
    

    LS = LinearSystem(A, Y)
    X = LS.LUResolution()
    
    print(X)
    
    B = Matrix([       [R(5, 4),    R(-13, 6),   R(9, 4), R(11, 12)],
                       [R(2, 3),    R(-7, 6),    R(4, 3), R(2, 3)],
                       [R(1, 3),    R(-1, 3),    R(1, 6), R(1, 3)],
                       [R(-3, 4),   R(7, 6),     R(-1, 4),R(-5, 12)]])

    target = Matrix([[R(22, 3)], 
                     [R(5)],
                     [R(3, 2)],
                     [R(-5, 6)]])
                     
    LSJ = LinearSystem(B, target)
    X1 = LSJ.Jacobi(50)
    print(B * X1)
