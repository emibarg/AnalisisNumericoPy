import numpy as np

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def evaluate(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
        return result

    def print(self):
        print(self.coefficients)

def cubic_spline_natural(Xi, Yi):
    n = len(Xi)
    Hj = [Xi[i + 1] - Xi[i] for i in range(n - 1)]
    Alphaj = [0] * n

    for i in range(1, n - 1):
        Alphaj[i] = (3.0 * (Yi[i + 1] - Yi[i]) / Hj[i]) - (3.0 * (Yi[i] - Yi[i - 1]) / Hj[i - 1])

    Lj = [0] * n
    MuJ = [0] * n
    Zj = [0] * n

    Lj[0] = 1
    MuJ[0] = 0
    Zj[0] = 0

    for i in range(1, n - 1):
        Lj[i] = 2.0 * (Xi[i + 1] - Xi[i - 1]) - Hj[i - 1] * MuJ[i - 1]
        MuJ[i] = Hj[i] / Lj[i]
        Zj[i] = (Alphaj[i] - Hj[i - 1] * Zj[i - 1]) / Lj[i]

    Ci = [0] * n
    Lj[-1] = 1
    Zj[-1] = 0

    for i in range(n - 2, -1, -1):
        Ci[i] = Zj[i] - MuJ[i] * Ci[i + 1]

    Bi = [0] * (n - 1)
    Di = [0] * (n - 1)

    for i in range(n - 1):
        Bi[i] = (Yi[i + 1] - Yi[i]) / Hj[i] - (Hj[i] * (Ci[i + 1] + 2.0 * Ci[i])) / 3.0
        Di[i] = (Ci[i + 1] - Ci[i]) / (3.0 * Hj[i])

    results = []

    for j in range(n - 1):
        coefficients = [Yi[j], Bi[j], Ci[j], Di[j]]
        results.append(Polynomial(coefficients))

    return results

# Example usage:
Xi = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
Yi = [1.0, 2.1190, 2.9100, 3.9450, 5.72, 8.6950]

result = cubic_spline_natural(Xi, Yi)

for i, poly in enumerate(result):
    print(f"Segment {i + 1}:")
    poly.print()
