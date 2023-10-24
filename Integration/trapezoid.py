##Trapezoid method for integration
##f = function f(x)
##a = lower bound
##b = upper bound
##n = number of subintervals
##Returns the integral
##Also returns a table with the calculations with i, Xi, f(Xi)
import numpy as np
import math

def trapezoid(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    print("{:<10} | {:<10} | {:<10}".format("i", "Xi", "f(Xi)"))
    print("{:<10} | {:<10} | {:<10}".format(0, round(a, 5), round(f(a), 5)))
    for i in range(1, n):
        s += f(a + i * h)
        print("{:<10} | {:<10} | {:<10}".format(i, round(a + i * h, 5), round(f(a + i * h), 5)))
    print("{:<10} | {:<10} | {:<10}".format(n, round(a + n * h, 5), round(f(a + n * h), 5)))
    print("El resultado es: ")
    return round(h * s, 5)

def f(x):
    return 8 + 5*math.cos(x)

a = 0
b = math.pi
n = 10
print(trapezoid(f, a, b, n))