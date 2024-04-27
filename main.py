#Mateusz Fydrych
#Uklady rownan liniowych
import math
from Matrix import Matrix

#tests
A = Matrix.createMatrixA(4, 1, 2, 3)
B = Matrix.createMatrixA(4, 1, 2, 3)
print(A)
print(A == B)
b = Matrix.createColumnVector(4, 6)
print(b)
