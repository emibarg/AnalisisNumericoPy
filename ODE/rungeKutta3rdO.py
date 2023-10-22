## Runge-Kutta (3rd order) method for solving ODEs
## y' = f(x,y), y(x0) = y0
## x0 = initial x value
## y0 = initial y value
## h = step size
## n = number of steps
## f = function f(x,y)
## Returns x and y arrays
## Returns k1, k2 and k3 arrays
import numpy as np
import math
def rungeKutta3rdO(x0, y0, h, n, f):
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0] = x0
    y[0] = y0
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    k3 = np.zeros(n)
    for i in range(n):
        k1[i] = h * f(x[i], y[i])
        k2[i] = h * f(x[i] + h / 2, y[i] + k1[i] / 2)
        k3[i] = h * f(x[i] + h, y[i] - k1[i] + 2 * k2[i])
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + (k1[i] + 4 * k2[i] + k3[i]) / 6
    return x, y, k1, k2, k3
# Example usage:
def f(x, y):
    return pow(math.e, 0.8*x) - 0.5*y
x0 = 0
y0 = 2
h = 0.1
n = 7
x, y, k1, k2, k3 = rungeKutta3rdO(x0, y0, h, n, f)
print("x values:")
print(x)
print("y values:")
print(y)
print("k1 values:")
print(k1)
print("k2 values:")
print(k2)
print("k3 values:")
print(k3)
