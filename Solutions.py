from Macierz import Macierz

class Solutions:

    @staticmethod
    def jacobiMethod(N, A, b, maxIter, convergence=1e-9):
        x = Macierz(N, 1)
        res = float('inf')
        res_vect = []
        iterations = 0
        while res > convergence and iterations < maxIter:
            iterations += 1
            xNext = Macierz(N, 1)
            for i in range(N):
                sum1 = 0
                for j in range(N):
                    if i != j:
                        sum1 += A.tab[i][j] * x.tab[j][0]
                xNext.tab[i][0] = (b.tab[i][0] - sum1) / A.tab[i][i]
            res = A * xNext - b
            res_vect.append(res.norm())
            res = res_vect[-1]
            x = xNext
        return xNext, iterations, res_vect


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






