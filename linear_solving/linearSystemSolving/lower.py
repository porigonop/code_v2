import Matrix
from Identity import Identity
from Rational import Rational as R
Lower = Matrix.Matrix([[R(1),       R(0),     R(0),     R(0)],
                           [R(-1, 2),   R(1),     R(0),     R(0)],
                           [R(-2),      R(0),     R(1),     R(0)],
                           [R(-1),      R(4, 5),  R(2, 9),  R(1)]])
def lower(matrix):
#pas fini
    nb_line = len(matrix.matrix)
    En = Identity(nb_line)
    for k in range (nb_line - 1): #E_{n-1} ... E_{1}
        #Create empty matrix
        E = []
        for i in range(nb_line):
            E.append([])
        
        #Create E_{n}^{-1} matrix
        for column in range (nb_line):
            for line in range (nb_line):
                if column == line: #in the diagonal
                    E[line].append(R(1))
                    
                elif k == column and column < line:
                    E[line].append( matrix[line][k] / matrix[k][k])
                else:
                    E[line].append(R(0))
        E = Matrix.Matrix(E)
        En =  En  * E
        #---------------------
        #multiply matrix by E
        #---------------------
        E = E.matrix
        
        #Create E_{n}^{-1} matrix
        for column in range (nb_line):
            for line in range (nb_line):
                if column == line: #in the diagonal
                    pass
                else:
                    E[column][line] = R(0)-E[column][line]
        #AFAIRE ! matrix deviens matrix * E_{n}  
        E = Matrix.Matrix(E)
        matrix = E * matrix
        #-------------------------

    return En


if __name__ == "__main__":
    A = Matrix.Matrix([[R(1),    R(2),   R(3)],
                       [R(3),   R(2),   R(1)],
                       [R(4),   R(0),  R(-5)]])
                       
    
    Lower = Matrix.Matrix([[R(1),       R(0),     R(0),     R(0)],
                           [R(-1, 2),   R(1),     R(0),     R(0)],
                           [R(-2),      R(0),     R(1),     R(0)],
                           [R(-1),      R(4, 5),  R(2, 9),  R(1)]])
    An = lower(A)
    print (An)
    

    #print(Lower)
    Upper = Matrix.Matrix([ [R(2),      R(3),       R(3),       R(1)],
                            [R(0),      R(5, 2),    R(5, 2),    R(3, 2)],
                            [R(0),      R(0),       R(9),       R(4)],
                            [R(0),      R(0),       R(0),       R(-4, 45)]])
    #print(Upper)
    print(Lower * Upper)
    
