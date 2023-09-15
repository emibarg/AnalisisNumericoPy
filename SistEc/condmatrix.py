import numpy as np

# Definir una matriz A
A = np.array([[3, -0.1, -0.2],
              [0.1, 7,-0.3],
              [0.3, -0.2, 10]])

# Calcular el numero de condición utilizando la norma 2 (valor predeterminado)
cond_A = np.linalg.cond(A)

print("Numero de condicion de A:", cond_A)
