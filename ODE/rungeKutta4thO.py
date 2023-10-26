import numpy as np
import math
from tabulate import tabulate

def RK4(h, inicio, final, Y0, f):
    """
    Runge-Kutta (4th order) method for solving ODEs
    y' = f(x,y), y(inicio) = Y0
    h = step size
    inicio = initial x value
    final = final x value
    f = function f(x,y)
    Returns x and y arrays
    Returns K1, K2, K3, and K4 arrays
    """
    x = np.arange(inicio, final + h, h)
    y = np.zeros(len(x))
    K1 = np.zeros(len(x))
    K2 = np.zeros(len(x))
    K3 = np.zeros(len(x))
    K4 = np.zeros(len(x))
    y[0] = Y0
    for i in range(len(x) - 1):
        K1[i] = f(x[i], y[i])
        K2[i] = f(x[i] + h/2, y[i] + K1[i] * h/2)
        K3[i] = f(x[i] + h/2, y[i] + K2[i] * h/2)
        K4[i] = f(x[i] + h, y[i] + K3[i] * h)
        y[i + 1] = y[i] + (1/6 * K1[i] + 1/3 * K2[i] + 1/3 * K3[i] + 1/6 * K4[i]) * h
    K1[-1] = f(x[-1], y[-1])
    K2[-1] = f(x[-1] + h/2, y[-1] + K1[-1] * h/2)
    K3[-1] = f(x[-1] + h/2, y[-1] + K2[-1] * h/2)
    K4[-1] = f(x[-1] + h, y[-1] + K3[-1] * h)
    return x, y, K1, K2, K3, K4

# Example usage:
def f(x, y):
    return pow(math.e, 0.8*x) - 0.5*y

inicio = 0
final = 4
Y0 = 2
h = 0.1

x, y, k1, k2, k3, k4 = RK4(h, inicio, final, Y0, f)

# Format the output as a table
table = [['x', 'y', 'K1', 'K2', 'K3', 'K4']]
for i in range(len(x)):
    table.append([f'{x[i]:.1f}', f'{y[i]:.4f}', f'{k1[i]:.4f}', f'{k2[i]:.4f}', f'{k3[i]:.4f}', f'{k4[i]:.4f}'])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))