import numpy as np

def newton_interpolation(x, y, xi):
    """
    Perform polynomial interpolation using Newton's divided difference method.

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
    fdd = np.zeros((n, n))  # Initialize divided difference table

    # Fill in the first column with the y-values
    fdd[:, 0] = y

    # Compute divided difference coefficients
    for j in range(1, n):
        for i in range(n - j):
            fdd[i, j] = (fdd[i + 1, j - 1] - fdd[i, j - 1]) / (x[i + j] - x[i])

    # Evaluate the polynomial at xi using Horner's method
    result = fdd[0, 0]
    for j in range(1, n):
        term = fdd[0, j]
        for i in range(j):
            term *= (xi - x[i])
        result += term

    return result

# Example usage:
x_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y_data = np.array([0.0, 1.0, 0.0, 1.0, 0.0])
xi = 2.5

interpolated_y = newton_interpolation(x_data, y_data, xi)
print(f"Interpolated y at x={xi}: {interpolated_y}")
