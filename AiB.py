from Macierz import Macierz
from Solutions import Solutions
import time
#193410
a1 = 9
a2 = a3 = -1
N = 910
f = 3
A = Macierz.createMatrixA(N, a1, a2, a3)
b = Macierz.createColumnVector(N, f+1)

#metoda Jacobiego
start = time.time()
x, iterations, errors = Solutions.jacobiMethod(N, A, b, 100)
end = time.time()
print("Jacobi Method:")
print("Time:", end - start)
#print(x)
print(iterations)
print(errors[iterations-1])

#metoda Gaussa-Seidela
start = time.time()
x2, iterations2, errors2 = Solutions.gaussSeidelMethod(N, A, b, 100)
end = time.time()
print("\nGauss-Seidel Method:")
print("Time:", end - start)
#print(x2)
print(iterations2)
print(errors2[iterations2-1])
