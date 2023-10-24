##Simpson method for integration
##f = function f(x)
##a = lower bound
##b = upper bound
##n = number of subintervals
##Returns the integral
##Also returns a table with the calculations with i, Xi, f(Xi)


import numpy as np
import math
def simpson(f,a,b,n):
    if n%2==1:
        print("n must be even")
        return None
    h=(b-a)/n
    s=f(a)+f(b)
    for i in range(1,n,2):
        s+=4*f(a+i*h)
    for i in range(2,n-1,2):
        s+=2*f(a+i*h)
    print("{:<10} | {:<10} | {:<10}".format("i", "Xi", "f(Xi)"))
    print("{:<10} | {:<10} | {:<10}".format(0, round(a, 5), round(f(a))))
    for i in range(1, n):
        print("{:<10} | {:<10} | {:<10}".format(i, round(a + i * h, 5), round(f(a + i * h), 5)))
    print("{:<10} | {:<10} | {:<10}".format(n, round(a + n * h, 5), round(f(a + n * h), 5)))

    print("El resultado es: ")
    return s*h/3
def f(x):
    return 8 + 5*math.cos(x)
print(simpson(f,0,np.pi,10))