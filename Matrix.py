from numpy import sin
from math import sqrt

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.tab = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(0)
            self.tab.append(row)

    def __str__(self):
        s = ""
        for i in range(self.n):
            for j in range(self.m):
                s += str(self.tab[i][j]) + " "
            s += "\n"
        return s

    def __add__(self, other):
        wynik = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                wynik.tab[i][j] = self.tab[i][j] + other.tab[i][j]
        return wynik

    def __sub__(self, other):
        wynik = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                wynik.tab[i][j] = self.tab[i][j] - other.tab[i][j]
        return wynik

    def __mul__(self, other):
        wynik = Matrix(self.n, other.m)
        #O(n^3) do poprawy
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    wynik.tab[i][j] += self.tab[i][k] * other.tab[k][j]
        return wynik

    #test
    def __eq__(self, other):
        if self.n != other.n or self.m != other.m:
            return False
        for i in range(self.n):
            for j in range(self.m):
                if self.tab[i][j] != other.tab[i][j]:
                    return False
        return True

    def print(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.tab[i][j], end=" ")
            print()

    @staticmethod
    def createMatrixA(N, a1, a2, a3):
        A = Matrix(N, N)
        for i in range(N):
            for j in range(N):
                if i == j:
                    A.tab[i][j] = a1
                elif i == j - 1 or i == j + 1:
                    A.tab[i][j] = a2
                elif i == j - 2 or i == j + 2:
                    A.tab[i][j] = a3
        return A

    @staticmethod
    def createColumnVector(N, fPlusOne):
        b = Matrix(N, 1)
        for i in range(N):
            b.tab[i][0] = sin(i * fPlusOne)
        return b

    @staticmethod
    def drukujPierwszyElement(self):
        print(self.tab[0][0])

    def norm(self):
        sum = 0
        for i in range(self.n):
            sum += self.tab[i][0] ** 2
        return sqrt(sum)

    def __copy__(self):
        A = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                A.tab[i][j] = self.tab[i][j]
        return A

    #get L for LU factorization
    @staticmethod
    def getL(N, A):
        L = Matrix(N, N)
        for i in range(N):
            for j in range(N):
                if i > j:
                    L.tab[i][j] = A.tab[i][j]
                elif i == j:
                    L.tab[i][j] = 1
        return L

    #get U for LU factorization
    @staticmethod
    def getU(N, A):
        U = Matrix(N, N)
        for i in range(N):
            for j in range(N):
                if i <= j:
                    U.tab[i][j] = A.tab[i][j]
        return U

    @staticmethod
    def luHandler(L, U, n):
        for i in range(1, n):
            for j in range(i):
                L.tab[i][j] = U.tab[i][j] / U.tab[j][j]
                for k in range(j, n):
                    U.tab[i][k] -= L.tab[i][j] * U.tab[j][k]
        return L, U

    @staticmethod
    def LYEqualsB(L, y, b):
        for i in range(L.n):
            sum = 0
            for j in range(i):
                sum += L.tab[i][j] * y.tab[j][0]
            y.tab[i][0] = b.tab[i][0] - sum
        return y

    @staticmethod
    def UXEqualsY(U, x, y):
        for i in range(U.n-1, -1, -1):
            sum = 0
            for j in range(i+1, U.n):
                sum += U.tab[i][j] * x.tab[j][0]
            x.tab[i][0] = (y.tab[i][0] - sum) / U.tab[i][i]
        return x

