import numpy as np
import math
from tabulate import tabulate

def RK2(h, inicio, final, Y0, f):
    """
    Runge-Kutta (2nd order) method for solving ODEs
    y' = f(x,y), y(inicio) = Y0
    h = step size
    inicio = initial x value
    final = final x value
    f = function f(x,y)
    Returns x and y arrays
    Returns K1 and K2 arrays
    """
    x = np.arange(inicio, final + h, h)
    y = np.zeros(len(x))
    K1 = np.zeros(len(x))
    K2 = np.zeros(len(x))
    y[0] = Y0
    for i in range(len(x) - 1):
        K1[i] = f(x[i], y[i])
        K2[i] = f(x[i] + h, y[i] + K1[i] * h)
        y[i + 1] = y[i] + (0.5 * K1[i] + 0.5 * K2[i]) * h
    K1[-1] = f(x[-1], y[-1])
    K2[-1] = f(x[-1] + h, y[-1] + K1[-1] * h)
    return x, y, K1, K2

# Example usage:
def f(x, y):
    return math.e**(0.8*x) - 0.5*y

inicio = 0
final = 4
Y0 = 2
h = 0.1

x, y, K1, K2 = RK2(h, inicio, final, Y0, f)

# Format the output as a table
table = [['x', 'y', 'K1', 'K2']]
for i in range(len(x)):
    table.append([f'{x[i]:.1f}', f'{y[i]:.4f}', f'{K1[i]:.4f}', f'{K2[i]:.4f}'])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))