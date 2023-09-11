from tabulate import tabulate
import math

def secant(f, x0, x1, epsilon, max_iter):
    '''Approximate solution of f(x)=0 by the secant method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    x0 : number
        Initial guess for the solution f(x)=0.
    x1 : number
        Another initial guess for the solution f(x)=0 (different from x0).
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of the secant method.

    Returns
    -------
    xn : number
        Implement the secant method: compute the linear approximation
        of f(x) between x0 and x1 and find the x intercept.
        Continue until abs(f(xn)) < epsilon or max_iter is reached.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secant(f, 1, 2, 1e-8, 10)
    Found solution after 6 iterations.
    1.618033988749989
    '''
    table = []

    for n in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        row = [n, x0, fx0]
        table.append(row)
        
        if abs(fx1) < epsilon:
            print(tabulate(table, headers=["Iteration", "x0", "f(x0)"]))
            print('Found solution after', n, 'iterations.')
            return x1
        
        if fx1 == fx0:
            print(tabulate(table, headers=["Iteration", "x0", "f(x0)"]))
            print('Secant method failed: Division by zero.')
            return None
        
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        x0, x1 = x1, x2
    
    print(tabulate(table, headers=["Iteration", "x0", "f(x0)"]))
    print('Exceeded maximum iterations. No solution found.')
    return None

f = lambda x: math.e**-x -x
secant(f, 1, 2, 1e-3, 6)
