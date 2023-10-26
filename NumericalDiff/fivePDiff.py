import numpy as np
from tabulate import tabulate

def fivePDiff(X, Y):
    size = len(X)
    resultados = np.zeros(size)

    table = [["Xi", "f(Xi)", "f'(Xi)", "Formula"]]
    for i in range(size):
        valor = 0
        formula = ""

        # Centrada:
        if i + 2 < size and i - 2 >= 0:
            valor += Y[i - 2] - 8 * Y[i - 1] + 8 * Y[i + 1] - Y[i + 2]
            valor /= 12 * (X[i + 1] - X[i])
            formula = "Centrada"
        elif i + 4 < size:
            # Progresiva
            valor += -25 * Y[i] + 48 * Y[i + 1] - 36 * Y[i + 2] + 16 * Y[i + 3] - 3 * Y[i + 4]
            valor /= 12 * (X[i + 1] - X[i])
            formula = "Progresiva"
        elif i - 4 >= 0:
            # Regresiva
            valor += 3 * Y[i - 4] - 16 * Y[i - 3] + 36 * Y[i - 2] - 48 * Y[i - 1] + 25 * Y[i]
            valor /= 12 * (X[i] - X[i - 1])
            formula = "Regresiva"
        else:
            print("! No se puede calcular la derivada en el punto", X[i], "!")

        resultados[i] = valor

        table.append([X[i], Y[i], resultados[i], formula])

    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

# Example usage
X = [0.0000 ,0.1000, 0.2000, 0.3000, 0.4000, 0.5000, 0.6000, 0.7000]
Y = [1.0000, 1.09965,1.19706, 1.28957, 1.37406, 1.44689, 1.50386, 1.54020]
fivePDiff(X, Y)