import numpy as np

def lagrange_basis_polynomial(x, k):
    """
    Compute the k-th Lagrange basis polynomial for given data points.

    Parameters:
    x: numpy.ndarray
        Array of x-coordinates of data points.
    k: int
        Index of the basis polynomial to compute.

    Returns:
    numpy.ndarray
        The k-th Lagrange basis polynomial as an array of coefficients.
    """
    n = len(x)
    basis = np.ones(n)
    for j in range(n):
        if j != k:
            basis *= (np.poly([x[j]]) / (x[k] - x[j]))
    return basis

def lagrange_interpolation(x, y, xi):
    """
    Perform Lagrange polynomial interpolation.

    Parameters:
    x: numpy.ndarray
        Array of x-coordinates of data points.
    y: numpy.ndarray
        Array of y-coordinates of data points.
    xi: float
        The x-coordinate at which to evaluate the interpolated polynomial.

    Returns:
    float
        The interpolated y-coordinate at xi.
    """
    n = len(x)
    interpolated_y = 0.0

    for k in range(n):
        basis_k = lagrange_basis_polynomial(x, k)
        interpolated_y += y[k] * np.polyval(basis_k, xi)

    return interpolated_y

# Example usage:
x_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y_data = np.array([0.0, 1.0, 0.0, 1.0, 0.0])
xi = 2.5

interpolated_y = lagrange_interpolation(x_data, y_data, xi)
print(f"Interpolated y at x={xi}: {interpolated_y}")
