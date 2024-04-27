from Matrix import Matrix
from Solutions import Solutions
import time


a1 = 3
a2 = a3 = -1
N = 910
f = 3
maxIterations=200
A = Matrix.createMatrixA(N, a1, a2, a3)
b = Matrix.createColumnVector(N, f+1)

#Zaimplementuj metodę bezpośredniego rozwiązania układów równań liniowych: metodę faktoryzacji LU.
#Ile wynosi norma residuum w tym przypadku?

start = time.time()
x, error = Solutions.luFactorization(N, A, b)
end = time.time()
print("LU Method:")
print("Time:", end - start)
print("Error:", error)
