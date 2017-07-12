from Rational import Rational as R

class Matrix:
    """ define Matrix """
    
    def __init__(self, matrix):
        """create an empty matrix
        """
        self.matrix = matrix
        
    def multiply(self, matrix):
        """
        define the matrix product
        no change to the initial Matrix
        """
        result = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(matrix.matrix[i])):
                somme = R(0)
                for k in range(len(matrix.matrix)):
                    somme += self.matrix[i][k] * matrix.matrix[k][j]
                line.append(somme)
            result.append(line)
        return Matrix(result)
        
    def reverse_diag(self):
        """
        Test if a matrix is diagonal and reverse it
        """
        result = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix)):
                if i == j and self.matrix[i][j] != 0:
                    line.append(R(1)/self.matrix[i][j])
                else:
                    line.append(R(0))
                if i != j and self.matrix[i][j] != R(0.0):
                    # print(i, j, self.matrix[i][j])
                    raise ValueError("matrix isn't diagonal")
            result.append(line)
        return Matrix(result)

    def lower(self):
        matrix = self
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
            E = Matrix(E)
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
            E = Matrix(E)
            matrix = E * matrix
            #-------------------------

        return En

    def upper(self):
        """
        return the upper matrix of a matrix
        """
        matrix = self
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
                    
                                        
            E = Matrix(E)
            
            An = E * An
        return An
    
    def __mul__(self, matrix):
        return self.multiply(matrix)
        
    def __sub__(self, matrix):
        result = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix)):
                line.append(self.matrix[i][j] - matrix.matrix[i][j])
            result.append(line)
        result = Matrix(result)
        return result
        
    def __add__(self, matrix):
        result = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix[i])):
                line.append(self.matrix[i][j] + matrix.matrix[i][j])
            result.append(line)
        result = Matrix(result)
        return result
            
    
    def __getitem__(self, number):
        return self.matrix[number]
        
    def __repr__(self):
        result = ""
        for i in range(len(self.matrix)):
            result = result + "( "
            for j in range(len(self.matrix[i])): 
                 result = result + str(self.matrix[i][j]) + "\t"
            result = result + ")\n"
        result = result +"-------------"
        return result.strip()




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
    A = [[R(1), R(2), R(3)],
         [R(3), R(4), R(5)],
         [R(1), R(2), R(3)]]
    
    B = [[R(5), R(6), R(10)],
         [R(7), R(8), R(45)],
         [R(1), R(2), R(3)]]
    A = Matrix(A)
    B = Matrix(B)
    print (A.multiply(B))
    
    A = [[R(3), R(0), R(0)],
        [R(0), R(2), R(0)],
        [R(0), R(0), R(0)]]
    A = Matrix(A)
    print(A.reverse_diag())
    
    A = Matrix([[R(2),    R(3),   R(3), R(1)],
                  [R(-1),   R(1),   R(1), R(1)],
                  [R(-4),   R(-6),  R(3), R(2)],
                  [R(-2),   R(-1),  R(1), R(1)]])

    B = Matrix([ [R(21)], 
                    [R(8)],
                    [R(1)],
                    [R(3)]])
    print(A*B)
    
