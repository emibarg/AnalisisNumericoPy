import numpy as np
import pandas as pd

def newton_interpolation_table(x, y):
    """
    Create a table of Newton's divided difference coefficients.

    Parameters:
    x: numpy.ndarray
        Array of x-coordinates of data points.
    y: numpy.ndarray
        Array of y-coordinates of data points.

    Returns:
    pd.DataFrame
        A DataFrame representing the divided difference table.
    """
    n = len(x)
    fdd = np.zeros((n, n))  # Initialize divided difference table

    # Fill in the first column with the y-values
    fdd[:, 0] = y

    # Compute divided difference coefficients
    for j in range(1, n):
        for i in range(n - j):
            fdd[i, j] = (fdd[i + 1, j - 1] - fdd[i, j - 1]) / (x[i + j] - x[i])

    # Create a DataFrame for the coefficients
    coef_table = pd.DataFrame(fdd, columns=["f[x{0}]".format(i) for i in range(n)])

    return coef_table

def newton_interpolation_polynomial(x, coef_table):
    """
    Create and format the Newton interpolation polynomial.

    Parameters:
    x: numpy.ndarray
        Array of x-coordinates of data points.
    coef_table: pd.DataFrame
        The divided difference table.

    Returns:
    str
        A string representation of the Newton interpolation polynomial.
    """
    n = len(x)
    coefficients = coef_table.iloc[0]  # Coefficients from the first row of the divided difference table

    # Initialize the polynomial string
    polynomial_str = ""

    for i in range(n):
        term_str = str(coefficients[i])
        for j in range(i):
            term_str += "*(x - {0})".format(x[j])
        polynomial_str += term_str

        if i < n - 1:
            polynomial_str += " + "

    return polynomial_str

# Example usage:
x_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y_data = np.array([0.0, 1.0, 0.0, 1.0, 0.0])

coef_table = newton_interpolation_table(x_data, y_data)
print("Divided Difference Coefficients Table:")
print(coef_table)

polynomial = newton_interpolation_polynomial(x_data, coef_table)
print("Newton Interpolation Polynomial:")
print(polynomial)
