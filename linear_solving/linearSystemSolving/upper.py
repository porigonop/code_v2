import Matrix
from Rational import Rational as R

def upper(matrix):
    """
    return the upper matrix of a matrix
    """
    nb_line = len(matrix.matrix)
    An = matrix
    
    for n in range (nb_line-1): # E_{n-1} * ... * E_{1} * A, so nb_line-1
        
        #create empty matrix
        E = []
        for i in range(nb_line):
            E.append([])
            
        #create E_{n} matrix
        for column in range (nb_line):
            for line in range (nb_line):
                if column == line:
                    E[line].append(R(1))
                    continue
                else :
                    if n == column and column < line:
                        E[line].append((R(0) - An[line][column]) / An[n][n])
                        continue
                        
                E[line].append(R(0))
                
                                    
        E = Matrix.Matrix(E)
        
        An = E * An
    return An



        

if __name__ == "__main__":
    A = Matrix.Matrix([[R(1),    R(2),   R(3)],
                       [R(3),   R(2),   R(1)],
                       [R(4),   R(0),  R(-5)]])
    An = upper(A)
    print (An)
