##Three point difference method
import numpy as np

def threePDiff(X, Y):
    size = len(X)
    resultados = np.zeros(size)

    for i in range(size):
        valor = 0

        # Centrada:
        if i + 1 < size and i - 1 >= 0:
            valor += Y[i + 1] - Y[i - 1]
            valor /= X[i + 1] - X[i - 1]
        elif i + 2 < size:
            # Progresiva
            valor += -3 * Y[i] + 4 * Y[i + 1] - Y[i + 2]
            valor /= 2 * (X[i + 1] - X[i])
        elif i - 2 >= 0:
            # Regresiva
            valor += Y[i - 2] - 4 * Y[i - 1] + 3 * Y[i]
            valor /= 2 * (X[i] - X[i - 1])

        resultados[i] = valor

    print("{:<10} | {:<10} | {:<10}".format("Xi", "f(Xi)", "f'(Xi)"))
    for i in range(size):
        print("{:<10} | {:<10} | {:<10}".format(X[i], Y[i], resultados[i]))

# Example usage
X = [0, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70]
Y = [1.0, 1.09965, 1.19706, 1.28957, 1.37406,1.44689,1.50386,1.54020]
threePDiff(X, Y)
