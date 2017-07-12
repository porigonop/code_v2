from lower import lower
from upper import upper
import Matrix
from Rational import Rational as R


#AX = B

A = Matrix.Matrix([[R(2),    R(3),   R(3), R(1)],
                  [R(-1),   R(1),   R(1), R(1)],
                  [R(-4),   R(-6),  R(3), R(2)],
                  [R(-2),   R(-1),  R(1), R(1)]])

B = Matrix.Matrix([ [R(21)], 
                    [R(8)],
                    [R(1)],
                    [R(3)]])

L = lower(A)

U = upper(A)

#A = LU

#UX = Y
#LY = B
print(L*U)
print(L)
print(U, "\n")
Y = []
for bindex in range(len(B.matrix)):
    b = B[bindex][0]
    y = b/L[bindex][bindex]
    for i in range(len(Y)):
        y = y - (L[bindex][i] * Y[i][0]) / L[bindex][bindex]
    Y.append([y])
Y = Matrix.Matrix(Y)


print(Y, "\n")
print(U)

X = []
for yindex in range(len(Y.matrix)-1, -1, -1):
    
    y = Y[yindex][0]
    x = y/U[yindex][yindex]
    
    for i in range(len(X)):
        x = x - (U[yindex][-i-1] * X[i][0]) / U[yindex][yindex]
    X.append([x])
X.reverse()
X = Matrix.Matrix(X)
print(X)
