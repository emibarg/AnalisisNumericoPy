import numpy as np

def threePDiff(X, Y):
    size = len(X)
    resultados = np.zeros(size)

    print("{:<10} | {:<10} | {:<10} | {:<10}".format("Xi", "f(Xi)", "f'(Xi)", "Formula"))
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

        print("{:<10} | {:<10} | {:<10} | {:<10}".format(X[i], Y[i], resultados[i], formula))

# Example usage
X = [0.0000 ,0.5000, 1.0000, 1.5000, 2.0000]
Y = [0.0000, 0.4207, 0.4546, 0.0706, -0.3784]
threePDiff(X, Y)