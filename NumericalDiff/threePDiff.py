import numpy as np
from tabulate import tabulate

def threePDiff(X, Y):
    size = len(X)
    resultados = np.zeros(size)

    table = [["Xi", "f(Xi)", "f'(Xi)", "Formula"]]
    for i in range(size):
        valor = 0
        formula = ""

        # Centrada:
        if i + 1 < size and i - 1 >= 0:
            valor += Y[i + 1] - Y[i - 1]
            valor /= X[i + 1] - X[i - 1]
            formula = "Centrada"
        elif i + 2 < size:
            # Progresiva
            valor += -3 * Y[i] + 4 * Y[i + 1] - Y[i + 2]
            valor /= 2 * (X[i + 1] - X[i])
            formula = "Progresiva"
        elif i - 2 >= 0:
            # Regresiva
            valor += Y[i - 2] - 4 * Y[i - 1] + 3 * Y[i]
            valor /= 2 * (X[i] - X[i - 1])
            formula = "Regresiva"

        resultados[i] = valor

        table.append([X[i], Y[i], resultados[i], formula])

    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

# Example usage
X = [0.0000 ,0.1000, 0.2000, 0.3000, 0.4000, 0.5000, 0.6000, 0.7000]
Y = [1.0000, 1.09965,1.19706, 1.28957, 1.37406, 1.44689, 1.50386, 1.54020]
threePDiff(X, Y)