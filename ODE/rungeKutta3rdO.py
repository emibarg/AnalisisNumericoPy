import numpy as np
import math


def RK3(h, inicio, final, Y0, f):
    """
    Runge-Kutta (3rd order) method for solving ODEs
    y' = f(x,y), y(inicio) = Y0
    h = step size
    inicio = initial x value
    final = final x value
    f = function f(x,y)
    Returns x and y arrays
    Returns K1, K2, and K3 arrays
    """
    x = np.arange(inicio, final + h, h)
    y = np.zeros(len(x))
    K1 = np.zeros(len(x))
    K2 = np.zeros(len(x))
    K3 = np.zeros(len(x))
    y[0] = Y0
    for i in range(len(x) - 1):
        K1[i] = f(x[i], y[i])
        K2[i] = f(x[i] + h/2, y[i] + K1[i] * h/2)
        K3[i] = f(x[i] + h, y[i] - K1[i] * h + 2 * K2[i] * h)
        y[i + 1] = y[i] + (1/6 * K1[i] + 2/3 * K2[i] + 1/6 * K3[i]) * h
    K1[-1] = f(x[-1], y[-1])
    K2[-1] = f(x[-1] + h/2, y[-1] + K1[-1] * h/2)
    K3[-1] = f(x[-1] + h, y[-1] - K1[-1] * h + 2 * K2[-1] * h)
    return x, y, K1, K2, K3
##Example usage

def f(x, y):
    return math.e**(0.8*x) - 0.5*y

inicio = 0
final = 4
Y0 = 2
h = 0.1

x, y, K1, K2,K3 = RK3(h, inicio, final, Y0, f)

print("x values:")
print(x)
print("y values:")
print(y)
print("K1 values:")
print(K1)
print("K2 values:")
print(K2)
print("K3 values:")
print(K3)