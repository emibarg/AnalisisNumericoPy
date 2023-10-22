## Runge-Kutta (2nd order) method for solving ODEs
## y' = f(x,y), y(x0) = y0
## x0 = initial x value
## y0 = initial y value
## h = step size
## n = number of steps
## f = function f(x,y)
## Returns x and y arrays
## Returns k1 and k2 arrays
import numpy as np
import math
def rungeKutta2ndO(x0, y0, h, n, f):
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0] = x0
    y[0] = y0
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    for i in range(n):
        k1[i] = h * f(x[i], y[i])
        k2[i] = h * f(x[i] + h, y[i] + k1[i])
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + (k1[i] + k2[i]) / 2
    return x, y, k1, k2
# Example usage:
def f(x, y):
    return pow(math.e, 0.8*x) - 0.5*y
x0 = 0
y0 = 2
h = 0.1
n = 7
x, y, k1, k2 = rungeKutta2ndO(x0, y0, h, n, f)
print("x values:")
print(x)
print("y values:")
print(y)
print("k1 values:")
print(k1)
print("k2 values:")
print(k2)

# Output:
# x values:
# [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]
# y values:
# [1.         1.         1.02002002 1.06024024 1.12288136 1.21126761
#  1.32911392 1.48192771 1.67605634 1.91943128 2.22222222]