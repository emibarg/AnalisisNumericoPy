import numpy as np

def bisection_method(func, a, b, err):
    def f(x):
        return eval(func)
    
    if f(a) * f(b) >= 0:
        print("No hay raices o hay multiples raices en este intervalo.")
        return None
    
    error = abs(b - a)
    iterations = 0
    results = []  # List to store iteration results
    while error > err:
        c = (b + a) / 2
        iterations += 1
        if f(c) == 0:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        error = abs(b - a)
        results.append((iterations, a, c, b, f(a), f(c), f(b), error))
    
    return (a + b) / 2, results  # Return the root and the list of iteration results

def barrerfunc(func, a, b, step, err):
    def f(x):
        return eval(func)
    roots = []
    c = a + step
    while c <= b:
        if f(a) * f(c) < 0:
            root, results = bisection_method(func, a, c, err)
            if root is not None:
                roots.append((root, results))
        a = c
        c += step
    
    return roots

# Example usage
roots = barrerfunc("-0.874*x**2 + 1.750*x + 2.627", -10, 10, 0.3, 0.001)

# Print the table of iteration results
for i, (root, results) in enumerate(roots):
    print(f"Root {i + 1}: {root}")
    print("Iterations\t   a\t\tc\t\t   b\t\tf(a)\t\tf(c)\t\tf(b)\t\tError")
    for iteration, a, c, b, fa, fc, fb, error in results:
        print(f"{iteration}\t\t{a:.6f}\t{c:.6f}\t{b:.6f}\t{fa:.6f}\t{fc:.6f}\t{fb:.6f}\t{error:.6f}")
    print()
