from Matrix import Matrix
from Solutions import Solutions
import time
import matplotlib.pyplot as plt

#193410
a1 = 5+4
a2 = a3 = -1
N = 910
f = 3
maxIterations=100
A = Matrix.createMatrixA(N, a1, a2, a3)
b = Matrix.createColumnVector(N, f+1)

n = [10,25,64,128,256,512,1024, 2024]
timesJacobi = []
timesGaussSeidl= []
timesLU = []
for N in n:
    A = Matrix.createMatrixA(N, a1, a2, a3)
    b = Matrix.createColumnVector(N, f+1)
    start = time.time()
    x, iterations, errors = Solutions.jacobiMethod(N, A, b, maxIterations)
    end = time.time()
    timesJacobi.append(end-start)
    start = time.time()
    x2, iterations2, errors2 = Solutions.gaussSeidelMethod(N, A, b, maxIterations)
    end = time.time()
    timesGaussSeidl.append(end-start)
    start = time.time()
    x3, error3 = Solutions.luFactorization(N, A, b)
    end = time.time()
    timesLU.append(end-start)

plt.plot(n, timesJacobi, label="Jacobi")
plt.plot(n, timesGaussSeidl, label="Gauss-Seidl")
plt.plot(n, timesLU, label="LU")
plt.xlabel("N")
plt.ylabel("Time")
plt.legend(loc="upper left")
plt.show()

