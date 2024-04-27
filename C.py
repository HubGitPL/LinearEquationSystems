from Matrix import Matrix
from Solutions import Solutions
import time
import matplotlib.pyplot as plt

a1 = 3
a2 = a3 = -1
N = 910
f = 3
maxIterations=200
A = Matrix.createMatrixA(N, a1, a2, a3)
b = Matrix.createColumnVector(N, f+1)

#Jacob method
start = time.time()
x, iterations, errors = Solutions.jacobiMethod(N, A, b, maxIterations)
end = time.time()
print("Jacobi Method:")
print("Time:", end - start)
#print(x)
print(iterations)
print(errors[iterations-1])

#Gauss-Seidel method
start = time.time()
x2, iterations2, errors2 = Solutions.gaussSeidelMethod(N, A, b, maxIterations)
end = time.time()
print("\nGauss-Seidel Method:")
print("Time:", end - start)
#print(x2)
print(iterations2)
print(errors2[iterations2-1])

# Czy metody iteracyjne dla takich wartości elementów macierzy A zbiegają się?
# Dla obu metod przedstaw na wykresie jak zmienia się norma residuum w kolejnych iteracjach.
plt.plot(range(1, iterations+1), errors, label="Jacobi")
plt.plot(range(1, iterations2+1), errors2, label="Gauss-Seidel")
plt.yscale('log')
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.legend(loc="upper right")
plt.show()
