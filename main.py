#Mateusz Fydrych
#Uklady rownan liniowych

import math
from Macierz import Macierz
#testy

A = Macierz.createMatrixA(4, 1, 2, 3)
B = Macierz.createMatrixA(4, 1, 2, 3)
print(A)
print(A == B)
b = Macierz.createColumnVector(4, 6)
print(b)
