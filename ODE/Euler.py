import numpy as np
import math

def euler(x0, y0, h, n, f):
    """
    Euler method for solving ODEs
    y' = f(x,y), y(x0) = y0
    x0 = initial x value
    y0 = initial y value
    h = step size
    n = number of steps
    f = function f(x,y)
    Returns x and y arrays
    """
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0] = x0
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
        x[i + 1] = x[i] + h
    return x, y

def f(x, y):
    return pow(math.e, 0.8*x) - 0.5*y

x0 = 0
y0 = 2
h = 0.1
n = 40
x, y = euler(x0, y0, h, n, f)

print("x values\t y values")
for i in range(len(x)):
    print("{:.2f}\t\t {:.4f}".format(x[i], y[i]))