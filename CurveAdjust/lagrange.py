import sympy as sp

def display_interpolated_function(Xi, Yi):
    x = sp.symbols('x')
    interpolated_function = 0
    Lagrange_polynomials = []

    for i in range(len(Xi)):
        term = Yi[i]
        Lagrange_polynomial = 1
        for j in range(len(Xi)):
            if j != i:
                term *= (x - Xi[j]) / (Xi[i] - Xi[j])
                Lagrange_polynomial *= (x - Xi[j]) / (Xi[i] - Xi[j])
        interpolated_function += term
        Lagrange_polynomials.append(Lagrange_polynomial)

    simplified_function = sp.simplify(interpolated_function)
    
    print(f"f(x) = {simplified_function}")
    
    for i, poly in enumerate(Lagrange_polynomials):
        simplified_poly = sp.simplify(poly)
        print(f"L{i}(x) = {simplified_poly}")

def lagrange_interpolation(Xi, Yi):
    display_interpolated_function(Xi, Yi)

# Example usage:
Xi = [0.0, 1.0, 2.0, 3.0]
Yi = [1.0, 2.7182, 7.3891, 20.0855]

lagrange_interpolation(Xi, Yi)
