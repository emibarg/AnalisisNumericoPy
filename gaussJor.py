import numpy as np

def gaussian_elimination(A, b):
    '''
    Solve a system of linear equations Ax = b using Gaussian elimination.

    Parameters:
    A: numpy.ndarray
        Coefficient matrix.
    b: numpy.ndarray
        Right-hand side vector.

    Returns:
    x: numpy.ndarray
        Solution vector.
    '''

    # Check if A is square
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square.")

    n = len(b)
    # Augmenting the matrix A with vector b
    Ab = np.column_stack((A, b))

    # Forward elimination
    for i in range(n):
        # Partial pivoting to avoid division by small numbers
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]

        pivot = Ab[i, i]
        if pivot == 0:
            raise ValueError("Matrix is singular, cannot proceed.")

        Ab[i, :] = Ab[i, :] / pivot

        for j in range(i + 1, n):
            factor = Ab[j, i]
            Ab[j, :] -= factor * Ab[i, :]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1]
        for j in range(i + 1, n):
            x[i] -= Ab[i, j] * x[j]

    return x

# Example usage:
A = np.array([[2, 1, -1], [1, 3, 2], [3, 2, -3]], dtype=float)
b = np.array([8, 10, 0], dtype=float)
x = gaussian_elimination(A, b)
print("Solution x:", x)
