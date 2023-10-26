##Simpson method for integration with points 
##X = list of points
##Y = list of f(X)
##Returns the integral
##Also returns a table with the calculations with i, Xi, f(Xi)
import numpy as np
import math
from tabulate import tabulate

def simpson(X, Y):
    size = len(X)
    h = X[size - 1] - X[0]
    h /= size - 1
    sum = 0

    table = [["i", "Xi", "f(Xi)"]]
    for i in range(size):
        table.append([i, X[i], Y[i]])

    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    for i in range(1, size - 1):
        if i % 2 == 0:
            sum += 2. * Y[i]
        else:
            sum += 4. * Y[i]

    sum += Y[0]
    sum += Y[size - 1]
    sum *= h / 3

    return sum

X = [0,0.3141,0.6283,0.9425,1.2566,1.5708,1.8850,2.1991,2.5133,2.8274,3.1416]
Y = [13,12.7553, 12.0451, 10.9389, 9.5450, 8, 6.4549, 5.0611, 3.9549, 3.2447, 3]

##X = [0, 0.10, 0.20, 0.30, 0.40, 0.50]
##Y = [1.0, 7.0, 4.0, 3.0, 5.0, 9.0]
print(simpson(X, Y))