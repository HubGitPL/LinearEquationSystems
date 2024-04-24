from Macierz import Macierz

class Solutions:
    @staticmethod
    def jacobiMethod(N, A, b, maxIter, convergence=1e-9):
        x, xNext = Macierz(A.n, 1), Macierz(A.n, 1)
        errors = []
        iterations = 0
        errorBound = float('inf')
        while errorBound > convergence and iterations < maxIter:
            iterations += 1
            for i in range(A.n):
                sum1 = 0
                for j in range(i):
                    sum1 += A.tab[i][j] * xNext.tab[j][0]
                sum2 = 0
                for j in range(i + 1, A.m):
                    sum2 += A.tab[i][j] * x.tab[j][0]
                xNext.tab[i][0] = (b.tab[i][0] - sum1 - sum2) / A.tab[i][i]
            res = A * xNext - b
            errors.append(res.norm())
            x = xNext
            errorBound = errors[-1]
            if errorBound < convergence:
                break

        return xNext, iterations, errors

    @staticmethod
    def gaussSeidelMethod(N, A, b, maxIter, convergence=1e-9):
        x, xNext = Macierz(A.n, 1), Macierz(A.n, 1)
        errors = []
        iterations = 0
        errorBound = float('inf')
        while errorBound > convergence and iterations < maxIter:
            iterations += 1
            for i in range(A.n):
                sum1 = 0
                for j in range(i):
                    sum1 += A.tab[i][j] * xNext.tab[j][0]
                sum2 = 0
                for j in range(i + 1, A.m):
                    sum2 += A.tab[i][j] * x.tab[j][0]
                xNext.tab[i][0] = (b.tab[i][0] - sum1 - sum2) / A.tab[i][i]
            res = A * xNext - b
            errors.append(res.norm())
            x = xNext
            errorBound = errors[-1]
            if errorBound < convergence:
                break

        return xNext, iterations, errors






