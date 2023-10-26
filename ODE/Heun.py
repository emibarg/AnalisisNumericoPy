import numpy as np
import math
from tabulate import tabulate

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

def heun(x0, y0, h, n, f):
    """
    Heun method for solving ODEs
    y' = f(x,y), y(x0) = y0
    x0 = initial x value
    y0 = initial y value
    h = step size
    n = number of steps
    f = function f(x,y)
    Returns x, y, and euler arrays
    """
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    euler = np.zeros(n + 1)
    x[0] = x0
    y[0] = y0
    euler[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + (h / 2) * (f(x[i], y[i]) + f(x[i] + h, y[i] + h * f(x[i], y[i])))
        x[i + 1] = x[i] + h
        euler[i + 1] = euler[i] + h * f(x[i], euler[i])
    return x, y, euler

def f(x, y):
    return pow(math.e, 0.8*x) - 0.5*y

x0 = 0
y0 = 2 
h = 0.1
n = 40
x, y, euler = heun(x0, y0, h, n, f)

# Format the output as a table
table = [['y', 'y prima', 'euler']]
for i in range(len(x)):
    table.append([f'{x[i]:.2f}', f'{y[i]:.4f}', f'{euler[i]:.4f}'])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))